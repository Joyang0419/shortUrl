"""Application module."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from src.configs.app_config import PROJECT_NAME, DEBUG, VERSION, LOGURU_HANDLERS
from src.configs.log_handler import InterceptHandler
from src.implements.db_manager import ASYNC_SQLALCHEMY
from src.routers import user, short_url


def set_logulu_logger():
    """Uses Loguru as project logger."""

    logging.getLogger().handlers = [InterceptHandler()]

    logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]

    logger.configure(handlers=LOGURU_HANDLERS)


def app_init() -> FastAPI:
    set_logulu_logger()

    application = FastAPI(
        title=PROJECT_NAME,
        debug=DEBUG,
        version=VERSION
    )
    #
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"]
    )

    application.include_router(router=user.router)
    application.include_router(router=short_url.router)

    return application


app = app_init()


# @app.on_event("startup")
# async def startup_event():
#     assert await ASYNC_SQLALCHEMY.is_connected()
