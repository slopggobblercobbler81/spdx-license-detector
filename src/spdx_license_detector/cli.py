# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""Command line interface for spdx-license-detector."""

import argparse
import json
import os
import sys
from typing import List, Optional

from spdx_license_detector import __version__
from spdx_license_detector.catalog import LICENSE_CATALOG, get_license_by_id
from spdx_license_detector.matcher import LicenseMatcher
from spdx_license_detector.scanner import LicenseScanner


class Color:
    """Terminal ANSI colors."""
    _USE = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None

    @classmethod
    def green(cls, t: str) -> str:
        return f"\033[92m{t}\033[0m" if cls._USE else t

    @classmethod
    def red(cls, t: str) -> str:
        return f"\033[91m{t}\033[0m" if cls._USE else t

    @classmethod
    def yellow(cls, t: str) -> str:
        return f"\033[93m{t}\033[0m" if cls._USE else t

    @classmethod
    def blue(cls, t: str) -> str:
        return f"\033[94m{t}\033[0m" if cls._USE else t

    @classmethod
    def bold(cls, t: str) -> str:
        return f"\033[1m{t}\033[0m" if cls._USE else t

    @classmethod
    def dim(cls, t: str) -> str:
        return f"\033[2m{t}\033[0m" if cls._USE else t


def build_parser() -> argparse.ArgumentParser:
    """Build command line argument parser."""
    # Shared arguments parser
    common_p = argparse.ArgumentParser(add_help=False)
    common_p.add_argument("--json", action="store_true", help="Output results in JSON format")
    common_p.add_argument("--no-color", action="store_true", help="Disable colored output")
    common_p.add_argument(
        "--threshold",
        type=float,
        default=0.70,
        help="Confidence threshold between 0.0 and 1.0 (default: 0.70)",
    )

    parser = argparse.ArgumentParser(
        prog="spdx-detect",
        description="Fast offline classifier for open-source LICENSE files against the SPDX catalog.",
        parents=[common_p],
    )
    parser.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Command: detect <file>
    detect_p = subparsers.add_parser("detect", parents=[common_p], help="Identify the license of a single file")
    detect_p.add_argument("file", help="Path to license file or source file")

    # Command: scan <dir>
    scan_p = subparsers.add_parser("scan", parents=[common_p], help="Scan a directory tree for license files")
    scan_p.add_argument("dir", nargs="?", default=".", help="Directory to scan (default: current directory)")
    scan_p.add_argument("--all", action="store_true", help="Scan all text files, not only LICENSE*")

    # Command: list
    subparsers.add_parser("list", parents=[common_p], help="List all canonical SPDX licenses in the catalog")

    # Command: info <id>
    info_p = subparsers.add_parser("info", parents=[common_p], help="Show details and text for a given SPDX ID")
    info_p.add_argument("spdx_id", help="SPDX Identifier (e.g. MIT, Apache-2.0)")

    return parser


def cmd_detect(file_path: str, threshold: float, as_json: bool) -> int:
    """Detect license of a file."""
    if not os.path.isfile(file_path):
        if as_json:
            print(json.dumps({"error": f"File not found: {file_path}"}))
        else:
            print(Color.red(f"Error: File not found: {file_path}"), file=sys.stderr)
        return 2

    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except OSError as e:
        if as_json:
            print(json.dumps({"error": str(e)}))
        else:
            print(Color.red(f"Error reading file: {e}"), file=sys.stderr)
        return 2

    matcher = LicenseMatcher(min_confidence=threshold)
    res = matcher.match(content)

    if as_json:
        payload = {
            "file": file_path,
            "matched": res.matched,
            "spdx_id": res.spdx_id,
            "confidence": res.confidence,
            "method": res.method,
            "license_name": res.license_info.name if res.license_info else None,
            "osi_approved": res.license_info.osi_approved if res.license_info else None,
            "fsf_libre": res.license_info.fsf_libre if res.license_info else None,
            "years": res.detected_years,
            "holder": res.detected_holder,
            "summary": res.summary,
        }
        print(json.dumps(payload, indent=2))
    else:
        print(Color.bold("File: ") + file_path)
        if res.matched:
            pct = f"{round(res.confidence * 100, 1)}%"
            osi = "[+] OSI Approved" if res.license_info.osi_approved else "[-] Non-OSI"
            fsf = "[+] FSF Libre" if res.license_info.fsf_libre else "[-] Non-FSF"
            print(Color.bold("SPDX ID:     ") + Color.green(res.spdx_id))
            print(Color.bold("Name:        ") + res.license_info.name)
            print(Color.bold("Confidence:  ") + Color.green(pct) + f" (via {res.method})")
            print(Color.bold("Status:      ") + f"{osi} | {fsf}")
            if res.detected_years:
                print(Color.bold("Copyright:   ") + f"{', '.join(res.detected_years)} {res.detected_holder or ''}")
        else:
            print(Color.red("Status:      No matching license found"))
            print(Color.dim(res.summary))

    return 0 if res.matched else 1


