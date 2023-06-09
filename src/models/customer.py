import uuid

from sqlalchemy import Column, String, UUID

from src.models.base import Base


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_customer = Column(String)
    lat = Column(String)
    long = Column(String)
