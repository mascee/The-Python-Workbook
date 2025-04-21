# This program converts numbers between different bases

from Hex_to_Dec import hex2int, int2hex

def dec2n(num, new_base):
    result = ""
    q = num

    while q > 0:
        r = q % new_base
        result = int2hex(r) + result 
        q = q // new_base

    if result == "":
        result = "0" 

    return result

def n2dec(num, b):
    decimal = 0
    for digit in num:
        decimal = decimal * b + hex2int(digit)
    return decimal

def main():
    from_base = int(input("Enter base to convert from (2 to 16): "))
    if from_base < 2 or from_base > 16:
        print("Only bases between 2 and 16 are supported.")
        return

    from_num = input("Sequence of digits in that base: ")

    # Convert to base 10 and display results
    dec = n2dec(from_num.upper(), from_base)
    print(f"That's {dec} in base 10.")

    # Convert to new base
    to_base = int(input("Enter the base to convert to (2-16): "))
    if to_base < 2 or to_base > 16:
        print("Only bases from 2 to 16 are supported.")
        return

    to_num = dec2n(dec, to_base)
    print(f"That's {to_num} in base {to_base}.")

main()

