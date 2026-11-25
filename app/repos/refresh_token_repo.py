from sqlalchemy.ext.asyncio import AsyncSession

from app.models.refresh_token import RefreshToken

from datetime import datetime




async def create_db_refresh_token(session: AsyncSession, user_id: int, token_hash: str, expires_at: datetime) -> RefreshToken:
    refresh_token = RefreshToken(
        token_hash=token_hash, 
        user_id=user_id, 
        expires_at=expires_at       
    )
    session.add(refresh_token)
    return refresh_token
