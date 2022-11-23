from flask import current_app, render_template
import services.consumer_service as consumerService

def home_page():
    return render_template("home.html")

def consumers_page():
    consumers = consumerService.get_consumers()
    return render_template("consumers.html", consumers=consumers)