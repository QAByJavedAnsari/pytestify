# src/pytestify/tests/test_sample.py
import pytest
import requests

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

def test_sample_response():
    url = "http://localhost:8080/api/test"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"message": "This is a sample response from wiremock"}

@pytest.mark.xfail
def test_not_found_response():
    response = requests.get("http://localhost:8080/api/unknown")
    assert response.status_code == 200 #404


# Sample UPI Tests with mocking
def test_upi_payment_success():
    url = "http://localhost:8080/upi/payment/status"
    payload = {"transactionId": "1234567890"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json() == {
        "status": "SUCCESS",
        "transactionId": "1234567890",
        "amount": "100.00",
        "currency": "INR",
        "message": "Payment successful",
        "upiId": "user@upi"
    }

    def test_upi_payment_failure():
        url = "http://localhost:8080/upi/payment/status"
        payload = {"transactionId": "1234567891"}
        response = requests.post(url, json=payload)
        assert response.status_code == 200
        assert response.json() == {
            "status": "FAILURE",
            "transactionId": "1234567891",
            "amount": "100.00",
            "currency": "INR",
            "message": "Payment failed",
            "errorCode": "INSUFFICIENT_FUNDS"
        }

def test_upi_payment_pending():
    url = "http://localhost:8080/upi/payment/status"
    payload = {"transactionId": "1234567892"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json() == {
        "status": "PENDING",
        "transactionId": "1234567892",
        "amount": "100.00",
        "currency": "INR",
        "message": "Payment is pending",
        "upiId": "user@upi"
    }
