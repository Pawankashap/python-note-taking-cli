from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///notetakingdb.db")
Session = sessionmaker(bind=engine)

note_tag_association = Table(
    'note_tag_association',
    Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,  autoincrement= True)
    username = Column(String, unique=True, nullable=False)
    notes = relationship("Note", back_populates="user")



class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    # tag_id= Column(Integer, ForeignKey("tags.id"))

    user = relationship("User", back_populates="notes")
    tags= relationship("Tag",secondary=note_tag_association, back_populates="notes")

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    notes=relationship("Note",secondary=note_tag_association,back_populates="tags")

Base.metadata.create_all(bind=engine)