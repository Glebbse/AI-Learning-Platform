



import asyncio

from logging import getLogger

from fastapi import FastAPI
from sqlalchemy import text


from app.core.exceptions import register_exception_handlers
from app.core.session import engine
from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router



logger = getLogger(__name__)


app = FastAPI(title="AI Interview Platform", description="An AI-powered interview platform for developers.", version="1.0.0")

app.include_router(health_router)
app.include_router(auth_router)

register_exception_handlers(app)

async def test_db():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        logger.info("DB result: %s", result.scalar())


if __name__ == "__main__":
    asyncio.run(test_db())
