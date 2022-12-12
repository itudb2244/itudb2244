from flask import Flask
import views
from subprocess import call
import db_updated_check

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/customers", view_func=views.customers_page)

    app.config["dbname"] = "import_test.db"

    return app

def create_db():
    if db_updated_check.database_date_check():
        rc = call("./import_tables.sh")

if __name__ == "__main__":
    create_db()
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(port=port)
