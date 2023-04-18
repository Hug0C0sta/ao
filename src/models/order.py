from sqlalchemy import Column, Integer, String, Date, Float, Boolean

from src.models.base import Base


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    order_price = Column(Float)
    order_total = Column(Float)
    coupon_discount = Column(Integer)
    is_expedited_delivery = Column(Boolean)
    distance_to_nearest_warehouse = Column(String)
    season = Column(String)
    nearest_warehouse = Column(String)
    shopping_cart = Column()
    latest_customer_review = Column(String)
    is_happy_customer = Column(Boolean)
    delivery_charges = Column(Float)
    fk_customer_id = Column(Integer)
