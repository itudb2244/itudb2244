from flask import current_app, render_template, request, redirect, url_for
import services.customer_service as customerService

from services.service import *

class Table():
    def __init__(self, type, service, child ):
        self.type = type
        self.service = service
        self.child = child

    def get_table(self):
        service = self.service()
        data = service.get_data()
        print(request.path)
        return render_template("generic_list.html", title=type, table=data, view_class=self.child)
    def add_row(self):
        return render_template("AddCustomer.html")

class CustomerTable(Table):
    def __init__(self):
        super().__init__("Customers",CustomerService, "customers")
class PeopleTable(Table):
    def __init__(self):
        super().__init__("People", PeopleService, "customers")
        

def home_page():
    #return render_template("home.html")
    return redirect(url_for("customers_page"))


def customers_page():
    service = CustomerService()
    customers = service.get_data()
    return render_template("generic_list.html", title="Customers", table=customers)

def get_customer(id):
    service = CustomerService()
    customer = service.get_rows_by_column(id, "CustomerID")
    return render_template("generic_list.html", title="Get Customer", table=customer)

def add_customers_page():
    return render_template("customers.html")











