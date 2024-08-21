import logging
from pytestify.data.data_loader import load_config


def test_get_request(api_client):
    config = load_config()
    endpoint = config['endpoints']['posts']
    user_id = config['user_id']

    response = api_client.get(f"{endpoint}/{user_id}")
    logging.info("Response of the GET request: %s", response)
    logging.info("Response code: %d", response.status_code)

    assert response.status_code == 200
    logging.info("Response code 200 is matched")

    json_data = response.json()
    logging.info("Response received from the GET request is: %s", json_data)

    assert json_data['id'] == user_id


def test_post_request(api_client, ):
    config = load_config()

    endpoint = config['endpoints']['posts']
    default_post = config['default_post']

    response = api_client.post(endpoint, json=default_post)
    logging.info("Response of the POST request: %s", response)
    logging.info("Response code: %d", response.status_code)

    assert response.status_code == 201
    logging.info("Response code 201 is matched")

    json_data = response.json()
    logging.info("Response received from the POST request is: %s", json_data)

    assert json_data['title'] == default_post['title']
    assert json_data['body'] == default_post['body']