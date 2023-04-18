import uuid

from sqlalchemy import Column, Integer, String, UUID, ForeignKey

from src.models.base import Base


class OrderItems(Base):
    __tablename__ = 'order_items'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    quantity = Column(Integer)
    fk_product_id = Column(UUID, ForeignKey('products.id'), default=uuid.uuid4)

