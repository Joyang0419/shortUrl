import pytest
from _pytest.fixtures import SubRequest

from src.implements.services import TOKEN_SERVICE
from src.services.token.models import JWTPayload


class TestJWTService:
    @pytest.fixture(
        scope='function',
        autouse=True,
        params=[
            pytest.param(
                {
                    "user_id": 55,
                },
                id="Successful Case"
            )
        ]
    )
    def setup(self, request: SubRequest):
        payload_dict = request.param
        self.access_token = TOKEN_SERVICE.create_access_token(**payload_dict)

    def test_decode_token(self):
        decode_token = TOKEN_SERVICE.decode_access_token(
            token=self.access_token.access_token
        )
        assert isinstance(decode_token, JWTPayload)
