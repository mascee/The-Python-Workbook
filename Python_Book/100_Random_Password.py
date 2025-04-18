# This program is for writing random passwords
# The passwords should have a random length of between 7 and 10 characters.
# Each character should be randomly selected from positions 33 to 126
# in the ASCII table.

from random import randint

short_password = 7
long_password = 10
MIN_ASCII = 33
MAX_ASCII = 126

def random_password():
    random_length = randint(short_password, long_password)
    result = ""
    for i in range(random_length):
        random_char = chr(randint(MIN_ASCII, MAX_ASCII))
        result += random_char
    return result

def main():
    print(f"Your random password is {random_password()}. ")

if __name__ == "__main__":
    main()
