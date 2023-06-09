from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

username = 'your_username'
password = 'your_password'
account = 'your_account_url'
warehouse = 'your_warehouse'
database = 'your_database'
schema = 'your_schema'

snowflake_url = URL(
    account=account,
    user=username,
    password=password,
    warehouse=warehouse,
    database=database,
    schema=schema
)

engine = create_engine(snowflake_url)
with engine.connect() as connection:
    connection.execute(f"CREATE WAREHOUSE {warehouse}")

