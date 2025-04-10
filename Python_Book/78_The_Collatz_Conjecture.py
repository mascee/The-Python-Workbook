# This program simulates Collatz Conjecture, that states that if it starts in positive integer,
# It ends on 1.
# The rules: Start with any positive integer.
# If the last term is even, add next term by dividing the last term by 2 using floor division,
# Else: Add another term to the sequence by multiplying the last term by 3 and adding 1.

number = int(input("Please enter any positive integer and I will make a Collatz Conjecture: "))

if number < 0:
    number = int(input("Please enter any positive integer and I will make a Collatz Conjecture: "))
    print(number)
else:
    while number!= 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = number*3 + 1
            print(number)


