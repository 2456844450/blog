from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean
class Message(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    content = Column(String(100), nullable=False)
    state = Column(Integer, default=1)
