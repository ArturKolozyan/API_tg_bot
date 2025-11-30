from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from models import Base, User


class DatabaseService:
    def __init__(self, db_url: str, echo: bool = False):
        self.engine = create_async_engine(db_url, echo=echo)
        self.async_session = async_sessionmaker(self.engine)

    async def create_database(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Database tables created.")

    async def delete_database(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        print("Database tables dropped.")

    async def create_user(self, data):
        async with self.async_session() as session:
            async with session.begin():
                new_user = User(**data)
                session.add(new_user)
                await session.flush()
                await session.refresh(new_user)
                return new_user
                pass
