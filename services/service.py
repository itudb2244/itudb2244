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
                new_object = self.object_type()
                new_object.set_data(row)
                object_list.append(new_object)

        return object_list
        

class CustomerService(Service):
    def __init__(self):
        Service.__init__(self, "CUSTOMERS", type(Customer()))

class PeopleService(Service):
    def __init__(self):
        Service.__init__(self, "PEOPLE", type(People()))

