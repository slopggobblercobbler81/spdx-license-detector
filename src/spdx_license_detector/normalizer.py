# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""Text normalization and preprocessing for license identification."""

import re
from typing import List, Set, Tuple, Optional


# Regex to identify copyright lines to remove for pure license comparison
COPYRIGHT_LINE_RE = re.compile(
    r"(?:^|\n)\s*(?:#|//|/\*|\*|--|;;)?\s*(?:copyright|copr\.|\(c\)|©)\s+.*?(?=\n|$)",
    re.IGNORECASE,
)
YEAR_RANGE_RE = re.compile(r"\b((?:19|20)\d{2})(?:\s*[-–]\s*((?:19|20)\d{2}))?\b")
HOLDER_RE = re.compile(
    r"(?:copyright|copr\.|\(c\)|©)\s*(?:(?:19|20)\d{2}(?:\s*[-–]\s*(?:19|20)\d{2})?\s*)?([^\n\r,.<>]+)",
    re.IGNORECASE,
)


class LicenseNormalizer:
    """Normalizes text by removing boilerplate variance and generating word tokens."""

    @staticmethod
    def extract_metadata(text: str) -> Tuple[List[str], Optional[str]]:
        """Extract copyright years and holder if present."""
        years = []
        for m in YEAR_RANGE_RE.finditer(text):
            start_yr, end_yr = m.group(1), m.group(2)
            years.append(f"{start_yr}-{end_yr}" if end_yr else start_yr)

        holder = None
        holder_match = HOLDER_RE.search(text)
        if holder_match:
            candidate = holder_match.group(1).strip()
            # Filter common spurious words
            if candidate and not candidate.lower().startswith(("all rights reserved", "under", "by")):
                holder = candidate

        return years, holder

    @staticmethod
    def strip_copyright(text: str) -> str:
        """Remove copyright notices and author claims from license text."""
        cleaned = COPYRIGHT_LINE_RE.sub("\n", text)
        return cleaned

    @classmethod
    def normalize_text(cls, text: str, strip_copyright: bool = True) -> str:
        """Fully normalize text: lowercase, ASCII quotes/dashes, punctuation removal, whitespace compaction."""
        if strip_copyright:
            text = cls.strip_copyright(text)

        # Replace smart quotes and dashes
        replacements = {
            "“": '"', "”": '"', "‘": "'", "’": "'",
            "—": "-", "–": "-", "…": "...", "\t": " ",
            "\r\n": "\n", "\r": "\n",
        }
        for k, v in replacements.items():
            text = text.replace(k, v)

        # Lowercase
        text = text.lower()

        # Remove punctuation except alphanumeric and space
        text = re.sub(r"[^\w\s]", " ", text)

        # Normalize whitespace
        text = re.sub(r"\s+", " ", text).strip()
        return text

    @classmethod
    def tokenize(cls, text: str, strip_copyright: bool = True) -> List[str]:
        """Convert text into normalized list of word tokens."""
        norm = cls.normalize_text(text, strip_copyright=strip_copyright)
        if not norm:
            return []
        return norm.split()

    @classmethod
    def get_ngrams(cls, tokens: List[str], n: int = 3) -> Set[Tuple[str, ...]]:
        """Generate word n-grams from a token list."""
        if len(tokens) < n:
            return {tuple(tokens)} if tokens else set()
        return {tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)}


def normalize_spdx_id(spdx_id: str) -> str:
    """Returns canonical formatted uppercase SPDX license identifier."""
    return spdx_id.strip().upper()
