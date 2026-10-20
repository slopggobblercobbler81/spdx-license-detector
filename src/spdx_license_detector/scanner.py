# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""Directory scanning for repository license detection."""

import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
from spdx_license_detector.matcher import LicenseMatcher, MatchResult


LICENSE_FILENAMES = {
    "license",
    "license.txt",
    "license.md",
    "license.rst",
    "licence",
    "licence.txt",
    "licence.md",
    "copying",
    "copying.txt",
    "copying.md",
    "unlicense",
    "unlicense.txt",
}

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".venv",
    "venv",
    "dist",
    "build",
    "target",
    ".tox",
}


@dataclass
class ScanResult:
    """Aggregated scan findings across a project directory."""
    directory: str
    files_checked: int
    matches: List[Tuple[str, MatchResult]]
    primary_license: Optional[str]
    confidence: float


class LicenseScanner:
    """Recursively locates and classifies license files within directory trees."""

    def __init__(self, matcher: Optional[LicenseMatcher] = None):
        self.matcher = matcher or LicenseMatcher()

    def scan_directory(self, target_dir: str, include_all_text: bool = False) -> ScanResult:
        """Scan a directory for license files and identify project licenses."""
        abs_dir = os.path.abspath(target_dir)
        matches: List[Tuple[str, MatchResult]] = []
        files_checked = 0

        for root, dirs, files in os.walk(abs_dir):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for fname in files:
                lower_name = fname.lower()
                is_license_file = lower_name in LICENSE_FILENAMES or lower_name.startswith("license.")

                if is_license_file or include_all_text:
                    filepath = os.path.join(root, fname)
                    files_checked += 1
                    try:
                        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                            content = f.read()
                    except OSError:
                        continue

                    res = self.matcher.match(content)
                    if res.matched:
                        matches.append((filepath, res))

        # Determine primary license (highest confidence root license)
        primary = None
        max_conf = 0.0

        for path, res in matches:
            # Prefer root-level license file
            is_root = os.path.dirname(os.path.abspath(path)) == abs_dir
            score = res.confidence * (1.2 if is_root else 1.0)
            if score > max_conf:
                max_conf = score
                primary = res.spdx_id

        return ScanResult(
            directory=target_dir,
            files_checked=files_checked,
            matches=matches,
            primary_license=primary,
            confidence=min(1.0, max_conf),
        )
