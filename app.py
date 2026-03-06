import os

def add(a, b):
    return a + b

# VULNERABLE FUNCTION (command injection)
def run_command(user_input):
    os.system("echo " + user_input)