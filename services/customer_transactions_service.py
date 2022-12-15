from flask import current_app
import sqlite3
from models import CustomerTransactions

def get_customers():
    query = 'SELECT * FROM Customers_Transactions'
    customers_transactions = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            customer_transaction = CustomerTransactions(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            customers_transactions.append(customer_transaction)
    return customers_transactions

def get_customer(id):
    query = "SELECT * FROM Customers_Transactions WHERE(Customers_Transactions.CustomerTransactionID = %s)"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            customer_transaction = CustomerTransactions(dictionary['CustomerTransactionID'], dictionary['CustomerID'], dictionary['InvoiceID'], dictionary['TransactionDate'], dictionary['AmountExcludingTax'], dictionary['TaxAmount'], dictionary['TransactionAmount'], dictionary['OutstandingBalance'], dictionary['FinalizationDate'], dictionary['IsFinalize'])
            return customer_transaction
    return None
        
def delete_customer(id):
    query = "DELETE FROM Customers_Transactions WHERE(CustomerTransactionID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return True
    except:
        return False

def update_customer(id,Customer_Transaction):
    query = "UPDATE Customers_Transactions SET TransactionDate=%s, AmountExcludingTax=%s, TaxAmount=%s, TransactionAmount=%s, OutstandingBalance=%s, FinalizationDate=%s, IsFinalize=%s WHERE (CustomerTransactionID = %s)"
    customer_transaction = Customer_Transaction.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (customer_transaction['TransactionDate'], customer_transaction['AmountExcludingTax'], customer_transaction['TaxAmount'], customer_transaction['TransactionAmount'], customer_transaction['OutstandingBalance'], customer_transaction['FinalizationDate'], customer_transaction['IsFinalize'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 




