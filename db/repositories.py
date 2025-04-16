from .models import Base


class DbRepository:
    def __init__(self, engine, session):
        self.engine = engine
        self.session = session

    async def create_database(self):
        async with self.engine.connect() as conn:
            await conn.run_sync(Base.metadata.create_all)
            await conn.commit()

    async def delete_database(self):
        async with self.engine.connect() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.commit()

    async def save_data(self):
        pass