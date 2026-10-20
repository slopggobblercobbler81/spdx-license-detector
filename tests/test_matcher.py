# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""Tests for license classification and matching engine."""

import unittest
from spdx_license_detector.catalog import LICENSE_CATALOG
from spdx_license_detector.matcher import LicenseMatcher


class TestMatcher(unittest.TestCase):
    def setUp(self):
        self.matcher = LicenseMatcher()

    def test_spdx_tag_match(self):
        text = "// SPDX-License-Identifier: MIT\nconsole.log(42);"
        res = self.matcher.match(text)
        self.assertTrue(res.matched)
        self.assertEqual(res.spdx_id, "MIT")
        self.assertEqual(res.confidence, 1.0)
        self.assertEqual(res.method, "spdx_tag")

    def test_mit_realistic_file(self):
        text = (
            "MIT License\n\n"
            "Copyright (c) 2026 Example Corp.\n\n"
            "Permission is hereby granted, free of charge, to any person obtaining a copy "
            "of this software and associated documentation files (the \"Software\"), to deal "
            "in the Software without restriction, including without limitation the rights "
            "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell "
            "copies of the Software, and to permit persons to whom the Software is "
            "furnished to do so, subject to the following conditions:\n\n"
            "The above copyright notice and this permission notice shall be included in all "
            "copies or substantial portions of the Software.\n\n"
            "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND..."
        )
        res = self.matcher.match(text)
        self.assertTrue(res.matched)
        self.assertEqual(res.spdx_id, "MIT")
        self.assertGreaterEqual(res.confidence, 0.90)
        self.assertIn("2026", res.detected_years)

    def test_apache2_realistic_file(self):
        text = (
            "Copyright 2024 The MegaProject Contributors\n\n"
            "Licensed under the Apache License, Version 2.0 (the \"License\");\n"
            "you may not use this file except in compliance with the License.\n"
            "You may obtain a copy of the License at\n\n"
            "    http://www.apache.org/licenses/LICENSE-2.0\n\n"
            "Unless required by applicable law or agreed to in writing, software "
            "distributed under the License is distributed on an \"AS IS\" BASIS, "
            "WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND..."
        )
        res = self.matcher.match(text)
        self.assertTrue(res.matched)
        self.assertEqual(res.spdx_id, "Apache-2.0")
        self.assertGreaterEqual(res.confidence, 0.85)

    def test_bsd_3_clause(self):
        text = LICENSE_CATALOG["BSD-3-Clause"].text
        res = self.matcher.match(text)
        self.assertTrue(res.matched)
        self.assertEqual(res.spdx_id, "BSD-3-Clause")
        self.assertGreaterEqual(res.confidence, 0.95)

    def test_isc_license(self):
        text = LICENSE_CATALOG["ISC"].text
        res = self.matcher.match(text)
        self.assertTrue(res.matched)
        self.assertEqual(res.spdx_id, "ISC")
        self.assertGreaterEqual(res.confidence, 0.95)

    def test_unlicense(self):
        text = LICENSE_CATALOG["Unlicense"].text
        res = self.matcher.match(text)
        self.assertTrue(res.matched)
        self.assertEqual(res.spdx_id, "Unlicense")

    def test_empty_and_garbage(self):
        empty_res = self.matcher.match("")
        self.assertFalse(empty_res.matched)

        garbage = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio."
        garbage_res = self.matcher.match(garbage)
        self.assertFalse(garbage_res.matched)


if __name__ == "__main__":
    unittest.main()
