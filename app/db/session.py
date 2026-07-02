from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_async_engine(settings.db_url, echo=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

