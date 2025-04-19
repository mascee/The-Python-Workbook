# Creates random password and checks if it's good.

from Random_Password import random_password
from Check_A_Password import is_password_good

def main():
    password = random_password()
    attempts = 1

    while is_password_good(password):
        password = random_password()
        attempts += 1
        print(f"Attempt {attempts}: {password} - Not good enough.")

    print(f"Password is {password}. Number of attempts: {attempts}. ")

if __name__ == "__main__":
    main()