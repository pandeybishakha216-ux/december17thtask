#Python program to check the validity of username and password input by users
valid_username = "admin"
valid_password = "password123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == valid_username and password == valid_password:
    print("Login successful!")
else:
    print("Invalid username or password.")
    