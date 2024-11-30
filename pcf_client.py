# pcf_client.py
import requests
import json
from datetime import datetime, timedelta
import mysql.connector
import pytz

API_URL = 'http://localhost:8000/api/messages/'

# Function to get the last product id from the database
def get_last_product_id():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='root',  # Replace with your MySQL password
        database='pcf_db'  # Ensure this matches your Django settings
    )
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM pcf_app_message;")
    last_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return last_id if last_id is not None else 0

# Function to send message
def send_message(product_name, carbon_footprint, reference_start, reference_stop):
    data = {
        'product_name': product_name,
        'carbon_footprint': carbon_footprint,
        'reference_start': reference_start,
        'reference_stop': reference_stop
    }
    response = requests.post(API_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    return response

if __name__ == "__main__":
    last_id = get_last_product_id()
    timezone = pytz.timezone('Asia/Kolkata')
    for i in range(1, 11):
        product_id = last_id + i
        product_name = f'Product {product_id}'
        carbon_footprint = 50.0 + product_id
        now = datetime.now(timezone)
        reference_start = now.isoformat()
        reference_stop = (now + timedelta(hours=1)).isoformat()
        response = send_message(product_name, carbon_footprint, reference_start, reference_stop)
        print(f'Status Code: {response.status_code}, Response: {response.json() if response.status_code == 200 else response.text}')
