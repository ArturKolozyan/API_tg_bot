from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .models import Base
from src.config import config


class DbRepository:

    def __init__(self):
        self.engine = create_async_engine(config.get_db_url, echo=True)
        self.session = async_sessionmaker(self.engine)

    async def create_database(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def delete_database(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)


db = DbRepository()
