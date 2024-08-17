# src/pytestify/tests/test_sample.py
import pytest
from pytestify.utils.utils import log_info, format_url


def test_format_url():
    base_url = "http://example.com/"
    endpoint = "api/test"
    expected_url = "http://example.com/api/test"

    # Use the format_url function
    result_url = format_url(base_url, endpoint)

    # Log the result (optional)
    log_info(f"Formatted URL: {result_url}")

    # Assert the URL is as expected
    assert result_url == expected_url

    if result_url == expected_url:
        print("Result URL is matched")
