from flask import current_app
import sqlite3
from models import Orders

def get_orders():
    query = "SELECT * FROM ORDERS, CUSTOMERS WHERE (ORDERS.customerID=CUSTOMERS.customerID)"
    orders = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            order = Orders(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            orders.append(order)
    return orders

def get_order(id):
    query = "SELECT * FROM ORDERS, CUSTOMERS WHERE((ORDERS.OrderID = %s) AND (ORDERS.customerID=CUSTOMERS.customerID))"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            order = Orders(dictionary['OrderID'], dictionary['CustomerID'], dictionary['OrderDate'], dictionary['ExpectedDeliveryDate'], dictionary['CustomerPurchaseOrderNumber'], dictionary['IsUndersupplyBackordered'], dictionary['PickingCompletedWhen'])
            return order
    return None

def add_order(Order):
    query = "INSERT INTO ORDERS (customerID, orderDate, expectedDeliveryDate,  customerPurchaseOrderNumber, isUndersupplyBackordered, pickingCompletedWhen)"\
            "VALUES (%(customerID)s, %(orderDate)s,%(expectedDeliveryDate)s,%(customerPurchaseOrderNumber)s,%(isUndersupplyBackordered)s,%(pickingCompletedWhen)s)"\
            "RETURNING orderID"
    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        order = Order.get()
        cursor.execute(query,order)
        orderID = cursor.fetchone()[0]
        return orderID
        
def delete_order(id):
    query = "DELETE FROM ORDERS WHERE(orderID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return True
    except:
        return False

def update_order(id,Order):
    query = "UPDATE ORDERS SET customerID=%s, orderDate=%s, expectedDeliveryDate=%s, customerPurchaseOrderNumber=%s, isUndersupplyBackordered=%s, pickingCompletedWhen=%s WHERE (orderID = %s)"
    order = Order.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (order['customerID'], order['OrderDate'], order['ExpectedDeliveryDate'], order['CustomerPurchaseOrderNumber'], order['IsUndersupplyBackordered'], order['PickingCompletedWhen'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 




