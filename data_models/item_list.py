"""
A list of items to rank bracket style (64, 32, 16, 8, 4, 2, 1 winner).
App will update count each time list is modified, must have 64 to make a list live for bracketing
A live list can no longer be modified
"""
from base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import String, Enum, ForeignKey
from datetime import datetime


class ItemList(Base):
    __tablename__ = "item_list"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(Enum("draft", "live"), default="draft", nullable=False)
    type: Mapped[str]
    count: Mapped[int] = mapped_column(default=0, nullable=False)
    items: Mapped[list] = mapped_column(JSON)
    create_dt: Mapped[datetime] = mapped_column(default=datetime.now)
    update_dt: Mapped[datetime] = mapped_column(default=datetime.now)

    def __repr__(self) -> str:
        return f"<List: {self.name}>"
