correct_username_kdm = "admin"
correct_password_kdm = "1234"
attempts = 0
while attempts < 3:
    username_kdm = input("Enter username: ")
    password_kdm = input("Enter password: ")
    if username_kdm == correct_username_kdm and password_kdm == correct_password_kdm:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
    attempts += 1
if attempts == 3:
    print("Account Locked")
    # Montes, Karen