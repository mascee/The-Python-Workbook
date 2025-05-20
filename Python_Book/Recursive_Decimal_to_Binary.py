# Exercise 175. Recursive Decimal to Binary
# Write a recursive function that converts a non-negative decimal number to binary.

def decimal_to_binary(n):
    index = 0
    result = ""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
    
def main():
    number = int(input("Enter a number: "))
    binary = decimal_to_binary(number)
    print(f"{number} to binary is: {binary}. ")

if __name__ == "__main__":
    main()



