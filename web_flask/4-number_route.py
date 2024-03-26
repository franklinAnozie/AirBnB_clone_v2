#!/usr/bin/python3
""" Flask web app """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ hello hbnb """
    return f"Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hello hbnb """
    return f"HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_msg(text):
    """ the c route that accepts url args """
    new_text = text.replace("_", " ")
    return f"C {new_text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_msg(text="is_cool"):
    """ the c route that accepts url args """
    new_text = text.replace("_", " ")
    return f"Python {new_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def nums_n(n):
    """ display number """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
