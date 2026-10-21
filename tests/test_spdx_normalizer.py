from spdx_license_detector.normalizer import normalize_spdx_id

def test_normalize_spdx_id():
    assert normalize_spdx_id("mit") == "MIT"
    assert normalize_spdx_id(" apache-2.0 ") == "APACHE-2.0"