def cmd_scan(dir_path: str, include_all: bool, threshold: float, as_json: bool) -> int:
    """Scan a directory for licenses."""
    matcher = LicenseMatcher(min_confidence=threshold)
    scanner = LicenseScanner(matcher=matcher)
    res = scanner.scan_directory(dir_path, include_all_text=include_all)

    if as_json:
        payload = {
            "directory": res.directory,
            "files_checked": res.files_checked,
            "primary_license": res.primary_license,
            "confidence": res.confidence,
            "matches": [
                {
                    "file": path,
                    "spdx_id": m.spdx_id,
                    "confidence": m.confidence,
                    "name": m.license_info.name if m.license_info else None,
                    "osi_approved": m.license_info.osi_approved if m.license_info else None,
                }
                for path, m in res.matches
            ],
        }
        print(json.dumps(payload, indent=2))
    else:
        print(Color.bold("Directory: ") + res.directory)
        print(f"Files checked: {res.files_checked}")
        if res.primary_license:
            print(Color.bold("Primary License: ") + Color.green(res.primary_license) + f" ({round(res.confidence * 100, 1)}%)")
        else:
            print(Color.yellow("Primary License: Undetected"))

        if res.matches:
            print("\n" + Color.bold("Detected License Files:"))
            for path, m in res.matches:
                print(f"  {Color.green(m.spdx_id):<16} {round(m.confidence * 100, 1):>5}%  {path}")
        else:
            print(Color.yellow("No license files detected."))

    return 0 if res.primary_license else 1


def cmd_list(as_json: bool) -> int:
    """List catalogued licenses."""
    if as_json:
        items = [
            {
                "spdx_id": info.spdx_id,
                "name": info.name,
                "osi_approved": info.osi_approved,
                "fsf_libre": info.fsf_libre,
                "url": info.url,
            }
            for info in LICENSE_CATALOG.values()
        ]
        print(json.dumps(items, indent=2))
    else:
        print(Color.bold(f"{'SPDX ID':<16} {'OSI':<6} {'FSF':<6} {'Name'}"))
        print("-" * 65)
        for info in LICENSE_CATALOG.values():
            osi = "YES" if info.osi_approved else "NO"
            fsf = "YES" if info.fsf_libre else "NO"
            print(f"{Color.green(info.spdx_id):<16} {osi:<6} {fsf:<6} {info.name}")
    return 0


def cmd_info(spdx_id: str, as_json: bool) -> int:
    """Print details for a specific license."""
    info = get_license_by_id(spdx_id)
    if not info:
        if as_json:
            print(json.dumps({"error": f"Unknown SPDX ID: {spdx_id}"}))
        else:
            print(Color.red(f"Error: Unknown SPDX ID: {spdx_id}"), file=sys.stderr)
        return 1

    if as_json:
        payload = {
            "spdx_id": info.spdx_id,
            "name": info.name,
            "osi_approved": info.osi_approved,
            "fsf_libre": info.fsf_libre,
            "url": info.url,
            "text": info.text,
        }
        print(json.dumps(payload, indent=2))
    else:
        print(Color.bold("SPDX Identifier: ") + Color.green(info.spdx_id))
        print(Color.bold("Name:            ") + info.name)
        print(Color.bold("OSI Approved:    ") + ("Yes" if info.osi_approved else "No"))
        print(Color.bold("FSF Libre:       ") + ("Yes" if info.fsf_libre else "No"))
        print(Color.bold("Canonical URL:   ") + info.url)
        print("\n" + Color.bold("Canonical Text:") + "\n" + Color.dim(info.text))
    return 0


def main(args: Optional[List[str]] = None) -> int:
    """Main CLI entrypoint."""
    parser = build_parser()
    parsed = parser.parse_args(args)

    if parsed.no_color:
        Color._USE = False

    if parsed.command is None:
        parser.print_help()
        return 0

    if parsed.command == "detect":
        return cmd_detect(parsed.file, parsed.threshold, parsed.json)
    elif parsed.command == "scan":
        return cmd_scan(parsed.dir, parsed.all, parsed.threshold, parsed.json)
    elif parsed.command == "list":
        return cmd_list(parsed.json)
    elif parsed.command == "info":
        return cmd_info(parsed.spdx_id, parsed.json)

    return 0


if __name__ == "__main__":
    sys.exit(main())
