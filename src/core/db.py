from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from core.settings import settings

engine = create_async_engine(settings.DATABASE_URL, echo=settings.LOCAL, future=True, isolation_level="AUTOCOMMIT")
metadata = MetaData()
DeclarativeBase = declarative_base()
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
