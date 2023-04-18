from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.base import Base

engine = create_engine('postgresql://ao:ao@localhost:5432/ao')
Session = sessionmaker(engine)


def create_tables():
    Base.metadata.create_all(engine)
