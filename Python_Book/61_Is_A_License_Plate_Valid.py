# In a particular jurisdiction, older license plates consits of three uppercase letters 
# followed by three digits.
# When all of the license plates following that pattern had been used, the format was changed
# to four digits followed by three uppercase letters.
# This program determines if the license plate is new or old format.

plate = input("Please enter your license plate: ")

if len(plate) == 6 and plate[:3].isalpha() and plate[3:].isdigit():
    print(f"This license plate {plate} is of old format.")
elif len(plate) == 7 and plate[:4].isdigit() and plate[4:].isalpha():
    print(f"This license plate {plate} is of new format.")
else:
    print("Error: Invalid license plate format.")