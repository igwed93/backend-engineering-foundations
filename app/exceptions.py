class UserServiceError(Exception):
    """Base exception for user service errors."""

class InvalidUserDataError(UserServiceError):
    pass