from src.implements.services import ENCRYPT_SERVICE


def test_encrypt_password():
    pwd = 'password'
    pwd1 = ENCRYPT_SERVICE.get_hashed_password(plain_password=pwd)
    pwd2 = ENCRYPT_SERVICE.get_hashed_password(plain_password=pwd)

    assert pwd1 != pwd2
    assert ENCRYPT_SERVICE.verify_password(
        plain_password=pwd,
        hashed_password=pwd1
    )
    assert ENCRYPT_SERVICE.verify_password(
        plain_password=pwd,
        hashed_password=pwd2
    )
