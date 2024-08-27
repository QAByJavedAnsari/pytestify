#
import logging

import pytest

@pytest.mark.temp
@pytest.mark.real
def test_get_request(api_client, config):
    endpoint = config['endpoints']['get']
    user_id = config['sample_test']['user_id']

    response = api_client.get(f"{endpoint}/{user_id}")
    logging.info("Response of the GET request: %s", response)
    logging.info("Response code: %d", response.status_code)

    assert response.status_code == 200
    logging.info("Response code 200 is matched")

    json_data = response.json()
    logging.info("Response received from the GET request is: %s", json_data)

    assert json_data['id'] == user_id

@pytest.mark.temp
@pytest.mark.mock
def test_post_request(api_client, config ):
    endpoint = config['endpoints']['post']
    payload = config['sample_test']['payload']['default_post']

    response = api_client.post(endpoint, json=payload)

    assert response is not None, "Received None response from the server"
    logging.info("Response of the POST request: %s", response)
    logging.info("Response code: %d", response.status_code)

    assert response.status_code == 201
    logging.info("Response code 201 is matched")

    json_data = response.json()
    logging.info("Response received from the POST request is: %s", json_data)

    assert json_data['title'] == payload['title']
    assert json_data['body'] == payload['body']
