# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""Tests for text normalization and token extraction."""

import unittest
from spdx_license_detector.normalizer import LicenseNormalizer


class TestNormalizer(unittest.TestCase):
    def test_strip_copyright(self):
        text = "Copyright (c) 2026 Acme Corp.\nAll rights reserved.\nPermission is hereby granted..."
        cleaned = LicenseNormalizer.strip_copyright(text)
        self.assertNotIn("Acme Corp", cleaned)
        self.assertIn("Permission is hereby granted", cleaned)

    def test_normalize_punctuation_and_whitespace(self):
        raw = "Permission  is “hereby”\tgranted, free   of charge—to any person!"
        norm = LicenseNormalizer.normalize_text(raw, strip_copyright=False)
        self.assertEqual(norm, "permission is hereby granted free of charge to any person")

    def test_extract_years_and_holder(self):
        text = "Copyright (c) 2021-2026 Jane Doe\nAll rights reserved."
        years, holder = LicenseNormalizer.extract_metadata(text)
        self.assertIn("2021-2026", years)
        self.assertIn("Jane Doe", holder)

    def test_ngrams(self):
        tokens = ["permission", "is", "hereby", "granted"]
        bigrams = LicenseNormalizer.get_ngrams(tokens, n=2)
        self.assertEqual(len(bigrams), 3)
        self.assertIn(("permission", "is"), bigrams)
        self.assertIn(("is", "hereby"), bigrams)


if __name__ == "__main__":
    unittest.main()
