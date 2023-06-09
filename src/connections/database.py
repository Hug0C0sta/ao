from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.base import Base

username = 'postgres'
password = 'rDUTTaeFPN1JZ3XxSqUH'
host = 'containers-us-west-111.railway.app'
port = '6875'
database = 'railway'

url = f'postgresql://{username}:{password}@{host}:{port}/{database}'


engine = create_engine(url)


Session = sessionmaker(engine)


def create_tables():
    Base.metadata.create_all(engine)
