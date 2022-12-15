from flask import current_app
import sqlite3
from models import OrderLines

def get_customers():
    query = 'SELECT * FROM Order_Lines'
    order_lines = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            order_line = OrderLines(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            order_lines.append(order_line)
    return order_lines

def get_customer(id):
    query = "SELECT * FROM Order_Lines WHERE(Order_Lines.OrderLineID = %s)"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            order_line = OrderLines(dictionary['OrderLineID'], dictionary['OrderID'], dictionary['StockItemID'], dictionary['Description'], dictionary['Quantity'], dictionary['UnitPrice'], dictionary['PickedQuantity'], dictionary['PickingCompletedWhen'])
            return order_line
    return None
        
def delete_customer(id):
    query = "DELETE FROM Order_Lines WHERE(CustomerID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return True
    except:
        return False

def update_customer(id,Order_Line):
    query = "UPDATE Order_Lines SET Description=%s, Quantity=%s, UnitPrice=%s, PickedQuantity=%s, PickingCompletedWhen=%s WHERE (OrderLineID = %s)"
    order_line = Order_Line.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query,(order_line['Description'], order_line['Quantity'], order_line['UnitPrice'], order_line['PickedQuantity'], order_line['PickingCompletedWhen'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 




