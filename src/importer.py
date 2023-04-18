from os import path

import pandas as pd
import numpy as np

csv_path = path.join(path.dirname(path.realpath(__file__)), '../csv/dirty_data.csv')

df = pd.read_csv(csv_path)
specific_columns = df[['order_id', 'date', 'nearest_warehouse', 'shopping_cart', 'order_price', 'delivery_charges',
                       'customer_lat', 'customer_long', 'coupon_discount', 'order_total', 'season',
                       'is_expedited_delivery', 'distance_to_nearest_warehouse', 'is_happy_customer']]

