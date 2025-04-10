# This program converts decimal number (base 10) to binary number (base 2).

q = int(input("Please enter integer and I will convert it to binary number: "))
index = 0
if q < 0:
    print("Enter positive integer. ")
else:
    result = ""
    while q != 0:
        r = q % 2
        result += str(r)
        q = q // 2
    print(f"Binary number is {result}. ")
