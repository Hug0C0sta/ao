import uuid

from sqlalchemy.testing.plugin.plugin_base import logging

from importer import specific_columns
from src.connections.database import Session, create_tables
from src.models.customer import Customer
from src.models.opinion import Opinion
from src.models.order import Order
from src.models.order_items import OrderItems
from src.models.shopping_cart import ShoppingCart
from src.models.products import Products

if __name__ == '__main__':
    create_tables()
    with Session() as session:
        for _, row in specific_columns.iterrows():
            order_id = uuid.uuid4()
            customer_id = row['customer_id']
            opinion_id = uuid.uuid4()

            customer = session.query(Customer).filter_by(id_customer=customer_id).first()
            if not customer:
                customer = Customer(lat=row['customer_lat'], long=row['customer_long'],
                                    id_customer=customer_id, id=uuid.uuid4())
                session.add(customer)

            opinion = Opinion(opinion=row['latest_customer_review'], id=opinion_id)
            session.add(opinion)

            order = Order(id=order_id, id_order=row['order_id'], date=row['date'], order_price=row['order_price'],
                          order_total=row['order_total'], coupon_discount=row['coupon_discount'],
                          is_expedited_delivery=row['is_expedited_delivery'], season=row['season'].upper(),
                          distance_to_nearest_warehouse=row['distance_to_nearest_warehouse'],
                          nearest_warehouse=row['nearest_warehouse'].upper(),
                          is_happy_customer=row['is_happy_customer'], delivery_charges=row['delivery_charges'],
                          fk_customer=customer.id, fk_opinion=opinion_id)
            session.add(order)

            for item in eval(row['shopping_cart']):
                product = session.query(Products).filter_by(name=item[0].upper()).first()
                if not product:
                    product = Products(name=item[0].upper(), id=uuid.uuid4())
                    session.add(product)
                    session.commit()

                order_items_id = uuid.uuid4()
                order_item = OrderItems(id=order_items_id, quantity=item[1], fk_product_id=product.id)
                session.add(order_item)
                shopping_cart_id = uuid.uuid4()
                shopping_cart = ShoppingCart(id=shopping_cart_id, fk_order_id=order_id,
                                             fk_order_item_id=order_items_id)
                session.add(shopping_cart)

        session.commit()
