from .db import Base 
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime


# MODEL
class Post(Base):
    __tablename__ = "posts"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    caption = Column(Text)
    url = Column(String(255), nullable=False)
    file_type = Column(String(50), nullable=False)
    file_name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    