from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from data_models.base_model import Base
from dotenv import load_dotenv
import os

# get the db url from the .env file
load_dotenv("db.env")
DATABASE_URL = os.getenv("DATABASE_URL")

# Need engine to connect to a db
engine = create_async_engine(DATABASE_URL, echo=True)

# Need ability to create async sessions to transact against db
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# Establish the connection object to create db tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
