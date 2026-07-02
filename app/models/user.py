from sqlalchemy import String, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.core.base import Base





class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    target_role: Mapped[str] = mapped_column(String(20), nullable=True)
    experience_level: Mapped[str] = mapped_column(String(20), nullable=True, default="junior", server_default="junior")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())