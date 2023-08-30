"""
importing flask and initiating it
"""

from flask import Flask

"""
calling the routes
"""

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello HBNB!</p>"