# In a particular jurisdiction, older license plated consist of three letters
# followed by three digits. When all of the license plates following that pattern have been used,
# the format was changed to four digits followed by three letters.
# This program generates random license plate, approximately equal odds of generating a sequence
# of characters for an old license plate or a new license plate.

# old: ABC123
# new: 1234ABC
# ASCII from A to Z 65 to 90


from random import randint

old_plate = 1
new_plate = 2

def random_license_plate():
    random_choice = randint(old_plate, new_plate)
    if random_choice == old_plate:
        result_numbers = ""
        result_letters = ""
        result = ""
        for i in range(3):
            result_numbers += str(randint(0, 9))
        for j in range(3):
            result_letters += chr(randint(65, 90))
        result = result_letters + result_numbers
    elif random_choice == new_plate:
        result_numbers = ""
        result_letters = ""
        result = ""
        for i in range(4):
            result_numbers += str(randint(0, 9))
        for j in range(3):
            result_letters += chr(randint(65, 90))
        result = result_numbers + result_letters
    return result


def main():
    print(f"Your random licence plate is {random_license_plate()}. ")

if __name__ == "__main__":
    main()



