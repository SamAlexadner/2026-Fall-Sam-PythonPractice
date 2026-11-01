def main():
    password = input("Enter a password:").strip()
    if check_length_password(password):  # if check_lenth_password = True that means the password is passed length test.
        if check_password_contain(password):  # if check_password_contain = True that means the password is valid.
            print("Password is valid")
        else:
            print("Password is invalid")
    else:
        print("Password is invalid")
    
def check_length_password(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")  
        return False
    return True
    
def check_password_contain(password):
    has_upper = False
    for i in password:  # check the word  
        if i.isupper():  # is upper letter?
            has_upper = True  # is upper letter = True
    
    has_lower = False
    for i in password:  # check the word  
        if i.islower():  # is lower letter?
            has_lower = True  # is lower letter = True
    
    has_digit = False
    for i in password:  # check the word  
        if i.isdigit():  # is digit?
            has_digit = True  # is digit = True
    
    if not (has_upper and has_lower and has_digit and password.isalnum()):
        print("Password must contain at least one uppercase letter, "
              "one lowercase letter, and a digit, "
              "and may only contain letters and digits.")
        return False  # return False value to passeord
    return True  

if __name__ == '__main__':
    main()

