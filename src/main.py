# Intentionally Vulnerable Example Code (FOR EDUCATION ONLY)
# Do NOT use in production.

import os
import sqlite3

# ❌ Hardcoded secret (Credential Exposure)
API_KEY = "123456-SECRET-KEY"

def connect_to_db():
    # ❌ Using user-controlled path (Path Traversal)
    db_path = input("Enter database name: ")  
    conn = sqlite3.connect(db_path)  
    return conn

def insecure_login(conn):
    username = input("Username: ")
    password = input("Password: ")

    cursor = conn.cursor()

    # ❌ SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Login successful!")
    else:
        print("Invalid credentials")

def read_file():
    # ❌ Arbitrary file read (Path Traversal)
    filename = input("Enter filename to read: ")
    with open(filename, "r") as f:
        print(f.read())

def run_calculator():
    print("Simple Calculator")
    print("1.Add 2.Sub 3.Mul 4.Div")
    choice = input("Enter choice: ")

    # ❌ No input validation
    num1 = float(input("Num1: "))
    num2 = float(input("Num2: "))

    # ❌ Division by zero crash
    if choice == "4":
        print(num1 / num2)
    else:
        print("Result:", num1 + num2)

def insecure_system_call():
    # ❌ Command Injection
    cmd = input("Enter a command to run: ")
    os.system(cmd)

def main():
    print("1.Login 2.Read File 3.Calculator 4.Run Command")
    option = input("Choose: ")

    if option == "1":
        conn = connect_to_db()
        insecure_login(conn)
    elif option == "2":
        read_file()
    elif option == "3":
        run_calculator()
    elif option == "4":
        insecure_system_call()
    else:
        print("Invalid choice")

main()
