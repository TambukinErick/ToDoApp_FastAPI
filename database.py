from collections.abc import AsyncGenerator
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(DB_URL) #Add echo=True for displaying the queries in the terminal
    factory = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError as error:
            await session.rollback()
            raise




# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# engine = create_engine(DB_URL,echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()