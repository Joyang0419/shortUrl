"""user router"""

from fastapi import APIRouter, status, HTTPException, Response, Request, Depends
from fastapi.security import OAuth2PasswordRequestForm
from loguru import logger

from src.implements.services import ENCRYPT_SERVICE, TOKEN_SERVICE, USER_SERVICE
from src.routers.user.api_models.request import RegisterForm
from src.routers.user.api_models.response import TransactionResponse, \
    GetUserResponse, VerifyTokenResponse, LoginResponse, SignUpResponse
from src.services.token.exceptions import DecodeException
from src.services.user.exceptions import CreateUserException

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    path="/sign-up",
    response_model=SignUpResponse,
    responses=SignUpResponse.examples(),
    status_code=status.HTTP_201_CREATED
)
async def signup_user(
        register_form: RegisterForm,
        response: Response,
        request: Request
) -> SignUpResponse:
    hashed_password = ENCRYPT_SERVICE.get_hashed_password(
        plain_password=register_form.password
    )

    try:
        user_id = await USER_SERVICE.create_user(
            account=register_form.account,
            password=hashed_password,
        )

    except CreateUserException as e:
        transaction_response = TransactionResponse(is_success=False)

        return SignUpResponse(
            data=transaction_response,
            error_message=e.message
        )

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    transaction_response = TransactionResponse(is_success=True)

    response.headers["location"] = request.url_for(
        name='get_user',
        user_id=user_id
    )

    return SignUpResponse(data=transaction_response)


@router.get(
    path="/user/{user_id}",
    response_model=GetUserResponse,
    responses=GetUserResponse.examples(),
    status_code=status.HTTP_200_OK
)
async def get_user(
        user_id: int,
) -> GetUserResponse:
    user = await USER_SERVICE.get_user_by_id(user_id=user_id)

    if not user:
        return GetUserResponse(data=None)

    return GetUserResponse(data=user)


@router.get(
    path="/verify-token/{token}",
    response_model=VerifyTokenResponse,
    responses=VerifyTokenResponse.examples()
)
async def verify_token(token: str) -> VerifyTokenResponse:
    try:
        payload = TOKEN_SERVICE.decode_access_token(token=token)

    except DecodeException as e:
        return VerifyTokenResponse(error_message=e.message)

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return VerifyTokenResponse(data=payload)


@router.post(
    path="/login",
    response_model=LoginResponse,
    responses=LoginResponse.examples()
)
async def login_account(
        request: Request,
        response: Response,
        login_form: OAuth2PasswordRequestForm = Depends()
) -> LoginResponse:
    user_entity = await USER_SERVICE.get_user_by_account(
        account=login_form.username,
    )

    if not user_entity:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Not found user.'
        )

    is_correct_password = ENCRYPT_SERVICE.verify_password(
        plain_password=login_form.password,
        hashed_password=user_entity.hashed_password
    )

    if not is_correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Wrong password.'
        )

    access_token = TOKEN_SERVICE.create_access_token(
        user_id=user_entity.id,
    )

    token = access_token.token_type + ' ' + access_token.access_token

    response.headers["Authorization"] = token

    response.headers["location"] = request.url_for(
        name='verify_token',
        token=access_token.access_token
    )

    return access_token
