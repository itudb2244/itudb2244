from flask import current_app
import sqlite3
from models import Invoices

def get_invoices():
    query = 'SELECT * FROM Invoices'
    invoices = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            invoice = Invoices(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
            invoices.append(invoice)
    return invoices

def get_invoice(id):
    query = "SELECT * FROM Invoices WHERE(Invoices.InvoiceID = %s)"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            invoice = Invoices(dictionary['InvoiceID'], dictionary['CustomerID'], dictionary['OrderID'], dictionary['ContactPersonID'], dictionary['AccountsPersonID'], dictionary['InvoiceDate'], dictionary['CustomerPurchaseOrderNumber'], dictionary['DeliveryInstructions'], dictionary['InternalComments'], dictionary['DeliveryRun'], dictionary['RunPosition'], dictionary['ReturnedDeliveryData'], dictionary['ConfirmedDeliveryTime'], dictionary['ConfirmedReceivedBy'])
            return invoice
    return None
        
def delete_customer(id):
    query = "DELETE FROM Invoices WHERE(InvoiceID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return True
    except:
        return False

def update_customer(id,Invoice):
    query = "UPDATE Invoices SET InvoiceDate=%s, CustomerPurchaseOrderNumber=%s, DeliveryInstructions=%s, InternalComments=%s, DeliveryRun=%s, RunPosition=%s , ReturnedDeliveryData=%s , ConfirmedDeliveryTime=%s , ConfirmedReceivedBy=%s WHERE (CustomerID = %s)"
    invoice = Invoice.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (invoice['InvoiceDate'], invoice['CustomerPurchaseOrderNumber'], invoice['DeliveryInstructions'], invoice['InternalComments'], invoice['DeliveryRun'], invoice['RunPosition'], invoice['ReturnedDeliveryData'], invoice['ConfirmedDeliveryTime'], invoice['ConfirmedReceivedBy'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 




