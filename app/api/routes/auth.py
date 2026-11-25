from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_session
from app.schemas.auth import Token
from app.schemas.user import UserLogin, UserRead, UserRegister
from app.services import auth


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", summary="User registration endpoint", response_model=UserRead)
async def register_user(user_in: UserRegister, session: AsyncSession = Depends(get_session)):
    return await auth.register_user(session, user_in)

@router.post("/login", summary="User login endpoint", response_model=Token)
async def login_user(user_in: UserLogin, session: AsyncSession = Depends(get_session)):
    return await auth.login(session, user_in)

@router.post("/logout", summary="User logout endpoint")
async def logout_user(session: AsyncSession = Depends(get_session)):
    return await auth.logout(session)

@router.get("/refresh", summary="Token refresh endpoint")
async def refresh_token():  
    pass

