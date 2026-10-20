# spdx-license-detector 🔍

[![CI](https://github.com/slopggobblercobbler81/spdx-license-detector/actions/workflows/ci.yml/badge.svg)](https://github.com/slopggobblercobbler81/spdx-license-detector/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> **An ultra-fast, zero-dependency offline CLI tool and Python library that accurately classifies open-source LICENSE files against the canonical SPDX catalog using multi-tier normalized text matching and confidence scoring.**

---

## 🌟 Key Features

- ⚡ **100% Offline & Zero Dependencies**: Operates instantaneously with zero external network requests or third-party packages.
- 🎯 **Multi-Tier Matching Engine**:
  1. **SPDX-License-Identifier Tag Parsing**: Instant 100% confidence tag resolution.
  2. **Exact Normalized Text Match**: 100% confidence match after whitespace, quote, and boilerplate normalization.
  3. **Distinctive Phrase Signatures**: Identifies unique legal phrasing across variants.
  4. **N-Gram Similarity Scoring**: Calculates Sørensen–Dice and token containment coefficients for modified texts.
- 🗃️ **Comprehensive SPDX Catalog**:
  - MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, GPL-2.0-only, GPL-3.0-only, AGPL-3.0-only, LGPL-2.1-only, LGPL-3.0-only, MPL-2.0, Unlicense, CC0-1.0, 0BSD, BSL-1.0, and more.
- 🏷️ **Metadata Extraction**:
  - Automatically extracts copyright years (e.g. `2021-2026`) and copyright holder entities.
  - Flags OSI-Approved and FSF-Free/Libre licenses.
- 📁 **Repository Scanner**: Recursively discovers and audits license files across projects, identifying the primary project license.
- 🤖 **CI/CD & SBOM Integration**: Supports `--json` machine-readable output for integration into compliance pipelines and CycloneDX/SPDX generation.

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/slopggobblercobbler81/spdx-license-detector.git
cd spdx-license-detector
pip install .
```

Or run directly without installation:

```bash
python -m spdx_license_detector --help
```

---

## 💻 CLI Usage

### 1. Identify a License File (`detect`)

Classify a single `LICENSE` or source file:

```bash
spdx-detect detect LICENSE
```

Output:
```text
File: LICENSE
SPDX ID:     MIT
Name:        MIT License
Confidence:  95.0% (via distinctive_phrases)
Status:      [+] OSI Approved | [+] FSF Libre
Copyright:   2026 slopggobblercobbler81
```

Get JSON output:
```bash
spdx-detect detect LICENSE --json
```

```json
{
  "file": "LICENSE",
  "matched": true,
  "spdx_id": "MIT",
  "confidence": 0.95,
  "method": "distinctive_phrases",
  "license_name": "MIT License",
  "osi_approved": true,
  "fsf_libre": true,
  "years": [
    "2026"
  ],
  "holder": "slopggobblercobbler81",
  "summary": "Distinctive signature matched for MIT"
}
```

### 2. Scan an Entire Directory (`scan`)

Audit a project folder for all license files:

```bash
spdx-detect scan .
```

Output:
```text
Directory: /path/to/project
Files checked: 3
Primary License: MIT (100.0%)

Detected License Files:
  MIT               95.0%  ./LICENSE
  Apache-2.0       100.0%  ./vendor/lib/LICENSE
```

### 3. List Known Licenses (`list`)

View all licenses supported by the offline database:

```bash
spdx-detect list
```

### 4. Inspect Canonical License Info (`info`)

```bash
spdx-detect info Apache-2.0
```

---

## 🐍 Python API Usage

Use `spdx-license-detector` as a library inside your Python applications:

```python
from spdx_license_detector import LicenseMatcher, LicenseScanner

# Classify string content
matcher = LicenseMatcher(min_confidence=0.75)
result = matcher.match("""
Permission is hereby granted, free of charge, to any person obtaining a copy...
""")

if result.matched:
    print(f"Detected: {result.spdx_id} ({result.confidence * 100:.1f}%)")
    print(f"OSI Approved: {result.license_info.osi_approved}")

# Scan a directory
scanner = LicenseScanner(matcher=matcher)
scan_result = scanner.scan_directory("/path/to/repo")
print(f"Primary license: {scan_result.primary_license}")
```

---

## 🧪 Running Tests

Run the full test suite with standard `unittest`:

```bash
python -m unittest discover -s tests -v
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
Copyright (c) 2026 slopggobblercobbler81.
