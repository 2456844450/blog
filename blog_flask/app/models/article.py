



from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean
class Article(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    desc = Column(String(100), nullable=False)
    author = Column(String(20))
    img_url = Column(String(100))
    comments = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    views = Column(Integer, default=0)
    state = Column(Integer, default=1)
    year = Column(Integer, default=0)

    field = Column(Integer, default=0)

    project_name = Column(String(100))
    project_url = Column(String(100))
    start_time = Column(String(100))
    end_time = Column(String(100))

    numbers = Column(Integer, default=0)

    tags = Column(String(100))

    content = Column(String(10000))

    keyword = Column(String(50))

    @staticmethod
    def article_message_list(id):
        article = Article.query.filter_by(id=id).first()
        if article:
            views = article.views
            likes = article.likes
            comments = article.comments

            desc = article.desc

            numbers = article.numbers

            img_url = article.img_url

            state = article.state

            tags = article.tags

            tagArray = tags.split(',')

            tagList = []
            for tag in tagArray:
                tagList.append({
                    '_id': tag,
                    'name': tag
                })
            title = article.title

            content = article.content
            return {
                'meta': {
                    'views': views,
                    'likes': likes,
                    'comments': comments
                },
                'desc': desc,
                'numbers': numbers,
                'img_url': img_url,
                'state': state,
                'tags': tagList,
                'comments': [],
                '_id': id,
                'title': title,
                'author': 'azhou就是安州啊',
                'content': content,
                'create_time': article.create_datetime
            }
        else:
            return None