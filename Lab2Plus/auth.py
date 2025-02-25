import json
import re

USERS_FILE = "../Lab2Plus/users.json"

def load_users():
    """Load users from users.json if it exists, otherwise return an empty list."""
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(users):
    """Save users list to users.json."""
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def is_valid_egyptian_phone(phone):
    """Validate Egyptian phone number format."""
    return re.match(r"^01[0-2,5]{1}[0-9]{8}$", phone)

def register_user():
    """Register a new user."""
    users = load_users()
    
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    
    while True:
        email = input("Enter Email: ")
        if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            break
        print("Invalid email format. Try again.")
    
    while True:
        password = input("Enter Password: ")
        confirm_password = input("Confirm Password: ")
        if password == confirm_password:
            break
        print("Passwords do not match. Try again.")
    
    while True:
        phone = input("Enter Mobile Phone (Egyptian format): ")
        if is_valid_egyptian_phone(phone):
            break
        print("Invalid phone number. Try again.")
    
    users.append({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone
    })
    
    save_users(users)
    print("Registration successful!")

def login():
    """Login a user by verifying email and password."""
    users = load_users()

    while True:
        email = input("Enter Email: ")
        if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            break
        print("Invalid email format. Try again.")

    while True:
        password = input("Enter Password: ").strip()  
        if password:
            break
        print("Password cannot be empty. Try again.")

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome {user['first_name']} {user['last_name']}! 🎉")
            return True

    print("Invalid email or password. Try again.")
    return False
