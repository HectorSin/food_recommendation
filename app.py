import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def getResult():
    return render_template('result.html')

app.run(port=5001, debug=True)