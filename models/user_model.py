import datetime

from sqlalchemy import Column, ForeignKey, Table, orm
from sqlalchemy import String
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import LONGTEXT

class UserModel(DeclarativeBase):
    __tablename__ = "User"

    user_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    registered_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    disabled: Mapped[bool] = mapped_column(default=False)