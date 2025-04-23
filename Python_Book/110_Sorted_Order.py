# This program reads integers from user, stores them in a list, sorts them
# in the ascending order and displays one by one on each line

data = []

line = input("Enter an integer(blank to finish): ")
while True:
    line = input("Enter an integer(blank to finish): ")
    if line == "":
        break
    try:
        n = int(line)
        data.append(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

data.sort()

for num in data:
    print(f"{num}\n")

          