# login_file_system.py

import os

# File to store user data
USER_FILE = "users.txt"

def initialize_file():
    """Create the users file if it doesn't exist"""
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as file_kdm:
            pass  # Create empty file

def register():
    """Register a new user"""
    print("\n--- Register New User ---")
    username_kdm = input("Enter username: ").strip()
    password_kdm = input("Enter password: ").strip()
    
    # Check if username already exists
    with open(USER_FILE, 'r') as file_kdm:
        for line in file_kdm:
            stored_user, _ = line.strip().split(',')
            if stored_user == username_kdm:
                print("Username already exists! Please choose another.")
                return
    
    # Save new user
    with open(USER_FILE, 'a') as file_kdm:
        file_kdm.write(f"{username_kdm},{password_kdm}\n")
    
    print("Registration successful! You can now login.")

def login():
    """Login an existing user"""
    print("\n--- Login ---")
    username_kdm = input("Enter username: ").strip()
    password_kdm = input("Enter password: ").strip()
    
    # Check credentials
    with open(USER_FILE, 'r') as file_kdm:
        for line in file_kdm:
            stored_user, stored_pass = line.strip().split(',')
            if stored_user == username_kdm and stored_pass == password_kdm:
                print(f"Welcome back, {username_kdm}! Login successful.")
                return
    
    print("Invalid username or password. Please try again.")

def main():
    """Main menu loop"""
    initialize_file()
    
    while True:
        print("\n=== Login System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()