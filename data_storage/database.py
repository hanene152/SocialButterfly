# data_storage/database.py

from config import DATABASE_URI
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    user = Column(String)
    created_at = Column(DateTime)

class RedditPost(Base):
    __tablename__ = 'reddit_posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user = Column(String)
    created_at = Column(DateTime)

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def store_tweets(tweets):
    for tweet in tweets:
        tweet_obj = Tweet(**tweet)
        session.add(tweet_obj)
    session.commit()

def store_reddit_posts(posts):
    for post in posts:
        post_obj = RedditPost(**post)
        session.add(post_obj)
    session.commit()
