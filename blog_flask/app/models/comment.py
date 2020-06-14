



from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean
class Comment(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    article_id = Column(Integer, nullable=False)
    article_type = Column(Integer, default=1)
    content = Column(String(100), nullable=False)
    from_uid = Column(Integer, nullable=False)
    to_uid = Column(Integer, default=-1)
    origin_uid = Column(Integer)
    state = Column(Integer, default=1)
    comment_id = Column(Integer)