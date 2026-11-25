from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    """Base class for application-specific exceptions."""
    status_code = 500
    default_msg: str = "Internal server error"

    def __init__(self, msg: str | None = None):
        super().__init__(msg or self.default_msg)


class UserNotFoundError(AppError):
    """Exception raised when a user is not found."""
    status_code = 404
    default_msg = "User not found"

    @classmethod
    def by_id(cls, user_id: int) -> "UserNotFoundError":
        return cls(f"User with id {user_id} not found")

    @classmethod
    def by_email(cls, email: str) -> "UserNotFoundError":
        return cls(f"User with email {email} not found")
    

class UserAlreadyExistsError(AppError):
    """Exception raised when a user already exists."""
    status_code = 409
    default_msg = "User already exists"

    def __init__(self, email: str):
        super().__init__(f"User with email {email} already exists")


class InvalidCredentials(AppError):
    """Exception raised for invalid credentials."""
    status_code = 401
    default_msg = "Invalid email or password"


def register_exception_handlers(app: FastAPI):
    """Register exception handlers for the FastAPI application."""
    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": str(exc)},
        )