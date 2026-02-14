print("Login System")
corrrect_username = "jhaye_012607"
correct_password = "Jhaye012607"

username = (input("Enter username: "))
password = (input("Enter password: "))

if username == corrrect_username:
    if password == correct_password:
        print("Welcome! Login Succesful.")
    else:
        print("Inccorect Password")
else:
    print("Username Not Found")
