import uuid

from importer import specific_columns
from src.connections.database import Session, create_tables
from src.models.customer import Customer
from src.models.opinion import Opinion
from src.models.order import Order
from src.models.order_items import OrderItems
from src.models.shopping_cart import ShoppingCart

if __name__ == '__main__':
    create_tables()
    count = 1
    with Session() as session:
        for _, row in specific_columns.iterrows():
            order_id = uuid.uuid4()
            customer_id = uuid.uuid4()
            opinion_id = uuid.uuid4()

            order_items = []
            for item in eval(row['shopping_cart']):
                order_items_id = uuid.uuid4()
                order_item = OrderItems(id=order_items_id, item=item[0], quantity=item[1])
                order_items.append(order_item)
                session.add(order_item)


            customer = Customer(lat=row['customer_lat'], long=row['customer_long'],
                                id_customer=row['customer_id'], id=customer_id)
            session.add(customer)

            opinion = Opinion(opinion=row['latest_customer_review'], id=opinion_id)
            session.add(opinion)

            order = Order(id=order_id, id_order=row['order_id'], date=row['date'], order_price=row['order_price'],
                          order_total=row['order_total'], coupon_discount=row['coupon_discount'],
                          is_expedited_delivery=row['is_expedited_delivery'], season=row['season'],
                          distance_to_nearest_warehouse=row['distance_to_nearest_warehouse'],
                          nearest_warehouse=row['nearest_warehouse'],
                          is_happy_customer=row['is_happy_customer'], delivery_charges=row['delivery_charges'],
                          fk_customer=customer_id, fk_opinion=opinion_id)
            session.add(order)

            count+=1

            for item in order_items:
                shopping_cart_id = uuid.uuid4()
                shopping_cart = ShoppingCart(id=shopping_cart_id, fk_order_id=order_id, fk_order_item_id=order_items_id)
                session.add(shopping_cart)


        session.commit()
