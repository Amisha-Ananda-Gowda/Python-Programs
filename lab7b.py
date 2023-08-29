def Authenitcate_Password(input):
    has_letter = False
    has_number = False
    
    for x in input:
      if x.isalnum():
        if x.isalpha():
          has_letter = True
        elif x.isnumeric():
          has_number = True
      else: 
        return False
    if has_letter and has_number:
      return True    
    else:
      return False


while True:
    # Prompt the user for their phone number
    phone_number = input("Please enter your 10-digit phone number (numbers only): ")

    # Validate the phone number
    if len(phone_number) == 10 and phone_number.isdigit():
        print("valid phone number")
        break  # Valid phone number, exit the loop
    else:
        print("Invalid phone number. Please enter 10 digits only.")

while True:
    # Prompt the user for their password
    password = input("Please enter your password (at least 8 characters, letters and numbers only): ")
    # Validate the password
    if len(password) >= 8 and Authenitcate_Password(password):
      print("valid password")
      break
    else:
        print("Invalid password. Please enter at least 8 characters with letters and numbers only.")