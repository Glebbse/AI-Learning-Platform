



import asyncio

from logging import getLogger

from fastapi import FastAPI
from sqlalchemy import text


from app.db.session import engine
from app.api.routes.health import router as health_router


logger = getLogger(__name__)


app = FastAPI(title="AI Interview Platform", description="An AI-powered interview platform for developers.", version="1.0.0")

app.include_router(health_router)


async def test_db():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        logger.info("DB result: %s", result.scalar())


if __name__ == "__main__":
    asyncio.run(test_db())
