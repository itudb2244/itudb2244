from flask import current_app
import sqlite3
from models import StockItems

def get_stock_items():
    query = "SELECT * FROM STOCK_ITEMS"
    stock_items = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            stock_item = StockItems(row[0], row[1], row[2], row[3], row[4])
            stock_items.append(stock_item)
    return stock_items

def get_stock_item(id):
    query = "SELECT * FROM STOCK_ITEMS WHERE(STOCK_ITEMS.stockItemID = %s)"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            stock_item = StockItems(dictionary['StockItemID'], dictionary['StockItemName'], dictionary['LeadTimeDays'], dictionary['UnitPrice'], dictionary['RecommendedRetailPrice'])
            return stock_item
    return None

def add_stock_item(Stock_Item):
    query = "INSERT INTO STOCK_ITEMS (stockItemName, leadTimeDays, unitPrice, recommendedRetailPrice)"\
            "VALUES (%(stockItemName)s, %(leadTimeDays)s,%(unitPrice)s,%(recommendedRetailPrice)s)"\
            "RETURNING stockItemID"
    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        stock_item = Stock_Item.get()
        cursor.execute(query,stock_item)
        stockItemID = cursor.fetchone()[0]
        return stockItemID
        
def delete_stock_item(id):
    query = "DELETE FROM STOCK_ITEMS WHERE(stockItemID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return True
    except:
        return False

def update_stock_item(id,Stock_Item):
    query = "UPDATE STOCK_ITEMS SET stockItemName=%s, leadTimeDays=%s, unitPrice=%s, recommendedRetailPrice=%s WHERE (stockItemID = %s)"
    stock_item = Stock_Item.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (stock_item['stockItemName'], stock_item['leadTimeDays'], stock_item['unitPrice'], stock_item['recommendedRetailPrice'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 
