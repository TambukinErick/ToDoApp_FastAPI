import asyncio
import logging
import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.ext.asyncio import create_async_engine

logger = logging.getLogger()


async def migrate_tables() -> None:
    load_dotenv()
    logger.info("Starting to migrate")

    engine = create_async_engine(os.getenv("DB_URL"))
    async with engine.begin() as conn:
        await conn.run_sync(DeclarativeBase.metadata.create_all)

    logger.info("Done migrating")