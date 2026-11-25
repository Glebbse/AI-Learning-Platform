from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import UserDefinedOption


from app.schemas.user import UserCreate, UserRead
from app.models.user import User


async def create_db_user(session: AsyncSession, email: str, password_hash: str) -> User:
    user = User(
        email=email, 
        password_hash=password_hash
    )
    session.add(user)
    return user

async def get_db_user_by_email(session: AsyncSession, email: str) -> User | None:
    query = select(User).where(User.email == email)
    result = await session.execute(query)
    return result.scalar_one_or_none()

async def get_db_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()

async def delete_db_user(session: AsyncSession, user: User) -> dict:
    await session.delete(user)
    return {"deleted": user}