# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""spdx-license-detector: Fast offline classifier for open-source LICENSE files."""

__version__ = "0.1.0"
__author__ = "slopggobblercobbler81"
__license__ = "MIT"

from spdx_license_detector.catalog import LicenseInfo, LICENSE_CATALOG, get_license_by_id
from spdx_license_detector.matcher import LicenseMatcher, MatchResult
from spdx_license_detector.normalizer import LicenseNormalizer
from spdx_license_detector.scanner import LicenseScanner, ScanResult

__all__ = [
    "__version__",
    "LicenseInfo",
    "LICENSE_CATALOG",
    "get_license_by_id",
    "LicenseMatcher",
    "MatchResult",
    "LicenseNormalizer",
    "LicenseScanner",
    "ScanResult",
]
