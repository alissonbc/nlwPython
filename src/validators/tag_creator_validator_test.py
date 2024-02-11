# import pytest
from src.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)

from .tag_creator_validator import tag_creator_validator


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


# @pytest.mark.test
def test_tag_creator_validator():
    req = MockRequest(json={"product_code": "12345"})
    tag_creator_validator(req)
    # response = tag_creator_validator(req)
    # assert response == 3


def test_tag_creator_validator_with_erros():
    req = MockRequest(json={"product_code": 12345})
    try:
        tag_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
