from flask import Flask, request
import os

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/")
def index():
    return "Hello Jenkins DevSecOps"

@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()

if __name__ == "__main__":
    app.run()