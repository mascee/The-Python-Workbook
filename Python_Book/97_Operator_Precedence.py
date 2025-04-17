# This program contains function that returns operator precedence for a character like "*", "+", "-" etc
# "^" is used for power operator

def operator(ch):
    if ch == "+" or ch == "-":
        return 1
    elif ch == "*" or ch == "/":
        return 2
    elif ch == "^":
        return 3
    else:
        return -1
    
def main():
    ch = input("Enter operator: ")
    result = operator(ch)
    print(f"Order of {ch} operator is {result}. ")

if __name__ == "__main__":
    main()