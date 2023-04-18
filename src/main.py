from src.connections.database import Session, create_tables
from src.models.customer import Customer
from importer import specific_columns

if __name__ == '__main__':
    create_tables()
    with Session() as session:
        for _, row in specific_columns.iterrows():
            customer = Customer(lat=row['customer_lat'], long=row['customer_long'])
            session.add(customer)

        session.commit()

