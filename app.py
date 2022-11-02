from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route("/")
def index():
    a = 5
    return render_template("index.html", text="Heyyyyyyyyyyy", a=a)

@app.route("/upload-file", methods=['GET','POST'])
def upload():
    if request.method == "POST":
        #f_name = request.form.get()
        #f = request.files.get("json_file")
        f = request.files["json_file"]
        a = json.load(f)
        print(a)
        return redirect("/")
    else:        
        return render_template("upload.html")
