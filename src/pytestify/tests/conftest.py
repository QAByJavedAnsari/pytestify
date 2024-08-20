# src/pytestify/tests/conftest.py
import pytest
from pytestify.utils.check_docker import check_docker

@pytest.fixture(scope='session', autouse=True)
def docker_check():
    if not check_docker():
        pytest.exit("Docker is required to run these tests. Please start Docker and try again.")
