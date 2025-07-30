import pandas as pd
from datetime import datetime, timedelta
import random

def generate_sales_data(rows=100):
    data = []
    start_date = datetime.now()

    for i in range(rows):
        order_id = 1000 + i
        customer_id = random.randint(200, 300)
        timestamp = (start_date - timedelta(minutes=i)).strftime('%Y-%m-%d %H:%M:%S')
        item = random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Cable'])
        quantity = random.randint(1, 5)
        price = round(random.uniform(20.0, 1500.0), 2)
        data.append([order_id, customer_id, timestamp, item, quantity, price])

    df = pd.DataFrame(data, columns=["order_id", "customer_id", "timestamp", "item", "quantity", "price"])
    df.to_csv("ingestion/sales_data.csv", index=False)
    print("sales_data.csv file created.")

generate_sales_data()
