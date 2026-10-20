# Copyright (c) 2026 slopggobblercobbler81
# SPDX-License-Identifier: MIT

"""SPDX license catalog and metadata."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class LicenseInfo:
    """SPDX license information and canonical text."""
    spdx_id: str
    name: str
    osi_approved: bool
    fsf_libre: bool
    url: str
    text: str
    distinctive_phrases: List[str] = field(default_factory=list)


# Canonical license texts and metadata
LICENSE_CATALOG: Dict[str, LicenseInfo] = {
    "MIT": LicenseInfo(
        spdx_id="MIT",
        name="MIT License",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/MIT.html",
        text=(
            "Permission is hereby granted, free of charge, to any person obtaining a copy "
            "of this software and associated documentation files (the \"Software\"), to deal "
            "in the Software without restriction, including without limitation the rights "
            "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell "
            "copies of the Software, and to permit persons to whom the Software is "
            "furnished to do so, subject to the following conditions:\n\n"
            "The above copyright notice and this permission notice shall be included in all "
            "copies or substantial portions of the Software.\n\n"
            "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR "
            "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, "
            "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE "
            "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER "
            "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, "
            "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE "
            "SOFTWARE."
        ),
        distinctive_phrases=[
            "permission is hereby granted, free of charge, to any person obtaining a copy of this software",
            "including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense",
            "the above copyright notice and this permission notice shall be included in all copies",
        ],
    ),
    "Apache-2.0": LicenseInfo(
        spdx_id="Apache-2.0",
        name="Apache License 2.0",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/Apache-2.0.html",
        text=(
            "Apache License\n"
            "Version 2.0, January 2004\n"
            "http://www.apache.org/licenses/\n\n"
            "TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n"
            "1. Definitions.\n"
            "\"License\" shall mean the terms and conditions for use, reproduction, and distribution "
            "as defined by Sections 1 through 9 of this document.\n"
            "\"Licensor\" shall mean the copyright owner or entity authorized by the copyright owner "
            "that is granting the License.\n"
            "\"Legal Entity\" shall mean the union of the acting entity and all other entities that control, "
            "are controlled by, or are under common control with that entity.\n"
            "\"You\" (or \"Your\") shall mean an individual or Legal Entity exercising permissions granted by this License.\n"
            "\"Source\" form shall mean the preferred form for making modifications...\n"
            "2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You...\n"
            "3. Grant of Patent License...\n"
            "4. Redistribution...\n"
            "5. Submission of Contributions...\n"
            "6. Trademarks...\n"
            "7. Disclaimer of Warranty...\n"
            "8. Limitation of Liability...\n"
            "9. Accepting Warranty or Additional Liability..."
        ),
        distinctive_phrases=[
            "apache license version 2.0",
            "terms and conditions for use, reproduction, and distribution",
            "licensed under the apache license, version 2.0",
            "grant of copyright license. subject to the terms and conditions of this license",
            "grant of patent license",
        ],
    ),
    "BSD-3-Clause": LicenseInfo(
        spdx_id="BSD-3-Clause",
        name="BSD 3-Clause \"New\" or \"Revised\" License",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/BSD-3-Clause.html",
        text=(
            "Redistribution and use in source and binary forms, with or without modification, "
            "are permitted provided that the following conditions are met:\n\n"
            "1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.\n\n"
            "2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.\n\n"
            "3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.\n\n"
            "THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, "
            "INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. "
            "IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR "
            "CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; "
            "OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT "
            "(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
        ),
        distinctive_phrases=[
            "redistribution and use in source and binary forms, with or without modification",
            "redistributions of source code must retain the above copyright notice",
            "neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products",
        ],
    ),
    "BSD-2-Clause": LicenseInfo(
        spdx_id="BSD-2-Clause",
        name="BSD 2-Clause \"Simplified\" License",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/BSD-2-Clause.html",
        text=(
            "Redistribution and use in source and binary forms, with or without modification, "
            "are permitted provided that the following conditions are met:\n\n"
            "1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.\n\n"
            "2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.\n\n"
            "THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\" AND ANY EXPRESS OR IMPLIED WARRANTIES, "
            "INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. "
            "IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR "
            "CONSEQUENTIAL DAMAGES."
        ),
        distinctive_phrases=[
            "redistribution and use in source and binary forms, with or without modification",
            "redistributions in binary form must reproduce the above copyright notice",
            "this software is provided by the copyright holders and contributors as is",
        ],
    ),
    "ISC": LicenseInfo(
        spdx_id="ISC",
        name="ISC License",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/ISC.html",
        text=(
            "Permission to use, copy, modify, and/or distribute this software for any purpose "
            "with or without fee is hereby granted, provided that the above copyright notice "
            "and this permission notice appear in all copies.\n\n"
            "THE SOFTWARE IS PROVIDED \"AS IS\" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH "
            "REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND "
            "FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, "
            "INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS "
            "OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER "
            "TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF "
            "THIS SOFTWARE."
        ),
        distinctive_phrases=[
            "permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted",
            "and the author disclaims all warranties with regard to this software including all implied warranties",
        ],
    ),
    "GPL-3.0-only": LicenseInfo(
        spdx_id="GPL-3.0-only",
        name="GNU General Public License v3.0 only",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/GPL-3.0-only.html",
        text=(
            "GNU GENERAL PUBLIC LICENSE\n"
            "Version 3, 29 June 2007\n\n"
            "Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>\n"
            "Everyone is permitted to copy and distribute verbatim copies "
            "of this license document, but changing it is not allowed.\n\n"
            "Preamble\n"
            "The GNU General Public License is a free, copyleft license for software and other kinds of works...\n"
            "TERMS AND CONDITIONS\n"
            "0. Definitions.\n"
            "\"This License\" refers to version 3 of the GNU General Public License."
        ),
        distinctive_phrases=[
            "gnu general public license version 3",
            "free, copyleft license for software and other kinds of works",
            "this license refers to version 3 of the gnu general public license",
        ],
    ),
    "GPL-2.0-only": LicenseInfo(
        spdx_id="GPL-2.0-only",
        name="GNU General Public License v2.0 only",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/GPL-2.0-only.html",
        text=(
            "GNU GENERAL PUBLIC LICENSE\n"
            "Version 2, June 1991\n\n"
            "Copyright (C) 1989, 1991 Free Software Foundation, Inc.\n"
            "51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA\n"
            "Everyone is permitted to copy and distribute verbatim copies of this license document...\n"
            "TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION"
        ),
        distinctive_phrases=[
            "gnu general public license version 2",
            "terms and conditions for copying, distribution and modification",
            "51 franklin street, fifth floor, boston, ma",
        ],
    ),
    "AGPL-3.0-only": LicenseInfo(
        spdx_id="AGPL-3.0-only",
        name="GNU Affero General Public License v3.0 only",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/AGPL-3.0-only.html",
        text=(
            "GNU AFFERO GENERAL PUBLIC LICENSE\n"
            "Version 3, 19 November 2007\n\n"
            "Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>\n"
            "Everyone is permitted to copy and distribute verbatim copies of this license document...\n"
            "remote network interaction; in the case of GNU Affero GPL..."
        ),
        distinctive_phrases=[
            "gnu affero general public license",
            "remote network interaction",
            "gnu affero gpl",
        ],
    ),
    "MPL-2.0": LicenseInfo(
        spdx_id="MPL-2.0",
        name="Mozilla Public License 2.0",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/MPL-2.0.html",
        text=(
            "Mozilla Public License Version 2.0\n"
            "==================================\n\n"
            "1. Definitions\n"
            "1.1. \"Contributor\"\n"
            "means each individual or legal entity that creates, contributes to the creation of, "
            "or owns Covered Software.\n\n"
            "1.2. \"Contributor Version\"\n"
            "means the combination of the Contributions of others (if any) used by a Contributor..."
        ),
        distinctive_phrases=[
            "mozilla public license version 2.0",
            "covered software",
            "contributor version",
            "incompatible with secondary licenses",
        ],
    ),
    "Unlicense": LicenseInfo(
        spdx_id="Unlicense",
        name="The Unlicense",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/Unlicense.html",
        text=(
            "This is free and unencumbered software released into the public domain.\n\n"
            "Anyone is free to copy, modify, publish, use, compile, sell, or "
            "distribute this software, either in source code form or as a compiled "
            "binary, for any purpose, commercial or non-commercial, and by any "
            "means.\n\n"
            "In jurisdictions that recognize copyright laws, the author or authors "
            "of this software dedicate any and all copyright interest in the "
            "software to the public domain. We make this dedication for the benefit "
            "of the public at large and to the detriment of our heirs and "
            "successors. We intend this dedication to be an overt act of "
            "relinquishment in perpetuity of all present and future rights to this "
            "software under copyright law.\n\n"
            "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND..."
        ),
        distinctive_phrases=[
            "this is free and unencumbered software released into the public domain",
            "anyone is free to copy, modify, publish, use, compile, sell, or distribute this software",
            "dedicate any and all copyright interest in the software to the public domain",
        ],
    ),
    "CC0-1.0": LicenseInfo(
        spdx_id="CC0-1.0",
        name="Creative Commons Zero v1.0 Universal",
        osi_approved=False,
        fsf_libre=True,
        url="https://spdx.org/licenses/CC0-1.0.html",
        text=(
            "Creative Commons Legal Code\n\n"
            "CC0 1.0 Universal\n\n"
            "CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE LEGAL SERVICES.\n\n"
            "Statement of Purpose\n"
            "The person who associated a work with this deed has dedicated the work to the public domain by waiving all of his or her rights to the work worldwide under copyright law..."
        ),
        distinctive_phrases=[
            "cc0 1.0 universal",
            "creative commons legal code",
            "has dedicated the work to the public domain by waiving all of his or her rights",
        ],
    ),
    "0BSD": LicenseInfo(
        spdx_id="0BSD",
        name="BSD Zero Clause License",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/0BSD.html",
        text=(
            "Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted.\n\n"
            "THE SOFTWARE IS PROVIDED \"AS IS\" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE."
        ),
        distinctive_phrases=[
            "permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted",
            "bsd zero clause",
        ],
    ),
    "BSL-1.0": LicenseInfo(
        spdx_id="BSL-1.0",
        name="Boost Software License 1.0",
        osi_approved=True,
        fsf_libre=True,
        url="https://spdx.org/licenses/BSL-1.0.html",
        text=(
            "Boost Software License - Version 1.0 - August 17th, 2003\n\n"
            "Permission is hereby granted, free of charge, to any person or organization "
            "obtaining a copy of the software and accompanying documentation covered by "
            "this license (the \"Software\") to use, reproduce, display, distribute, "
            "execute, and transmit the Software, and to prepare derivative works of the "
            "Software, and to permit third-parties to whom the Software is furnished to "
            "do so, all subject to the following:\n\n"
            "The copyright notices in the Software and this entire statement, including "
            "the above license grant, this restriction and the following disclaimer, "
            "must be included in all copies of the Software, in whole or in part..."
        ),
        distinctive_phrases=[
            "boost software license - version 1.0",
            "person or organization obtaining a copy of the software and accompanying documentation covered by this license",
        ],
    ),
}


def get_license_by_id(spdx_id: str) -> Optional[LicenseInfo]:
    """Retrieve license info by SPDX identifier (case-insensitive)."""
    norm = spdx_id.strip().upper()
    for k, v in LICENSE_CATALOG.items():
        if k.upper() == norm:
            return v
    return None
