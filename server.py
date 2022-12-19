from flask import Flask
import views
from subprocess import call
import db_updated_check
#url rules created for each table
def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    customersView = views.CustomerTable()
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/customers/<int:page>", endpoint="Customers_page", view_func=customersView.get_table, methods=["GET","POST"])
    app.add_url_rule("/customers/add", endpoint="Customers_add", view_func=customersView.add_row,  methods=["POST"])
    app.add_url_rule("/customers/delete", endpoint="Customers_delete", view_func=customersView.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/customers/update", endpoint="Customers_update", view_func=customersView.update_row, methods=["GET", "POST"])
    app.add_url_rule("/customers/search", endpoint="Customers_search", view_func=customersView.search, methods=["GET", "POST"])
   
    invoicesView = views.InvoicesTable()
    app.add_url_rule("/invoices/<int:page>", endpoint="Invoices_page", view_func=invoicesView.get_table, methods=["GET","POST"])
    app.add_url_rule("/invoices/add", endpoint="Invoices_add", view_func=invoicesView.add_row,  methods=["POST"])
    app.add_url_rule("/invoices/delete", endpoint="Invoices_delete", view_func=invoicesView.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/invoices/update", endpoint="Invoices_update", view_func=invoicesView.update_row, methods=["GET", "POST"])
    app.add_url_rule("/invoices/search", endpoint="Invoices_search", view_func=invoicesView.search, methods=["GET", "POST"])

    invoiceLinesView = views.InvoiceLinesTable()
    app.add_url_rule("/invoice-lines/<int:page>", endpoint="InvoiceLines_page", view_func=invoiceLinesView.get_table, methods=["GET","POST"])
    app.add_url_rule("/invoice-lines/add", endpoint="InvoiceLines_add", view_func=invoiceLinesView.add_row,  methods=["POST"])
    app.add_url_rule("/invoice-lines/delete", endpoint="InvoiceLines_delete", view_func=invoiceLinesView.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/invoice-lines/update", endpoint="InvoiceLines_update", view_func=invoiceLinesView.update_row, methods=["GET", "POST"])
    app.add_url_rule("/invoice-lines/search", endpoint="InvoiceLines_search", view_func=invoiceLinesView.search, methods=["GET", "POST"])

    ordersView = views.OrdersTable()
    app.add_url_rule("/orders/<int:page>", endpoint="Orders_page", view_func=ordersView.get_table, methods=["GET","POST"])
    app.add_url_rule("/orders/add", endpoint="Orders_add", view_func=ordersView.add_row,  methods=["POST"])
    app.add_url_rule("/orders/delete", endpoint="Orders_delete", view_func=ordersView.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/orders/update", endpoint="Orders_update", view_func=ordersView.update_row, methods=["GET", "POST"])
    app.add_url_rule("/orders/search", endpoint="Orders_search", view_func=ordersView.search, methods=["GET", "POST"])

    customerTransactionView = views.CustomerTransactionsTable()
    app.add_url_rule("/customer-transactions/<int:page>", endpoint="CustomerTransactions_page", view_func=customerTransactionView.get_table, methods=["GET","POST"])
    app.add_url_rule("/customer-transactions/add", endpoint="CustomerTransactions_add", view_func=customerTransactionView.add_row,  methods=["POST"])
    app.add_url_rule("/customer-transactions/delete", endpoint="CustomerTransactions_delete", view_func=customerTransactionView.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/customer-transactions/update", endpoint="CustomerTransactions_update", view_func=customerTransactionView.update_row, methods=["GET", "POST"])
    app.add_url_rule("/customer-transactions/search", endpoint="CustomerTransactions_search", view_func=customerTransactionView.search, methods=["GET", "POST"])

    orderLinesView = views.OrderLinesTable()
    app.add_url_rule("/order-lines/<int:page>", endpoint="OrderLines_page", view_func=orderLinesView.get_table, methods=["GET","POST"])
    app.add_url_rule("/order-lines/add", endpoint="OrderLines_add", view_func=orderLinesView.add_row,  methods=["POST"])
    app.add_url_rule("/order-lines/delete", endpoint="OrderLines_delete", view_func=orderLinesView.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/order-lines/update", endpoint="OrderLines_update", view_func=orderLinesView.update_row, methods=["GET", "POST"])
    app.add_url_rule("/order-lines/search", endpoint="OrderLines_search", view_func=orderLinesView.search, methods=["GET", "POST"])

    peopleView = views.PeopleTable()
    app.add_url_rule("/people/<int:page>", endpoint="People_page", view_func=peopleView.get_table, methods=["GET","POST"])
    app.add_url_rule("/people/add", endpoint="People_add", view_func=peopleView.add_row,  methods=["POST"])
    app.add_url_rule("/people/delete", endpoint="People_delete", view_func=peopleView.delete_row, methods=["GET", "POST"])
    app.add_url_rule("/people/update", endpoint="People_update", view_func=peopleView.update_row, methods=["GET", "POST"])
    app.add_url_rule("/people/search", endpoint="People_search", view_func=peopleView.search, methods=["GET", "POST"])

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
