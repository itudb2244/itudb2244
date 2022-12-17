from flask import current_app
import sqlite3
from models import Customer

def get_customers():
    query = 'SELECT * FROM Customers, People WHERE( (Customers.CustomerID = %s) AND (Customers.primaryContactPersonID=People.personID))'
    customers = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            customers.append(customer)
    return customers

def get_customer(id):
    query = "SELECT * FROM Customers, People WHERE( (Customers.CustomerID = %s) AND (Customers.primaryContactPersonID=People.personID))"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            customer = Customer(dictionary['CustomerID'], dictionary['CustomerName'], dictionary['PrimaryContactPersonID'], dictionary['PhoneNumber'], dictionary['WebSiteURL'], dictionary['DeliverAddressLine1'], dictionary['DeliverAddressLine2'])
            return customer
    return None

def add_customer(Customer):
    query = "INSERT INTO Customers (customerID, customerName, primaryContactPersonID,  phoneNumber, websiteURL, deliveryAddressLine1, deliveryAddressLine2)"\
            "VALUES (%(customerID)s, %(customerName)s,%(primaryContactPersonID)s,%(phoneNumber)s,%(websiteURL)s,%(deliveryAddressLine1)s,%(deliveryAddressLine2)s)"\
            "RETURNING customerID"
    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        customer = Customer.get()
        cursor.execute(query,customer)
        customerID = cursor.fetchone()[0]
        return customerID
        
def delete_customer(id):
    query = "DELETE FROM Customers WHERE(CustomerID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            connection.commit()
            return True
    except:
        return False



def update_customer(id,Customer):
    query = "UPDATE Customers SET CustomerName=%s, PrimaryContactPersonID=%s, PhoneNumber=%s, WebsiteURL=%s, DeliveryAddressLine1=%s, DeliveryAddressLine2=%s WHERE (CustomerID = %s)"
    customer = Customer.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (customer['CustomerName'], customer['PrimaryContactPersonID'], customer['PhoneNumber'], customer['WebSiteURL'], customer['DeliverAddressLine1'], customer['DeliverAddressLine2'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 
