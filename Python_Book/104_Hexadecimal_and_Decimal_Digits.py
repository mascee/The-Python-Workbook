# This program has two functions, hex2int and int2hex, that convert between hexadecimal digits
# and decimal integers.

def hex2int(hex_string):
    int_value = int(hex_string, 16)
    return int_value

def int2hex(int_value):
    hex_string = hex(int_value)
    return hex_string

def main():
    hex_string = input("Enter hexadecimal number: ")
    int_value = hex2int(hex_string)
    print(f"{hex_string} is {int_value} in decimal")

    int_value = int(input("Enter integer: "))
    hex_string = int2hex(int_value)
    print(f"{int_value} is {hex_string} in hexadecimal")

if __name__ == "__main__":
    main()
 
