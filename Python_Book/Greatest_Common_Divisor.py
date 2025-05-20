# Exercise 174. Greatest Common Divisor. Recursion

def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return greatest_common_divisor(b, c)
    
def main():
    a = int(input("Enter the first positive integer: "))
    b = int(input("Enter the second positive integer: "))
    common_divisor = greatest_common_divisor(a, b)
    print(f"Greatest common divisor of {a} and {b} is {common_divisor}. ")

if __name__ == "__main__":
    main()

    