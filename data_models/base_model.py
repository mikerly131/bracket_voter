"""
This file creates the base sqlalchemy base class for the ORM and gathering metadata
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
