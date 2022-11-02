from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route("/")
def index():
    a = 5
    return render_template("index.html", text="Heyyyyyyyyyyy", a=a)

@app.route("/upload-file", methods=['GET','POST'])
def upload():
    err = ""
    if request.method == "POST":
        f = request.files["json_file"]
        if f is None:
            err = "Error: No file provided"
        elif f.filename[-5:] not in [".json", ".JSON"]:
            err = "Error: File need to be of json format"
        else:
            a = json.load(f)
            # print(a)
        return render_template("upload.html", err=err)
    else:        
        return render_template("upload.html", err=err)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    filter = request.form['filterString']
    #Filter String will look like "Filter1:Filter2:Filter3" which can be parsed to create Sql String
    return render_template("index.html", filterString = filter)
