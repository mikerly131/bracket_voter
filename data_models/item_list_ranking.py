"""
The composite ranking of a list from the bracket that have been filled out for it.
Only needed for "live" lists of items to be ranked that have at least 1 bracket
Only counts 'complete' bracket for calculating rankings and scoring items, so not using a relationship
"""
from base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from sqlalchemy import ForeignKey
from datetime import datetime


class ItemListRanking(Base):
    __tablename__ = "item_list_ranking"

    id: Mapped[int] = mapped_column(primary_key=True)
    item_list_id: Mapped[int] = mapped_column(ForeignKey("item_list.id"))
    creator: Mapped[int] = mapped_column(ForeignKey("user.id"))

    bracket_count: Mapped[int]
    bracket_ids: Mapped[list] = mapped_column(ARRAY)
    ranked_items: Mapped[list] = mapped_column(JSON)
    scored_items: Mapped[list] = mapped_column(JSON)
    create_dt: Mapped[datetime] = mapped_column(default=datetime.now)
    update_dt: Mapped[datetime] = mapped_column(default=datetime.now)

    def __repr__(self) -> str:
        return f"<List Rank Tracker: {self.id}>"
