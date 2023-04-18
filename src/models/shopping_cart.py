import uuid

from sqlalchemy import Column, ForeignKey, UUID

from src.models.base import Base


class ShoppingCart(Base):
    __tablename__ = 'shopping_cart'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fk_order_id = Column(UUID, ForeignKey('order.id'))
    fk_order_item_id = Column(UUID, ForeignKey('order_items.id'))
