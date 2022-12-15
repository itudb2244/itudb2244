from flask import current_app
import sqlite3
from models import Orders

def get_orders():
    query = 'SELECT * FROM Orders'
    orders = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            order = Orders(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            orders.append(order)
    return orders

def get_order(id):
    query = "SELECT * FROM Orders WHERE(Orders.OrderID = %s)"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            order = Orders(dictionary['OrderID'], dictionary['CustomerID'], dictionary['OrderDate'], dictionary['ExpectedDeliveryDate'], dictionary['CustomerPurchaseOrderNumber'], dictionary['IsUndersupplyBackordered'], dictionary['PickingCompletedWhen'])
            return order
    return None
        
def delete_order(id):
    query = "DELETE FROM Orders WHERE(OrderID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return True
    except:
        return False

def update_order(id,Order):
    query = "UPDATE Orders SET OrderDate=%s, ExpectedDeliveryDate=%s, CustomerPurchaseOrderNumber=%s, IsUndersupplyBackordered=%s, PickingCompletedWhen=%s WHERE (OrderID = %s)"
    order = Order.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (order['OrderDate'], order['ExpectedDeliveryDate'], order['CustomerPurchaseOrderNumber'], order['IsUndersupplyBackordered'], order['PickingCompletedWhen'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 




