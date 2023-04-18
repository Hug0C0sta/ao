from sqlalchemy import Column, Integer, String, Float

from src.models.base import Base


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(String)
    long = Column(String)
