"""user services exceptions."""


class CreateUserException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def as_dict(self):
        return {"msg": self.message}
