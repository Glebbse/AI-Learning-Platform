

from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import UserAlreadyExistsError, UserNotFoundError, InvalidCredentials
from app.models.refresh_token import RefreshToken
from app.models.user import User
from app.schemas.user import UserLogin, UserRegister
from app.repos import user_repo, refresh_token_repo

from app.core.security import secure, manage_tokens
from app.schemas.auth import Token


def _ensure_utc_(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)

async def _issue_token_pair_(session: AsyncSession, user_id: int) -> Token:
    access_token = manage_tokens.create_access_token({"sub": str(user_id)})
    refresh_token = manage_tokens.create_refresh_token()
    refresh_token_hash = manage_tokens.hash_refresh_token(refresh_token)  
    expires_at = manage_tokens.get_refresh_token_expires_at()  
    await refresh_token_repo.create_db_refresh_token(session, user_id, refresh_token_hash, expires_at)
    await session.commit()
    return Token(
        access_token=access_token, 
        refresh_token=refresh_token,
        token_type="bearer"
    )

async def _ensure_refresh_token_not_expired_(token: RefreshToken) -> None:
    if _ensure_utc_(token.expires_at) <= datetime.now(timezone.utc):
        raise InvalidCredentials("Invalid refresh token")

async def register_user(session: AsyncSession, payload: UserRegister) -> User:
    existing_user = await user_repo.get_db_user_by_email(session, payload.email)

    if existing_user:
        raise UserAlreadyExistsError(payload.email)

    password_hash = secure.hash_password(payload.password)

    user = await user_repo.create_db_user(session, payload.email, password_hash)
    await session.commit()
    return user

async def delete_user(session: AsyncSession, user: User) -> dict:
    await user_repo.delete_db_user(session, user)
    await session.commit()
    return {"deleted": user}

async def authenticate_user(session: AsyncSession, payload: UserLogin) -> User:
    user = await user_repo.get_db_user_by_email(session, payload.email)
    if not user or not secure.verify_password(payload.password, user.password_hash):
        raise InvalidCredentials("Invalid email or password")
    return user

async def login(session: AsyncSession, payload: UserLogin) -> Token:
    user = await authenticate_user(session, payload)
    token = await _issue_token_pair_(session, user.id)
    return token

async def logout(session: AsyncSession):
    pass
