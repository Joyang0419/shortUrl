"""user_repo exceptions."""


class DuplicateAccountException(Exception):
    message = "Duplicate Account."

    def __str__(self):
        return DuplicateAccountException.message
