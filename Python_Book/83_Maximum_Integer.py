# This program finds maximum integer from the collection of integers 
# randomly selected from 1 to 100. 
# There could be duplicates.

from random import randrange

Num_Items = 100

#Generate the first number
max_number = randrange(1, Num_Items + 1)
print(max_number)

count_max = 0

for i in range(1, Num_Items, 1):
    number = randrange(1, Num_Items + 1)
    if number > max_number:
        max_number = number
        print(f"{max_number} <== Update")
        count_max += 1
    else:
        print(number)

print(f"The maxium value is {max_number}")
print(f"Maximum value was updated {count_max} times. ")
