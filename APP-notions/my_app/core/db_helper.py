from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from settings import settings


class DataBaseHelper:
    def __init__(self, db_url, echo: bool = False, max_overflow: int = 10):
        self.engine = create_async_engine(url=db_url, echo=echo, max_overflow=max_overflow)
        self.session_factory = async_sessionmaker(bind=self.engine, autoflush=False,
                                                  expire_on_commit=False, autocommit=False)

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DataBaseHelper(db_url=str(settings.db.db_url), echo=settings.db.echo, max_overflow=settings.db.max_overflow)
