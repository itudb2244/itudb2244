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
    customer = service.get_rows_by_column(id, "CustomerID")
    return render_template("generic_list.html", title="Get Customer", table=customer)

def add_customers_page():
    return render_template("customers.html")



def customer_transactions_page():
    service = CustomerTransactionService()
    customer_transactions = service.get_data()
    return render_template("customers.html", title="Customer Transactions", table=customer_transactions)

def get_customer_transactions(id):
    service = CustomerTransactionService()
    customer_transaction = service.get_rows_by_column(id, "CustomerTransactionID")
    return render_template("customers.html", title="Get Customer Transaction", table=customer_transaction)
def people_page():
    service = PeopleService()
    people = service.get_data()
    
    return render_template("generic_list.html", title="People", peoples=people)

def add_people_page():
    
    return render_template("AddPeople.html")


def customer_transactions_page():
    
    return render_template("generic_list.html")
    service = CustomerTransactionService()
    customer_transactions = service.get_data()
    return render_template("customers.html", title="Customer Transactions", table=customer_transactions)

def get_customer_transactions(id):
    service = CustomerTransactionService()
    customer_transaction = service.get_rows_by_column(id, "CustomerTransactionID")
    return render_template("customers.html", title="Get Customer Transaction", table=customer_transaction)

def add_customer_transactions_page():
    return render_template("customers.html")



def invoice_lines_page():
    service = InvoiceLineService()
    invoice_lines = service.get_data()
    return render_template("customers.html", title="Invoice Lines", table=invoice_lines)

def get_invoice_line(id):
    service = InvoiceLineService()
    invoice_line = service.get_rows_by_column(id, "InvoiceLineID")
    return render_template("customers.html", title="Get Invoice Line", table=invoice_line)

def add_invoice_lines_page():
    return render_template("AddInvoiceLines.html")



def invoices_page():
    service = InvoiceService()
    invoices = service.get_data()
    return render_template("customers.html", title="Invoices", table=invoices)

def get_invoice(id):
    service = InvoiceService()
    invoice = service.get_rows_by_column(id, "InvoiceID")
    return render_template("customers.html", title="Get Invoice", table=invoice)

def add_invoices_page(): 
    return render_template("AddInvoices.html")



def order_lines_page():
    service = OrderLineService()
    order_lines = service.get_data()
    return render_template("customers.html", title="Order Lines", table=order_lines)

def get_order_line(id):
    service = OrderLineService()
    order_line = service.get_rows_by_column(id, "OrderLineID")
    return render_template("customers.html", title="Get Order Line", table=order_line)

def add_order_lines_page():
    
    return render_template("AddOrderLines.html")


def orders_page():
    service = OrderService()
    orders = service.get_data()
    return render_template("customers.html", title="Orders", table=orders)

def get_order(id):
    service = OrderService()
    order = service.get_rows_by_column(id, "OrderID")
    return render_template("customers.html", title="Get Order", table=order)

def add_orders_page():
    
    return render_template("AddOrders.html")




def people_page():
    service = PeopleService()
    people = service.get_data()
    return render_template("customers.html", title="People", table=people)

def get_person(id):
    service = PeopleService()
    person = service.get_rows_by_column(id, "PersonID")
    return render_template("customer.html", title="Get Person", table=person)

def add_people_page():
    return render_template("AddPeople.html")



def stockitem_holdings_page():
    service = StockItemHoldingService()
    stockitem_holdings = service.get_data()
    return render_template("customers.html", title="Stock Item Holdings", table=stockitem_holdings)

def get_stockitem_holding(id):
    service = StockItemHoldingService()
    stockitem_holding = service.get_rows_by_column(id, "StockItemHoldingID")
    return render_template("customer.html", title="Get Stock Item Holding", table=stockitem_holding)

def add_stockitem_holdings_page():
    
    return render_template("AddStockItemHoldings.html")



def stockitems_page():
    service = StockItemService()
    stockitems = service.get_data()
    return render_template("customers.html", title="Stock Items", table=stockitems)

def get_stockitem(id):
    service = StockItemService()
    stockitem = service.get_rows_by_column(id, "StockItemID")
    return render_template("customer.html", title="Get Stock Item", table=stockitem)

def add_stockitems_page():
    
    return render_template("AddStockItems.html")



def stockitem_transactions_page():
    service = StockItemTransactionService()
    stockitem_transactions = service.get_data()
    return render_template("customers.html", title="Stock Item Transactions", table=stockitem_transactions)

def get_stockitem_transaction(id):
    service = StockItemTransactionService()
    stockitem_transaction = service.get_rows_by_column(id, "StockItemTransactionID")
    return render_template("customer.html", title="Get Stock Item Transaction", table=stockitem_transaction)

def add_stockitem_transactions_page():
    
    return render_template("AddStockItemTransactions.html")









