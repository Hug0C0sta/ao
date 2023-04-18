import uuid

from sqlalchemy import Column, Integer, String, UUID

from src.models.base import Base


class Products(Base):
    __tablename__ = 'products'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
