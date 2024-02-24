"""
Bracket are created from an initial list of ranked items.
They contain a reference to the initial list used to generate the initial round and the results of each ranking round
"""
from base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Enum, ForeignKey
from datetime import datetime


class Bracket(Base):
    __tablename__ = "bracket"

    id: Mapped[int] = mapped_column(primary_key=True)
    item_list_id: Mapped[int] = mapped_column(ForeignKey("item_list.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    status: Mapped[str] = mapped_column(Enum("active", "complete"), default="active")
    round_64: Mapped[list] = mapped_column(JSON)
    round_32: Mapped[list] = mapped_column(JSON)
    sweet_16: Mapped[list] = mapped_column(JSON)
    elite_8: Mapped[list] = mapped_column(JSON)
    final_4: Mapped[list] = mapped_column(JSON)
    last_2: Mapped[list] = mapped_column(JSON)
    champion: Mapped[dict] = mapped_column(JSON)
    create_dt: Mapped[datetime] = mapped_column(default=datetime.now)
    update_dt: Mapped[datetime] = mapped_column(default=datetime.now)

    def __repr__(self) -> str:
        return f"<Bracket: {self.id}>"

