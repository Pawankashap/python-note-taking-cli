from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Assuming you have the 'Base' instance from SQLAlchemy
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # Table name

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

class Post(Base):
    __tablename__ = 'notes'  # Table name

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, nullable=False)  # Foreign key reference to 'users' table

# More models can be defined here...
