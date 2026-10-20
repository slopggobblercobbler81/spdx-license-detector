# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""Entrypoint when executed with `python -m spdx_license_detector`."""

import sys
from spdx_license_detector.cli import main

if __name__ == "__main__":
    sys.exit(main())
