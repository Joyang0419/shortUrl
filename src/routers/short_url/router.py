"""short_url router"""
import secrets
from typing import Optional

from fastapi import APIRouter, status, Depends, Response, Request, Query
from fastapi.exceptions import HTTPException
from fastapi.responses import RedirectResponse

from src.implements.services import SHORT_URL_SERVICE, TOKEN_SERVICE
from src.routers.short_url.api_models.request import CreateShortUrlForm, \
    ModifyTargetUrlForm
from src.routers.short_url.api_models.response import \
    GetUserShortUrlsResponse, TransactionResponse, CreateShortUrlResponse, \
    ModifyUserShortUrlResponse, DeleteUserShortUrlResponse
from src.security import oauth2_scheme
from src.services.token.exceptions import DecodeException

router = APIRouter(prefix="/short_urls", tags=["short_url"])


@router.get(
    path="/",
    response_model=GetUserShortUrlsResponse,
    responses=GetUserShortUrlsResponse.examples(),
    status_code=status.HTTP_200_OK
)
async def get_user_short_urls(
        token: str = Depends(oauth2_scheme)
) -> GetUserShortUrlsResponse:
    try:
        payload = TOKEN_SERVICE.decode_access_token(token=token)

    except DecodeException as e:
        return GetUserShortUrlsResponse(
            data=None,
            error_message=e.message
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

    user_id = payload.sub.user_id

    user_short_urls = await SHORT_URL_SERVICE.get_short_urls(user_id=user_id)

    return GetUserShortUrlsResponse(
        data=user_short_urls
    )


@router.get(
    path="/{secret_key}",
    status_code=status.HTTP_303_SEE_OTHER
)
async def get_short_url(
        request: Request,
        secret_key: str
) -> Optional[RedirectResponse]:
    _ = secret_key
    short_url = request.url
    short_url_entity = await SHORT_URL_SERVICE.get_short_url(
        short_url=short_url
    )
    if not short_url_entity:
        return

    return RedirectResponse(
        url=short_url_entity.target_url,
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.post(
    path="/",
    response_model=CreateShortUrlResponse,
    responses=CreateShortUrlResponse.examples(),
    status_code=status.HTTP_201_CREATED
)
async def create_user_short_url(
        request: Request,
        response: Response,
        short_url_form: CreateShortUrlForm,
        token: str = Depends(oauth2_scheme)
) -> CreateShortUrlResponse:
    try:
        payload = TOKEN_SERVICE.decode_access_token(token=token)

    except DecodeException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.message

        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

    user_id = payload.sub.user_id

    short_url_id = await SHORT_URL_SERVICE.create_short_url(
        user_id=user_id,
        target_url=short_url_form.target_url,
        short_url=""
    )

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))

    short_url = request.url_for(
        name='get_short_url',
        secret_key=secret_key + str(short_url_id)
    )
    await SHORT_URL_SERVICE.update_short_url(
        short_url_id=short_url_id,
        modified_short_url=short_url
    )

    response.headers["location"] = short_url

    return CreateShortUrlResponse(
        data=TransactionResponse(
            is_success=True
        )
    )


@router.patch(
    path="/{secret_key}",
    response_model=ModifyUserShortUrlResponse,
    responses=ModifyUserShortUrlResponse.examples(),
    status_code=status.HTTP_200_OK
)
async def modify_user_short_url(
        request: Request,
        modify_target_url_form: ModifyTargetUrlForm,
        secret_key: str = Query(...),
        token: str = Depends(oauth2_scheme)
):
    try:
        payload = TOKEN_SERVICE.decode_access_token(token=token)

    except DecodeException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.message

        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

    user_id = payload.sub.user_id

    short_url = request.url_for(
        name='get_short_url',
        secret_key=secret_key
    )

    modified_status = await SHORT_URL_SERVICE.update_target_url(
        user_id=user_id,
        short_url=short_url,
        modified_target_url=modify_target_url_form.target_url
    )

    if not modified_status:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return ModifyUserShortUrlResponse(
        data=TransactionResponse(is_success=True)
    )


@router.delete(
    path="/{secret_key}",
    response_model=DeleteUserShortUrlResponse,
    responses=DeleteUserShortUrlResponse.examples(),
    status_code=status.HTTP_200_OK
)
async def delete_user_short_url(
        request: Request,
        token: str = Depends(oauth2_scheme),
        secret_key: str = Query(...),
) -> DeleteUserShortUrlResponse:
    try:
        payload = TOKEN_SERVICE.decode_access_token(token=token)

    except DecodeException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.message

        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e
        )

    user_id = payload.sub.user_id

    short_url = request.url_for(
        name='get_short_url',
        secret_key=secret_key
    )

    delete_status = await SHORT_URL_SERVICE.delete_short_urls(
        user_id=user_id,
        short_urls=[short_url],
    )

    if not delete_status:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return DeleteUserShortUrlResponse(
        data=TransactionResponse(is_success=True)
    )
