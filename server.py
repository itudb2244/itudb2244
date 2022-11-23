from flask import Flask
import views

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/customers", view_func=views.customers_page)

    app.config["dbname"] = "import_test.db"

    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(port=port)