import uuid

from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime, Numeric, UUID

from src.models.base import Base


class Order(Base):
    __tablename__ = 'order'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_order = Column(String)
    date = Column(DateTime)
    order_price = Column(Numeric(10, 2))
    order_total = Column(Numeric(10, 2))
    coupon_discount = Column(Numeric(10, 2))
    is_expedited_delivery = Column(Boolean)
    season = Column(String)
    distance_to_nearest_warehouse = Column(Numeric(10, 2))
    nearest_warehouse = Column(String)
    is_happy_customer = Column(Boolean)
    delivery_charges = Column(Numeric(10, 2))

    # fk_shopping_cart = Column(UUID, ForeignKey('shopping_cart.id'),  default=uuid.uuid4)
    fk_customer = Column(UUID, ForeignKey('customer.id'), default=uuid.uuid4)
    fk_opinion = Column(UUID, ForeignKey('opinion.id'), default=uuid.uuid4)
