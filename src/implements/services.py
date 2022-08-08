"""services implements"""

from src.implements.repos import USER_REPO, SHORT_URL_REPO
from src.services import UserService, CreateUserException, \
    CryptContextEncryptService, JsonWebTokenService, ShortUrlService
from passlib.context import CryptContext
from src.configs.app_config import PRIVATE_KEY, PUBLIC_KEY, JWT_ALGORITHM


USER_SERVICE = UserService(
    user_repo=USER_REPO,
)

ENCRYPT_SERVICE = CryptContextEncryptService(
    crypt_context=CryptContext(
        schemes=['bcrypt'],
        deprecated='auto'
    )
)

TOKEN_SERVICE = JsonWebTokenService(
    private_key=PRIVATE_KEY,
    public_key=PUBLIC_KEY,
    algorithm=JWT_ALGORITHM
)

SHORT_URL_SERVICE = ShortUrlService(
    short_url_repo=SHORT_URL_REPO
)
