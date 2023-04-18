import uuid

from sqlalchemy import Column, Integer, String, UUID

from src.models.base import Base


class OrderItems(Base):
    __tablename__ = 'order_items'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    item = Column(String)
    quantity = Column(Integer)
