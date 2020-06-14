

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean
class Timeaxis(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String(100), nullable=False)
    content = Column(String(100), nullable=False)

    start_time = Column(String(100), nullable=False)
    end_time = Column(String(100), nullable=False)

    state = Column(Integer, default=1)

