from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from note_taking.models import Base

DATABASE_URL = 'sqlite:///note_taking.db'

def create_session():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
