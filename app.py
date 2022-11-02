from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    a = 5
    return render_template("index.html", text="Heyyyyyyyyyyy", a=a)
