from flask import current_app, render_template
import services.customer_service as customerService

from services.service import *

def home_page():
    return render_template("home.html")


def customers_page():
    service = CustomerService()
    customers = service.get_data()
    return render_template("generic_list.html", title="Customers", table=customers)

def get_customer(id):
    service = CustomerService()
    customers = service.get_rows_by_column(id, "CustomerID")
    return render_template("generic_list.html", title="Get Customers", table=customers)

def add_customers_page():
    return render_template("AddCustomer.html")



def people_page():
    service = PeopleService()
    people = service.get_data()
    
    return render_template("generic_list.html", title="People", peoples=people)

def add_people_page():
    
    return render_template("AddPeople.html")


def customer_transactions_page():
    
    return render_template("generic_list.html")

def add_customer_transactions_page():
    
    return render_template("AddCustomerTransactions.html")


def invoice_lines_page():
    
    return render_template("InvoiceLines.html")

def add_invoice_lines_page():
    
    return render_template("AddInvoiceLines.html")


def invoices_page():
    return render_template("Invoices.html")

def add_invoices_page():
    
    return render_template("AddInvoices.html")

def order_lines_page():
    
    return render_template("OrderLines.html")

def add_order_lines_page():
    
    return render_template("AddOrderLines.html")


def orders_page():
    
    return render_template("Orders.html")

def add_orders_page():
    
    return render_template("AddOrders.html")

def stockitem_holdings_page():
    
    return render_template("StockItemHoldings.html")

def add_stockitem_holdings_page():
    
    return render_template("AddStockItemHoldings.html")

def stockitem_transactions_page():
    
    return render_template("StockItemTransactions.html")

def add_stockitem_transactions_page():
    
    return render_template("AddStockItemTransactions.html")


def stockitems_page():
    
    return render_template("StockItems.html")

def add_stockitems_page():
    
    return render_template("AddStockItems.html")

def customer_transactions():
    customer_transactions 
