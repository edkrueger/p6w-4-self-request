from flask import Flask, jsonify, render_template
import csv
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    # in real life, this would be readind from a database
    with open("owid-covid-2020-11-19-usa.csv") as file:
        dict_reader = csv.DictReader(file)
        return jsonify(list(dict_reader))

if __name__ == "__main__":
    app.run(debug=True)