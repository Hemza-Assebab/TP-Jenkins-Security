from flask import Flask, request
import subprocess

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route("/ping")
def ping():
    host = request.args.get("host")

    # VULNERABLE CODE (Command Injection)
    result = subprocess.getoutput("ping -c 1 " + host)

    return result

if __name__ == "__main__":
    app.run(debug=True)