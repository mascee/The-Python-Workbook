# This program reads numbers from the user and displays negatives first, followed by zeros, followed by positives, 
# in the order they wer entered.

negatives = []
positives = []
zeros = []

line = input("Enter a number: ")
while line != "":
    number = int(line)
    if number < 0:
        negatives.append(number)
    elif number== 0:
        zeros.append(number)
    elif number > 0:
        positives.append(number)
    line = input("Enter a number: ")


print("Negatives: ")
for i in negatives:
    print(i)

print("Zeros: ")
for i in zeros:
    print(i)

print("Positives: ")
for i in positives:
    print(i)