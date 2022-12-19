from flask import current_app, redirect, url_for, request
import sqlite3
from models import *

class Service():
    def __init__(self, table, object_type):
        self.table = table
        self.object_type = object_type

    def get_data(self, page, sort_by=None):
        max_row = 1000
        row_num_query = 'SELECT COUNT("' + self.object_type.getColumns()[0] + '") FROM ' + self.table

        object_list = []
        try:
            with sqlite3.connect(current_app.config["dbname"]) as connection:
                cursor = connection.cursor()

                num = 1
                
                row_num = cursor.execute(row_num_query)
                for i in row_num:
                    num = i[0]
                
                if page > num // max_row:
                    page = num // max_row + 1

                query = 'SELECT * FROM ' + self.table

                if sort_by is not None:
                    query += " ORDER BY "+sort_by+" ASC"

                query += " LIMIT " + str(max_row) + " OFFSET " + str((page-1)*max_row)

                print(query)

                res = cursor.execute(query)
                for row in res:
                    new_object = self.object_type(row)
                    object_list.append(new_object)
                return object_list
        except Exception as e:
            print(e)
            return []

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
        dict_data = data.toDict()

        # "UPDATE Customers SET CustomerName=Eymen, WebsiteURL=eymen.com"
        query = "UPDATE "+self.table+" SET "

        columns = self.object_type.getColumns()
        for i,column in enumerate(columns):
            if column in self.object_type.getNonKeyColumns():
                query += column + '="' + dict_data[column] + '"'
                if i != len(columns)-1:
                    query += ", "
        query += " WHERE (" + idColumn + " = " + str(id) + ")"

        try:
            with sqlite3.connect(current_app.config["dbname"]) as connection:
                cursor = connection.cursor()
                cursor.execute(query)
                return True
        except Exception as e:
            print(e)
            return False

    def search_and_list(self, dictionary):
        query = "SELECT * FROM " + self.table + " WHERE(("

        # SELECT * FROM Customers WHERE(id=5 AND (CustomerName LIKE "%esat%") AND id2=5)

        for i, key in enumerate(dictionary):
            if dictionary[key].isnumeric():
                print(dictionary[key])
                query += key + "=" + dictionary[key]
            else:
                query += key + " LIKE " + '"%' + dictionary[key] + '%"'
            if i != len(dictionary)-1:
                query += ") AND ("

        query += "))"

        print(query)

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
            return []


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
