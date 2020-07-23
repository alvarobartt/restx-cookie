# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

import pytest

from {{ cookiecutter.package_name }}.server import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_api(client):
    response = client.get('/v1/')
    assert response._status_code == 200
