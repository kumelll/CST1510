
password = input("Enter your password: ")

if len(password) < 8:
    print("Weak")
elif len(password) < 12:
    print("Moderate")
else:
    print("Strong")
