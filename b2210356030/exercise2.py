email = input("Enter your email: ")
if "@" in email:
    if "." in email:
        print("Valid email")
    else:
        print("Invalid email")
else:
    print("Invalid email")