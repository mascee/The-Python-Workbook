# Exercise 140. Postal Codes.
# This program reads a postal Canadian Code from the user and displays
# the province or territory associated with it, along with whether the address is urban or rural.
# "0" is for rural, otherwise it's urban.

from Reverse_Lookup import reverseLookup

Postal_Codes = {
    "Newfoundland": "A",
    "Nova Scotia": "B",
    "Prince Edward Island": "C",
    "New Brunswick": "E",
    "Quebec": ["G", "H", "J"],
    "Ontario": ["K", "L", "M", "N", "P"],
    "Manitoba": "R",
    "Saskatchewan": "S",
    "Alberta": "T",
    "British Columbia": "V",
    "Nunavut": "X",
    "Northwest Territories": "X",
    "Yukon": "Y"
}


post_code = input("Enter canadian postal code: ").upper()

if len(post_code) == 0:
    print("No postal code entered.")
else:
    province_found = False
    for province, code in Postal_Codes.items():
        if isinstance(code, list):
            if post_code[0] in code:
                print(f"Province/Territory: {province}")
                province_found = True
                break
        else:
            if post_code[0] == code:
                print(f"Province/Territory: {province}")
                province_found = True
                break

    if not province_found:
        print("Province not found for this postal code.")

    # Check for urban/rural
    if len(post_code) > 1:
        if post_code[1] == "0":
            print("Address Type: Rural")
        else:
            print("Address Type: Urban")
