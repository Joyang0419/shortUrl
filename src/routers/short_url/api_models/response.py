"""router: short_url response"""

from src.routers import FormatResponse
from typing import List
from src.entities.short_url_entity import ShortUrlEntity
from pydantic import BaseModel


class TransactionResponse(BaseModel):
    is_success: bool


class CreateShortUrlResponse(FormatResponse):
    data: TransactionResponse

    @staticmethod
    def examples():
        return {
            201: {
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
                                    "error_message": None
                                }
                            }
                        }
                    }
                }
            },
        }


class GetUserShortUrlsResponse(FormatResponse):
    data: List[ShortUrlEntity]

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
                                    "data": [
                                        {
                                            "id": 14,
                                            "user_id": 16,
                                            "short_url": "asb",
                                            "target_url": "asb",
                                            "create_time": "2022-08-05T06:04:24",
                                            "update_time": "2022-08-05T06:04:24"
                                        }
                                    ],
                                    "error_message": None
                                }
                            },
                        }
                    }
                }
            },
        }


class ModifyUserShortUrlResponse(FormatResponse):
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
                                    "error_message": None
                                }
                            }
                        }
                    }
                }
            },
        }


class DeleteUserShortUrlResponse(FormatResponse):
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
                                    "error_message": None
                                }
                            }
                        }
                    }
                }
            },
        }
