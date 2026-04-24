from fastapi import Depends, FastAPI, File, Form, UploadFile
from app.db import create_tables, get_db
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
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

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session:AsyncSession = Depends(get_db)    
):
    post = Post(
        caption=caption,
        url="dummy url",
        file_type = "photo",
        file_name = "dummy name"
    )
    
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post
    
@app.get("/feed")
async def feed(session:AsyncSession = Depends(get_db)):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [rows[0] for rows in result.all()]
    
    posts_data = []
    for post in posts:
        posts_data.append(
            {
                "id":str(post.id),
                "caption":post.caption,
                "url":post.url,
                "file_type":post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at.isoformat()
            }
        )
    return {"posts": posts_data}