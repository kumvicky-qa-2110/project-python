
password = "vicky123"
enter_password = input("Enter your password: ")

while enter_password != password:
    print("incorrect password, try again.")
    enter_password = input("Enter your password: ")
print("correct password, welcome back!")

