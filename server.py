from flask import Flask
import views
from subprocess import call
import db_updated_check

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    #CustomerTable = views.CustomerTable()
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/customers", view_func=views.CustomerTable().get_table, methods=["GET","POST"])
    app.add_url_rule("/people", view_func=views.people_page,methods=["GET","POST"])
    app.add_url_rule("/customer-transactions", view_func=views.customer_transactions_page,methods=["GET","POST"])
    app.add_url_rule("/invoice-lines", view_func=views.invoice_lines_page,methods=["GET","POST"])
    app.add_url_rule("/invoices", view_func=views.invoices_page,methods=["GET","POST"])
    app.add_url_rule("/order-lines", view_func=views.order_lines_page,methods=["GET","POST"])
    app.add_url_rule("/orders", view_func=views.orders_page,methods=["GET","POST"])
    app.add_url_rule("/stockitem-holdings", view_func=views.stockitem_holdings_page,methods=["GET","POST"])
    app.add_url_rule("/stockitems", view_func=views.stockitems_page,methods=["GET","POST"])
    app.add_url_rule("/stockitem-transactions", view_func=views.stockitem_transactions_page,methods=["GET","POST"])


    app.add_url_rule("/people/add-people", view_func=views.add_people_page,methods=["GET","POST"])
    app.add_url_rule("/customers/add-customer", view_func=views.add_customers_page,  methods=["GET","POST"])
    app.add_url_rule("/customer-transactions/add-customer-transactions", view_func=views.add_customer_transactions_page,methods=["GET","POST"])
    app.add_url_rule("/invoice-lines/add-invoice-lines", view_func=views.add_invoice_lines_page,methods=["GET","POST"])
    app.add_url_rule("/invoices/add-invoices", view_func=views.add_invoices_page,methods=["GET","POST"])
    app.add_url_rule("/order-lines/add-order-lines", view_func=views.add_order_lines_page,methods=["GET","POST"])
    app.add_url_rule("/orders/add-orders", view_func=views.add_orders_page,methods=["GET","POST"])
    app.add_url_rule("/stockitem-holdings/add-stockitem-holdings", view_func=views.add_stockitem_holdings_page,methods=["GET","POST"])
    app.add_url_rule("/stockitems/add-stockitems", view_func=views.add_stockitems_page,methods=["GET","POST"])
    app.add_url_rule("/stockitem-transactions/add-stockitem-transactions", view_func=views.add_stockitem_transactions_page,methods=["GET","POST"])


    app.add_url_rule("/customer/<int:id>", view_func=views.get_customer, methods=["GET", "POST"])

    app.config["dbname"] = "import_test.db"

    return app

def create_db():
    if not (db_updated_check.database_date_check()):
        rc = call("./import_tables.sh")

if __name__ == "__main__":
    # create_db() ################COMMENT to disable DB creation at every run
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(port=port)
