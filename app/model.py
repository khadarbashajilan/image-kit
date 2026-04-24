from .db import Base 
import uuid
from datetime import datetime, timezone, timedelta
from sqlalchemy import Column, String, Text, DateTime

# Create a timezone object for IST
IST = timezone(timedelta(hours=5, minutes=30))

# MODEL
class Post(Base):
    __tablename__ = "posts"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    caption = Column(Text)
    url = Column(String(255), nullable=False)
    file_type = Column(String(50), nullable=False)
    file_name = Column(String(255), nullable=False)
    # Store with IST timezone
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(IST))