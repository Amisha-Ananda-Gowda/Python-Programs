def authenticatePassword(input):
    has_letter=False
    has_number=False
    for x in input:
        if x.isalnum():
            if x.isalpha():
                has_letter=True
            elif x.isnumeric():
                has_number=True
        else:
            return False
    if has_letter and has_number:
        return True
    else:
        return False
while True:
    phone=input("Enter your phone number (10 digits)")
    if len(phone)==10 and phone.isdigit():
        print("Phone number valid")
        break
    else:
        print("Invalid phone number. Enter 10 digits only")
while True:
    pswd=input("Enter yor password (atleast 8 characters numbers and letters only)")
    if len(pswd)>=8 and authenticatePassword(pswd):
        print("Valid password")
        break
    else:
        print("Invalud password. Enter atleast 8 characters numbers and letters only ")