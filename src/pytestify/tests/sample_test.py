# src/pytestify/tests/test_sample.py
import pytest
import requests
import logging

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

@pytest.mark.test
def test_sample_response():
    url = "http://localhost:8080/api/test"
    response = requests.get(url)
    logging.info(f"Response Status Code: {response.status_code}")
    logging.info(f"Response Body: {response.text}")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a sample response from wiremock"}

@pytest.mark.xfail
def test_not_found_response():
    response = requests.get("http://localhost:8080/api/unknown")
    assert response.status_code == 200 #404