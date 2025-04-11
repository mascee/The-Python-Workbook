# This program writes a function that takes 3 values as parameters and returns te median value
# of those parameters as a result.

def median(a, b, c):
    if (a > b and b > c) or (a < b and b < c):
        return b
    elif (a > b and a < c) or (a < b and a > c):
        return a
    elif (c > a and c < b) or ( c > b and a < a):
        return c
    
def main():
    a, b, c = map(int, input("Please enter three integers separated by space and I will tell a median: ").split())
    med = median(a, b, c)
    print(f"Median of {a}, {b} and {c} is {med}. ")

main()

    
