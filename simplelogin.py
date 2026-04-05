import os

def log_attempt(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Attempt made...")
        return func(*args, **kwargs)
    return wrapper

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("Registered successfully!")

@log_attempt
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open("users.txt", "r") as f:
            for line in f:
                saved_user, saved_pass = line.strip().split(",")
                if username == saved_user and password == saved_pass:
                    print(f"Welcome, {username}!")
                    return
        print("Invalid username or password!")
    except FileNotFoundError:
        print("No users found. Please register first!")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")