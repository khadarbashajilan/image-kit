from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import text
import logging

DATABASE_URL = "mysql+aiomysql://root:jilan123@localhost:3306/image_kit"

# 1. ENGINE FIRST (important)
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

# 2. SESSION
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

# 3. BASE
Base = declarative_base()


# 4. DEPENDENCY
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session



async def create_tables():
    """Create all tables in the database"""
    try:
        async with engine.begin() as conn:
            # Create database if it doesn't exist
            await conn.execute(text("CREATE DATABASE IF NOT EXISTS image_kit"))
            await conn.execute(text("USE image_kit"))
            await conn.run_sync(Base.metadata.create_all)
            logging.info("Tables created successfully")
    except Exception as e:
        logging.error(f"Error creating tables: {e}")
        raise