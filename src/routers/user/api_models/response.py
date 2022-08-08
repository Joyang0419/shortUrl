"""router: user response"""

from typing import Optional

from pydantic import BaseModel

from src.routers import FormatResponse
from src.services.token.models import JWTPayload, AccessToken
from src.entities import UserEntity


class TransactionResponse(BaseModel):
    is_success: bool


class SignUpResponse(FormatResponse):
    data: TransactionResponse

    @staticmethod
    def examples():
        return {
            200: {
                "description": "Success",
                "content": {
                    "application/json": {
                        "examples": {
                            "Success": {
                                "summary": "Success",
                                "value": {
                                    "data": {
                                        "is_success": True
                                    },
                                    "error_message": ""
                                }
                            },
                            "Duplicated account": {
                                "summary": "Duplicated account",
                                "value": {
                                    "data": {
                                        "is_success": False
                                    },
                                    "error_message": "Duplicated account"
                                }
                            },
                            "Something wrong": {
                                "summary": "Something wrong",
                                "value": {
                                    "data": {
                                        "is_success": False
                                    },
                                    "error_message": "Something wrong."
                                }
                            },
                        }
                    }
                }
            },
        }


class GetUserResponse(FormatResponse):
    data: Optional[UserEntity]

    @staticmethod
    def examples():
        return {
            200: {
                "description": "Success",
                "content": {
                    "application/json": {
                        "examples": {
                            "Success": {
                                "summary": "Success",
                                "value": {
                                    "data": {
                                        "id": 15,
                                        "account": "user6",
                                        "hashed_password": "$2b$12$Lw3YBPmLFO5oIkWZcQ0CL.yrHyicUvX9A7fTS7cEJDrXMWtfPtPqO"
                                    },
                                    "error_message": None
                                }
                            },
                        }
                    }
                }
            },
        }


class VerifyTokenResponse(FormatResponse):
    data: Optional[JWTPayload]

    @staticmethod
    def examples():
        return {
            200: {
                "description": "Success",
                "content": {
                    "application/json": {
                        "examples": {
                            "Success": {
                                "summary": "Success",
                                "value": {
                                    "data": {
                                        "sub": {
                                            "user_id": 30,
                                        },
                                        "exp": 1683276039,
                                        },
                                    "error_message": None
                                }
                            },
                            "Decode token failed": {
                                "summary": "Decode token failed",
                                "value": {
                                    "data": None,
                                    "error_message": "Decode token failed"
                                }
                            },
                        }
                    }
                }
            },
        }


class LoginResponse(AccessToken):
    pass

    @staticmethod
    def examples():
        return {
            200: {
                "description": "Success",
                "content": {
                    "application/json": {
                        "examples": {
                            "Success": {
                                "summary": "Success",
                                "value": {
                                    "access_token": ".....",
                                    "token_type": "bearer"
                                }
                            }
                        },
                    }
                }
            },
            401: {
                "description": "Unauthorized",
                "content": {
                    "application/json": {
                        "examples": {
                            "Not found user": {
                                "summary": "Not found user",
                                "value": {
                                    "detail": "Not found user."
                                }
                            },
                            "Wrong password": {
                                "summary": "Wrong password",
                                "value": {
                                    "detail": "Wrong password."
                                }
                            }
                        },
                    }
                }
            },
            500: {
                "description": "Internal server error",
                "content": {
                    "application/json": {
                        "examples": {
                            "Internal server error": {
                                "summary": "Internal server error",
                                "value": {
                                    "detail": "Something wrong."
                                }
                            },
                        },
                    }
                }
            }
        }
