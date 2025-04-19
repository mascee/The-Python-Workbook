# This program determines if the password is good.
# Requirements: password should be at least 8 characters long and contains at least one uppercase letter,
# at least one lowercase letter, and at least one number.
# The function returns True if the password passed to it as its only parameter is good.
# Otherwise returns False.



def is_password_good(password):
    HAS_NUMBER = False
    HAS_LOWER = False
    HAS_UPPER = False

    for i in password:
        if i.isupper():
            HAS_UPPER = True
        elif i.islower():
            HAS_LOWER = True
        elif i.isdigit():
            HAS_NUMBER = True
    if len(password)>= 8 and HAS_NUMBER and HAS_LOWER and HAS_UPPER:
        return True
    else:
        return False
    
def main():
    password = input("Enter your password. It should be at least 8 characters, with at least one uppercase letter, one number: ")
    if is_password_good(password):
        print("Your password is good. ")
    else:
        print("Your password doesn't fit the requirements. ")


if __name__ == "__main__":
    main()

