# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h1 style='text-align:center;margin:20px;'>Greetings from Linux Academy!</h1>"
    return html

if __name__ == "__main__":
