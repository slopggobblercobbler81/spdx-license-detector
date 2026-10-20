# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""Tests for command-line interface."""

import io
import json
import os
import sys
import tempfile
import unittest
from spdx_license_detector.catalog import LICENSE_CATALOG
from spdx_license_detector.cli import main


class TestCLI(unittest.TestCase):
    def test_cli_detect_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "LICENSE")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(LICENSE_CATALOG["MIT"].text)

            code = main(["detect", file_path, "--no-color"])
            self.assertEqual(code, 0)

    def test_cli_detect_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "LICENSE")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(LICENSE_CATALOG["Apache-2.0"].text)

            old_stdout = sys.stdout
            sys.stdout = io.StringIO()
            try:
                code = main(["detect", file_path, "--json"])
                out = sys.stdout.getvalue()
            finally:
                sys.stdout = old_stdout

            self.assertEqual(code, 0)
            data = json.loads(out)
            self.assertTrue(data["matched"])
            self.assertEqual(data["spdx_id"], "Apache-2.0")

    def test_cli_list_command(self):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            code = main(["list", "--json"])
            out = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout

        self.assertEqual(code, 0)
        licenses = json.loads(out)
        self.assertTrue(any(l["spdx_id"] == "MIT" for l in licenses))

    def test_cli_info_command(self):
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            code = main(["info", "MIT", "--json"])
            out = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout

        self.assertEqual(code, 0)
        info = json.loads(out)
        self.assertEqual(info["spdx_id"], "MIT")
        self.assertTrue(info["osi_approved"])

    def test_cli_missing_file_returns_error(self):
        code = main(["detect", "non_existent_file_path_xyz.txt"])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
