"""
Users create lists of items to be made into bracket for other users to fill out.
They fill out bracket of their own lists and other users lists.
They view composite rankings of a list from all completely filled out bracket.
"""
from base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from datetime import datetime


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    hash_password: Mapped[str]
    item_list_count: Mapped[int] = mapped_column(default=0)
    live_item_list_count: Mapped[int] = mapped_column(default=0)
    brackets_active: Mapped[int] = mapped_column(default=0)
    brackets_complete: Mapped[int] = mapped_column(default=0)
    create_dt: Mapped[datetime] = mapped_column(default=datetime.now)
    last_login: Mapped[datetime] = mapped_column(default=datetime.now)

    def __repr__(self) -> str:
        return f"<User: {self.username}>"
