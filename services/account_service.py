from data_models.user import User
from typing import Optional
from db import database
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from sqlalchemy import select, func


# Using sqlalchemy 2.0 async sessions
async def create_account(username: str, password: str) -> User:
    user = User()
    user.username = username
    user.hash_password = crypto.hash(password, rounds=143_589)

    async with database.get_async_session() as session:
        session.add(user)
        await session.commit()

    return user


async def login_account(username: str, password: str) -> Optional[User]:
    async with database.get_async_session() as session:
        query = select(User).filter(User.username == username)
        result = await session.execute(query)
        user = result.scalar_one_or_none()

        if not user:
            return user

        if not crypto.verify(password, user.hash_password):
            return None

        return user


async def get_user_by_id(user_id: int) -> Optional[User]:
    async with database.get_async_session() as session:
        query = select(User).filter(User.id == user_id)
        # returns a tuple, need to access with .scalar()
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def get_user_by_username(username: str) -> Optional[User]:
    async with database.get_async_session() as session:
        query = select(User).filter(User.username == username)
        # returns a tuple, need to access with .scalar()
        result = await session.execute(query)
        return result.scalar_one_or_none()
