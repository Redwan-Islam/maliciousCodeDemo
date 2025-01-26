# malicious_code.py

import os

def execute_command(command):
    os.system(command)  # This is a dangerous operation

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def eval_code(code):
    eval(code)  # This can execute arbitrary code

def main():
    print("Executing a command...")
    execute_command("ls")  # Example command

if __name__ == "__main__":
    main()
