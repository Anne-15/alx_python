"""
importing flask and initiating it
"""

from flask import Flask
from markupsafe import escape

"""
calling the routes
"""

app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<string:text>", strict_slashes=False)
def hbnb(text):
    return f'C, {escape(text)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)