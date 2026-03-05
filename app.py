from flask import Flask, request
import subprocess

app = Flask(__name__)

def add(a, b):
    return a + b


@app.route("/")
def index():
    return "Hello Jenkins DevSecOps"


# Vulnerable endpoint (command injection)
@app.route("/run")
def run_command():
    cmd = request.args.get("cmd")
    result = subprocess.getoutput(cmd)  # unsafe execution
    return result


if __name__ == "__main__":
    app.run(debug=True)