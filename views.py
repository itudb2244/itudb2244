from flask import current_app, render_template
import services.customer_service as customerService

def home_page():
    return render_template("home.html")

def customers_page():
    customers = customerService.get_customers()
    return render_template("customers.html", customers=customers)

def customer_transactions():
    customer_transactions 
