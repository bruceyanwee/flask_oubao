# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
app = Flask(__name__)

@app.route("/test")
def test():
    return "this just a test for uni-app with flask on cloud"

@app.route("/hi")
def say_hi():
    return "hi"
app.run()