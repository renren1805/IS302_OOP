# secure_login_system.py

import hashlib
import getpass

# Sample user database
users_kdm = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "karen": hashlib.sha256("mypassword".encode()).hexdigest()
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    print("=== Secure Login System ===")

    username_kdm = input("Username: ")
    password_kdm = getpass.getpass("Password: ")

    hashed_password = hash_password(password_kdm)

    if username_kdm in users_kdm and users_kdm[username_kdm] == hashed_password:
        print("\nLogin Successful!")
        print(f"Welcome, {username_kdm}!")
    else:
        print("\nInvalid Username or Password.")

# Run the system
login()

# Montes, Karen D.