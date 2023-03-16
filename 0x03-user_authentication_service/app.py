#!/usr/bin/env pthon3
"""
Flask App
"""
from flask import Flask, jsonify
app = Flask(__name__)
AUTH = Auth()
@app.route('/', methods=['GET'], strict_slashes=False)
def basic() -> str:
    """ 
    returns a basic json response
    """
    return jsonify({"message": "Bienvenue"})
if __name__ == "__main__":
        app.run(host="0.0.0.0", port="5000")

