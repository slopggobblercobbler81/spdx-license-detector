# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""Tests for repository license directory scanner."""

import os
import tempfile
import unittest
from spdx_license_detector.catalog import LICENSE_CATALOG
from spdx_license_detector.scanner import LicenseScanner


class TestScanner(unittest.TestCase):
    def test_scan_finds_root_license(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            lic_path = os.path.join(tmpdir, "LICENSE")
            with open(lic_path, "w", encoding="utf-8") as f:
                f.write(LICENSE_CATALOG["MIT"].text)

            scanner = LicenseScanner()
            res = scanner.scan_directory(tmpdir)
            self.assertEqual(res.primary_license, "MIT")
            self.assertEqual(len(res.matches), 1)
            self.assertEqual(res.matches[0][0], lic_path)

    def test_scan_ignores_vendor_and_node_modules(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            nm = os.path.join(tmpdir, "node_modules", "some-dep")
            os.makedirs(nm, exist_ok=True)
            with open(os.path.join(nm, "LICENSE"), "w", encoding="utf-8") as f:
                f.write(LICENSE_CATALOG["Apache-2.0"].text)

            scanner = LicenseScanner()
            res = scanner.scan_directory(tmpdir)
            # node_modules should be ignored
            self.assertIsNone(res.primary_license)
            self.assertEqual(len(res.matches), 0)


if __name__ == "__main__":
    unittest.main()
