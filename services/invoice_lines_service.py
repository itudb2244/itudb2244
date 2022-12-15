from flask import current_app
import sqlite3
from models import InvoiceLines

def get_invoice_lines():
    query = 'SELECT * FROM Invoice_Lines'
    invoice_lines = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            invoice_line = InvoiceLines(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            invoice_lines.append(invoice_line)
    return invoice_lines

def get_invoice_line(id):
    query = "SELECT * FROM Invoice_Lines WHERE(Invoice_Lines.InvoiceLineID = %s)"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            invoice_line = InvoiceLines(dictionary['InvoiceLineID'], dictionary['InvoiceID'], dictionary['StockItemID'], dictionary['Description'], dictionary['Quantity'], dictionary['UnitPrice'], dictionary['LineProfit'], dictionary['ExtendedPrice'])
            return invoice_line
    return None
        
def delete_invoice_line(id):
    query = "DELETE FROM Invoice_Lines WHERE(InvoiceLineID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return True
    except:
        return False

def update_invoice_line(id, Invoice_line):
    query = "UPDATE Invoice_Lines SET Description=%s, Quantity=%s, UnitPrice=%s, LineProfit=%s, ExtendedPrice=%s WHERE (InvoiceLineID = %s)"
    invoice_line = Invoice_line.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (invoice_line['Description'], invoice_line['Quantity'], invoice_line['UnitPrice'], invoice_line['LineProfit'], invoice_line['ExtendedPrice'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 




