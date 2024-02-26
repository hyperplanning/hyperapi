import pytest
import responses
from hyperapi.client import HyperClient


@pytest.fixture
def hyper_client():
    return HyperClient('https://api.example.com')


@responses.activate
def login_success_test(hyper_client):
    responses.add(responses.POST, 'https://api.example.com/login',
                  json={"token": "abc123"}, status=200)

    assert hyper_client.login('user', 'pass') is True
    assert 'Authorization' in hyper_client.session.headers
    assert hyper_client.session.headers['Authorization'] == 'Bearer abc123'


@responses.activate
def login_failure_test(hyper_client):
    responses.add(responses.POST, 'https://api.example.com/login',
                  json={"error": "Invalid credentials"}, status=401)

    assert hyper_client.login('user', 'wrongpass') is False
