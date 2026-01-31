from flask import Flask, jsonify, render_template, request
from DepopCalc import program
app = Flask(__name__)


@app.route("/", methods =['GET', 'POST']) 
def home(): 
    return render_template('index.html')