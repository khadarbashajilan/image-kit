from fastapi import FastAPI
from app.db import create_tables, get_db
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
import logging
from app.model import Post 

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await create_tables()
        logging.info("Database tables created successfully")
    except Exception as e:
        logging.error(f"Error creating database tables: {e}")
        raise
    yield
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

