from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from data_models.base_model import Base
from dotenv import load_dotenv
import os


load_dotenv("db.env")
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
