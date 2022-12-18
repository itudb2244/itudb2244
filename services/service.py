from flask import current_app, redirect, url_for, request
import sqlite3
from models import *

class Service():
    def __init__(self, table, object_type):
        self.table = table
        self.object_type = object_type

    def get_data(self):
        query = 'SELECT * FROM ' + self.table
        object_list = []

        try:
            with sqlite3.connect(current_app.config["dbname"]) as connection:
                cursor = connection.cursor()
                res = cursor.execute(query)
                for row in res:
                    new_object = self.object_type(row)
                    object_list.append(new_object)
                return object_list
        except:
            return False

    def get_rows_by_column(self, id, column):
        query = 'SELECT * FROM '+self.table+' WHERE('+self.table+'.'+column+' = {})'.format(id)
        object_list = []
        
        try:
            with sqlite3.connect(current_app.config["dbname"]) as connection:
                cursor = connection.cursor()
                res = cursor.execute(query)
                for row in res:
                    new_object = self.object_type(row)
                    object_list.append(new_object)
                return object_list
        except:
            return None

    def add_row(self, obj):
        columns = self.object_type.getNonKeyColumns()

        query = 'INSERT INTO '+self.table+'('
        for i,column in enumerate(columns):
            query += column
            if i != len(columns) - 1:
                query += ', '

        query += ') VALUES('

        dictionary = obj.toDict()
        keys = dictionary.keys()

        for i,key in enumerate(keys):
            if key in columns:
                query += '"' + dictionary[key] + '"'
                if i != len(keys) - 1:
                    query += ', '
        
        query += ')'

        try:
            with sqlite3.connect(current_app.config["dbname"]) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                return True
        except:
            return False

    def delete_row(self, id, idColumn):
        query = "DELETE FROM "+self.table+" WHERE("+idColumn+" = "+str(id)+")"

        try:
            with sqlite3.connect(current_app.config["dbname"]) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                
                return True
        except:
            return False

    def update_row(self, data, id , idColumn):
        column_datas = data.toDict().values()

        # "UPDATE Customers SET CustomerName=Eymen, WebsiteURL=eymen.com"
        query = "UPDATE "+self.table+" SET "

        columns = self.object_type.getColumns()
        for i,column in enumerate(columns):
            if column in self.object_type.getNonKeyColumns():
                query += column + "=" + column_datas[i]
                if i != len(columns)-1:
                    query += ", "
        query += " WHERE (" + idColumn + " = " + str(id)

        print(query)

        try:
            with sqlite3.connect(current_app.config["dbname"]) as connection:
                cursor = connection.cursor()
                cursor.execute(query)

                return True
        except:
            return False



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
