# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""Tests for license catalog and metadata."""

import unittest
from spdx_license_detector.catalog import LICENSE_CATALOG, get_license_by_id


class TestCatalog(unittest.TestCase):
    def test_catalog_contains_core_licenses(self):
        core = ["MIT", "Apache-2.0", "BSD-3-Clause", "BSD-2-Clause", "ISC", "GPL-3.0-only", "Unlicense", "CC0-1.0"]
        for spdx_id in core:
            self.assertIn(spdx_id, LICENSE_CATALOG)
            info = LICENSE_CATALOG[spdx_id]
            self.assertEqual(info.spdx_id, spdx_id)
            self.assertTrue(info.url.startswith("https://spdx.org/"))

    def test_case_insensitive_lookup(self):
        mit = get_license_by_id("mit")
        self.assertIsNotNone(mit)
        self.assertEqual(mit.spdx_id, "MIT")

        apache = get_license_by_id("APACHE-2.0")
        self.assertIsNotNone(apache)
        self.assertEqual(apache.spdx_id, "Apache-2.0")

    def test_unknown_id(self):
        self.assertIsNone(get_license_by_id("NON-EXISTENT-LICENSE-123"))


if __name__ == "__main__":
    unittest.main()
