from fastapi import Depends, status, HTTPException


from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession


from app.core.session import SessionLocal


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise

