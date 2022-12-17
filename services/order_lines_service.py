from flask import current_app
import sqlite3
from models import OrderLines

def get_order_lines():
    query = "SELECT * FROM ORDER_LINES, Orders, Stock_Item WHERE((ORDER_LINES.orderID=ORDERS.orderID) AND (ORDER_LINES.stockItemID=STOCK_ITEMS.stockItemID))"
    order_lines = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            order_line = OrderLines(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            order_lines.append(order_line)
    return order_lines

def get_order_line(id):
    query = "SELECT * FROM ORDER_LINES, ORDERS, STOCK_ITEMS WHERE(ORDER_LINES.orderLineID = %s) AND ((ORDER_LINES.orderID=ORDERS.orderID) AND (ORDER_LINES.stockItemID=STOCK_ITEMS.stockItemID))"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            order_line = OrderLines(dictionary['OrderLineID'], dictionary['OrderID'], dictionary['StockItemID'], dictionary['Description'], dictionary['Quantity'], dictionary['UnitPrice'], dictionary['PickedQuantity'], dictionary['PickingCompletedWhen'])
            return order_line
    return None

def add_order_line(Order_Line):
    query = "INSERT INTO ORDER_LINES (orderID, stockItemID, description, quantity, unitPrice, pickedQuantity, pickingCompletedWhen)"\
            "VALUES (%(orderID)s,%(stockItemID)s,%(description)s,%(quantity)s,%(unitPrice)s,%(pickedQuantity)s,%(pickingCompletedWhen)s)"\
            "RETURNING orderLineID"
    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        order_line = Order_Line.get()
        cursor.execute(query,order_line)
        orderLineID = cursor.fetchone()[0]
        return orderLineID
        
def delete_order_line(id):
    query = "DELETE FROM ORDER_LINES WHERE(orderLineID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return True
    except:
        return False

def update_order_line(id,Order_Line):
    query = "UPDATE ORDER_LINES SET orderID=%s, stockItemID=%s, description=%s, quantity=%s, unitPrice=%s, pickedQuantity=%s, pickingCompletedWhen=%s WHERE (orderLineID = %s)"
    order_line = Order_Line.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query,(order_line['OrderID'], order_line['StockItemID'], order_line['Description'], order_line['Quantity'], order_line['UnitPrice'], order_line['PickedQuantity'], order_line['PickingCompletedWhen'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 




