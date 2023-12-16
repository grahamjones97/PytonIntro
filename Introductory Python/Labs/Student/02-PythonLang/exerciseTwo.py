def exercsie_2():
    honorific = input("What is your Honorific? ").upper()
    firstName = input("What is your First Name? ").title()
    lastName = input("What is your Last Name? ").title()
    email = input("What is your emai? ")
    pincode = input("Enter a 4 digit code: ")

    fullname = honorific + "." + " " + firstName + " " + lastName

    print(fullname)

    if "@" not in email:
        print("Not valid email")
    else:
        print(email)

    if len(pincode) == 4 and pincode.isdigit():
        print(f"Your pin is: {pincode}")
    else:
        print("not vailid pincode")


if __name__ == "__main__":
    exercsie_2()
