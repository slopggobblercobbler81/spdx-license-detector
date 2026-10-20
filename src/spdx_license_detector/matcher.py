# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""SPDX license matching and similarity scoring engine."""

import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from spdx_license_detector.catalog import LicenseInfo, LICENSE_CATALOG, get_license_by_id
from spdx_license_detector.normalizer import LicenseNormalizer


@dataclass
class MatchResult:
    """Detailed outcome of license classification."""
    matched: bool
    license_info: Optional[LicenseInfo]
    spdx_id: Optional[str]
    confidence: float
    method: str
    detected_years: List[str]
    detected_holder: Optional[str]
    summary: str


SPDX_TAG_RE = re.compile(r"SPDX-License-Identifier:\s*([A-Za-z0-9._-]+)", re.IGNORECASE)


class LicenseMatcher:
    """Classifies input text against canonical SPDX license database."""

    def __init__(
        self,
        catalog: Optional[Dict[str, LicenseInfo]] = None,
        min_confidence: float = 0.65,
    ):
        self.catalog = catalog if catalog is not None else LICENSE_CATALOG
        self.min_confidence = min_confidence
        self.normalizer = LicenseNormalizer()

        # Precompute normalized tokens and ngrams for catalog entries
        self._cached_catalog = {}
        for spdx_id, info in self.catalog.items():
            norm = self.normalizer.normalize_text(info.text, strip_copyright=False)
            tokens = norm.split()
            bigrams = self.normalizer.get_ngrams(tokens, n=2)
            trigrams = self.normalizer.get_ngrams(tokens, n=3)
            self._cached_catalog[spdx_id] = {
                "norm": norm,
                "tokens": tokens,
                "token_set": set(tokens),
                "bigrams": bigrams,
                "trigrams": trigrams,
            }

    def match(self, text: str) -> MatchResult:
        """Classify license text and return the best match."""
        if not text or not text.strip():
            return MatchResult(
                matched=False,
                license_info=None,
                spdx_id=None,
                confidence=0.0,
                method="none",
                detected_years=[],
                detected_holder=None,
                summary="Empty or blank input text",
            )

        years, holder = self.normalizer.extract_metadata(text)

        # 1. Check for SPDX tag in text
        tag_match = SPDX_TAG_RE.search(text)
        if tag_match:
            tag_id = tag_match.group(1).strip()
            info = get_license_by_id(tag_id)
            if info:
                return MatchResult(
                    matched=True,
                    license_info=info,
                    spdx_id=info.spdx_id,
                    confidence=1.0,
                    method="spdx_tag",
                    detected_years=years,
                    detected_holder=holder,
                    summary=f"Explicit SPDX identifier tag: {info.spdx_id}",
                )

        # 2. Normalize input text
        norm_input = self.normalizer.normalize_text(text, strip_copyright=True)
        if not norm_input:
            return MatchResult(
                matched=False,
                license_info=None,
                spdx_id=None,
                confidence=0.0,
                method="none",
                detected_years=years,
                detected_holder=holder,
                summary="No substantial text after removing copyright headers",
            )

        input_tokens = norm_input.split()
        input_token_set = set(input_tokens)
        input_bigrams = self.normalizer.get_ngrams(input_tokens, n=2)
        input_trigrams = self.normalizer.get_ngrams(input_tokens, n=3)

        # 3. Exact match check
        for spdx_id, cached in self._cached_catalog.items():
            if norm_input == cached["norm"]:
                info = self.catalog[spdx_id]
                return MatchResult(
                    matched=True,
                    license_info=info,
                    spdx_id=spdx_id,
                    confidence=1.0,
                    method="exact_match",
                    detected_years=years,
                    detected_holder=holder,
                    summary=f"Exact text match for {spdx_id}",
                )

        # 4. Check distinctive phrases
        for spdx_id, info in self.catalog.items():
            if info.distinctive_phrases:
                matched_phrases = 0
                for phrase in info.distinctive_phrases:
                    norm_phrase = self.normalizer.normalize_text(phrase, strip_copyright=False)
                    if norm_phrase in norm_input:
                        matched_phrases += 1

                # If 2 or more distinctive phrases matched, or 1 very specific phrase matched
                if (matched_phrases >= 2) or (matched_phrases >= 1 and any(
                    self.normalizer.normalize_text(p, strip_copyright=False) in norm_input
                    for p in [
                        "licensed under the apache license, version 2.0",
                        "apache license version 2.0",
                        "this is free and unencumbered software released into the public domain",
                        "creative commons legal code",
                        "gnu affero general public license",
                        "mozilla public license version 2.0",
                        "boost software license - version 1.0",
                    ]
                )):
                    return MatchResult(
                        matched=True,
                        license_info=info,
                        spdx_id=spdx_id,
                        confidence=0.95,
                        method="distinctive_phrases",
                        detected_years=years,
                        detected_holder=holder,
                        summary=f"Distinctive signature matched for {spdx_id}",
                    )

        # 5. N-gram similarity (Sørensen–Dice & token containment)
        best_id: Optional[str] = None
        best_score = 0.0

        for spdx_id, cached in self._cached_catalog.items():
            # Bigram dice
            b_inter = len(input_bigrams & cached["bigrams"])
            b_total = len(input_bigrams) + len(cached["bigrams"])
            b_dice = (2.0 * b_inter) / b_total if b_total > 0 else 0.0

            # Trigram dice
            t_inter = len(input_trigrams & cached["trigrams"])
            t_total = len(input_trigrams) + len(cached["trigrams"])
            t_dice = (2.0 * t_inter) / t_total if t_total > 0 else 0.0

            # Token overlap (containment relative to smaller)
            tok_inter = len(input_token_set & cached["token_set"])
            min_tok = min(len(input_token_set), len(cached["token_set"]))
            tok_containment = tok_inter / min_tok if min_tok > 0 else 0.0

            # Composite confidence score
            score = 0.45 * b_dice + 0.35 * t_dice + 0.20 * tok_containment

            if score > best_score:
                best_score = score
                best_id = spdx_id

        if best_id and best_score >= self.min_confidence:
            info = self.catalog[best_id]
            return MatchResult(
                matched=True,
                license_info=info,
                spdx_id=best_id,
                confidence=round(best_score, 4),
                method="similarity",
                detected_years=years,
                detected_holder=holder,
                summary=f"Detected {best_id} with {round(best_score * 100, 1)}% confidence",
            )

        return MatchResult(
            matched=False,
            license_info=None,
            spdx_id=None,
            confidence=round(best_score, 4),
            method="none",
            detected_years=years,
            detected_holder=holder,
            summary=f"Unrecognized license (best candidate: {best_id or 'none'} at {round(best_score * 100, 1)}% below threshold)",
        )
