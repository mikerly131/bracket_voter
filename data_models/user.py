"""
Users create lists of items to be made into brackets for other users to fill out.
They fill out brackets of their own lists and other users lists.
They view composite rankings of a list from all completely filled out brackets.
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
    item_list_count: Mapped[int]
    live_item_list_count: Mapped[int]
    brackets_active: Mapped[int]
    brackets_complete: Mapped[int]
    create_dt: Mapped[datetime] = mapped_column(default=datetime.now)
    last_login: Mapped[datetime] = mapped_column(default=datetime.now)

    def __repr__(self) -> str:
        return f"<User: {self.username}>"
