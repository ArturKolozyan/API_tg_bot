from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .models import Base
from src.config import config

engine = create_async_engine(config.get_db_url, echo=True)
session = async_sessionmaker(engine)

class DatabaseService:

    async def create_database(self):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def delete_database(self):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)