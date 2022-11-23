from flask import current_app
import sqlite3
from models import Consumer

def get_consumers():
    query = 'SELECT * FROM Customers'
    consumers = []

    with sqlite3.connect(current_app.config["dbname"]) as con:
        cursor = con.cursor()
        res = cursor.execute(query)
        for row in res:
            consumer = Consumer(row[0], row[1])
            consumers.append(consumer)
    return consumers
