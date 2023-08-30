"""
importing flask and initiating it
"""
from flask import Flask

"""
calling the routes
"""
app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

"""
dynamic routing with default values
"""
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

"""
dynamic routing with default values
"""
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace("_", " "))

"""
dynamic routing with default values
"""
@app.route('/python/', defaults={"text" | "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python {}".format(text.replace("_", " "))

"""
starting the server
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
