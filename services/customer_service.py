from flask import current_app
import sqlite3
from models import Customer

def get_customers():
    query = 'SELECT * FROM Customers'
    customers = []

    with sqlite3.connect(current_app.config["dbname"]) as con:
        cursor = con.cursor()
        res = cursor.execute(query)
        for row in res:
            customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            customers.append(customer)
    return customers
