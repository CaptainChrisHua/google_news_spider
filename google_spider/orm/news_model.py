from sqlalchemy import Column, Integer, Identity
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class NewsModel(Base):
    __tablename__ = 'news'

    id = Column(Integer, Identity(always=True), autoincrement=True, primary_key=True)
    web_name = Column(String(50), comment='web name')
    title = Column(String(255), comment='news title')
    abstract = Column(String(1024), comment='abstract')
    url = Column(String(255), comment='url')
    image = Column(String(255), comment='image_url')
    release_time = Column(String(255), comment='release_time')
