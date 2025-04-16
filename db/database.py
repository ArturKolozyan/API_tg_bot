from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import config
from .repositories import DbRepository

async_engine = create_async_engine(config.get_db_url())
async_session = async_sessionmaker(async_engine)

db = DbRepository(async_engine, async_session)
