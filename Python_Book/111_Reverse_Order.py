# This program reads integers from user and stores them in a list.
# 0 is used as a sentinel value to mark the end of the input.
# The program reverses the list and prints each number of a new line.

data = []

number = int(input("Enter integer(0 to break): "))
while number != 0:
    data.append(number)
    number = int(input("Enter integer(0 to break): "))
    

data.reverse()
print("Numbers is reverse order: ")
for num in data:
    print(num)


