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
    app.add_url_rule("/customers/add-customer", endpoint="Customers_add", view_func=views.CustomerTable().add_row,  methods=["POST"])
    app.add_url_rule("/customers/delete-customer", endpoint="Customers_delete", view_func=views.CustomerTable().delete_row, methods=["GET", "POST"])
    # app.add_url_rule("/customers/update-customer-view", endpoint="Customers_update_view", view_func=views.CustomerTable().update_row_view, methods=["GET", "POST"])
    app.add_url_rule("/customers/update-customer", endpoint="Customers_update", view_func=views.CustomerTable().update_row, methods=["GET", "POST"])
    # app.add_url_rule("/customer/<int:id>", endpoint="Customers_get", view_func=views.get_customer, methods=["GET", "POST"])


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
