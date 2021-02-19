import pytest
from django.test.client import Client
from pytest_factoryboy import register

from project.factories import PlaceFactory

register(PlaceFactory)


@pytest.fixture
def client(db):
    client = Client()
    client.login(user='user', password='password')
    return client
