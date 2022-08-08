"""json web token services exceptions."""


class DecodeException(Exception):
    message = "Decode token failed."

    def __str__(self):
        return DecodeException.message
