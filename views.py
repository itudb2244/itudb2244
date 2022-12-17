from flask import current_app, render_template, request, redirect, url_for
import services.customer_service as customerService

from services.service import *

class Table():
    def __init__(self, type, service, data_class):
        self.type = type
        self.service = service
        self.data_class = data_class

    def get_table(self):
        service = self.service()
        data = service.get_data()
        return render_template("generic_list.html", title=self.type, table=data)

    def add_row(self):
        row = []
        columns = self.data_class.getColumns()
        for column in columns:
            if column in self.data_class.getNonKeyColumns():
                row.append(request.form[column])
            else:
                row.append(-1)

        obj = self.data_class(row)

        service = self.service()
        service.add_row(obj)

        return redirect(url_for(self.type + "_page"))

    def delete_row(self):
        idString = request.args.get("id")
        id = idString.split("'")[1]

        idColumn = self.data_class.getColumns()[0]

        service = self.service()
        service.delete_row(id, idColumn)

        return redirect(url_for(self.type + "_page"))

        


class CustomerTable(Table):
    def __init__(self):
        super().__init__("Customers", CustomerService, Customer)
        

def home_page():
    return render_template("home.html")


def customers_page():
    service = CustomerService()
    customers = service.get_data()
    return render_template("generic_list.html", title="Customers", table=customers)

def get_customer(id):
    service = CustomerService()
    customer = service.get_rows_by_column(id, "CustomerID")
    return render_template("generic_list.html", title="Get Customer", table=customer)

def add_customers_page():
    customerName = request.form["CustomerName"]
    phoneNumber = request.form["PhoneNumber"]
    websiteURL = request.form["WebsiteURL"]
    deliveryAddressLine1 = request.form["DeliveryAddressLine1"]
    deliveryAddressLine2 = request.form["DeliveryAddressLine2"]
    customer = Customer((-1, customerName, -1, phoneNumber, websiteURL, deliveryAddressLine1, deliveryAddressLine2))

    service = CustomerService()
    service.add_row(customer)

    customers = service.get_data()
    return redirect(url_for("Customers_page"))
        