# This program determines if a number is prime number

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main():
    number = int(input("Enter integer and I will tell you if it's prime: "))
    result = is_prime(number)
    if result == True:
        print(f"{number} is Prime. ")
    else:
        print(f"{number} is not Prime. ")

if __name__ == "__main__":
    main()
        