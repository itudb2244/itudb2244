
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")

def table():
    return render_template("index.html")
    
