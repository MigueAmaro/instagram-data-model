import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    mail = Column(String, unique = True)
    password = Column(String)
    biography = Column(String, nullable = True)

class Post(Base):
    __tablename__ = 'Post'

    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    caption = Column(String(2200), nullable = True)

class Media(Base):
    __tablename__ = 'Media'
    
    media_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.post_id'))
    source_media = Column(String)
    type_media = Column(Enum)      

class Stories(Base):
    __tablename__ = 'stories'

    id = Column(Integer, primary_key=True)
    stories = Column(String(250))
    stories_id = Column(Integer, ForeignKey('User.id'))

class Comment(Base):
    __tablename__ = 'Comment'
    
    Comment_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.post_id'))
    user_id = Column(Integer, ForeignKey('User.id'))
    Comment = Column(String)

class Followers(Base):
    __tablename__ = 'Followers'
    
    Followers_id = Column(Integer, primary_key=True)
    User_From_id = Column(Integer, ForeignKey('User.id'))
    User_To_id = Column(Integer, ForeignKey('User.id'))
    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e