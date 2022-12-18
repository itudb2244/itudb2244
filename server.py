from flask import Flask
import views
from subprocess import call
import db_updated_check

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    #CustomerTable = views.CustomerTable()
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/customers", endpoint="Customers_page", view_func=views.CustomerTable().get_table, methods=["GET","POST"])
    app.add_url_rule("/customers/add", endpoint="Customers_add", view_func=views.CustomerTable().add_row,  methods=["POST"])
    app.add_url_rule("/customers/delete", endpoint="Customers_delete", view_func=views.CustomerTable().delete_row, methods=["GET", "POST"])
    app.add_url_rule("/customers/update", endpoint="Customers_update", view_func=views.CustomerTable().update_row, methods=["GET", "POST"])
    app.add_url_rule("/customers/search", endpoint="Customers_search", view_func=views.CustomerTable().search, methods=["GET", "POST"])
   
    # app.add_url_rule("/customer/<int:id>", endpoint="Customers_get", view_func=views.get_customer, methods=["GET", "POST"])
    app.add_url_rule("/invoices", endpoint="Invoices_page", view_func=views.InvoicesTable().get_table, methods=["GET","POST"])
    app.add_url_rule("/invoices/add", endpoint="Invoices_add", view_func=views.InvoicesTable().add_row,  methods=["POST"])
    app.add_url_rule("/invoices/delete", endpoint="Invoices_delete", view_func=views.InvoicesTable().delete_row, methods=["GET", "POST"])
    app.add_url_rule("/invoices/update", endpoint="Invoices_update", view_func=views.InvoicesTable().update_row, methods=["GET", "POST"])
    app.add_url_rule("/invoices/search", endpoint="Invoices_search", view_func=views.InvoicesTable().search, methods=["GET", "POST"])
  

    app.add_url_rule("/orders", endpoint="Orders_page", view_func=views.OrdersTable().get_table, methods=["GET","POST"])
    app.add_url_rule("/orders/add", endpoint="Orders_add", view_func=views.OrdersTable().add_row,  methods=["POST"])
    app.add_url_rule("/orders/delete", endpoint="Orders_delete", view_func=views.OrdersTable().delete_row, methods=["GET", "POST"])
    app.add_url_rule("/orders/update", endpoint="Orders_update", view_func=views.OrdersTable().update_row, methods=["GET", "POST"])
    app.add_url_rule("/orders/search", endpoint="Orders_search", view_func=views.OrdersTable().search, methods=["GET", "POST"])

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
