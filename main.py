# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
from flask import Flask,jsonify,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/test")
def test():
    return jsonify({"text":"this just a test for uni-app with flask on cloud"}) 

@app.route("/hi")
def say_hi():
    return "hi"
@app.route('/upload')
def upload_res():
    pass
app.run(host="0.0.0.0")