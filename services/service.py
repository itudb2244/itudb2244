from flask import current_app
import sqlite3
from models import *

class Service():
    def __init__(self, type, object_type):
        self.type = type
        self.object_type = object_type

    def get_data(self):
        query = 'SELECT * FROM ' + self.type
        object_list = []

        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            res = cursor.execute(query)
            for row in res:
                new_object = self.object_type(row)
                object_list.append(new_object)

        return object_list

    def get_rows_by_column(self, id, column):
        query = 'SELECT * FROM '+self.type+' WHERE('+self.type+'.'+column+' = {})'.format(id)
        object_list = []
        
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            res = cursor.execute(query)
            for row in res:
                new_object = self.object_type(row)
                object_list.append(new_object)

        return object_list
        

class CustomerService(Service):
    def __init__(self):
        Service.__init__(self, "Customers", Customer)

class CustomerTransactionService(Service):
    def __init__(self):
        Service.__init__(self, "CustomerTransactions", CustomerTransactions)

class InvoiceLineService(Service):
    def __init__(self):
        Service.__init__(self, "InvoiceLines", InvoiceLines)

class InvoiceService(Service):
    def __init__(self):
        Service.__init__(self, "Invoices", Invoices)

class OrderLineService(Service):
    def __init__(self):
        Service.__init__(self, "OrderLines", OrderLines)

class OrderService(Service):
    def __init__(self):
        Service.__init__(self, "Orders", Orders)

class PeopleService(Service):
    def __init__(self):
        Service.__init__(self, "People", People)

class StockItemHoldingService(Service):
    def __init__(self):
        Service.__init__(self, "StockItemHoldings", StockItemHoldings)

class StockItemService(Service):
    def __init__(self):
        Service.__init__(self, "StockItems", StockItems)

class StockItemTransactionService(Service):
    def __init__(self):
        Service.__init__(self, "StockItemTransactions", StockItemTransactions)

