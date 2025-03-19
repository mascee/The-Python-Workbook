# Develop a preogram that reads a 4-digit integer from the user and displays the sum of its digits.

number = int(input("Please enter 4-digit number: "))
copy_number = number

thousands = number // 1000
number = number % 1000
hundreds = number // 100
number = number % 100
tens = number // 10
number = number % 10
ones = number // 1

sum = thousands + hundreds + tens + ones


 
print (f"Sum of digits in {copy_number} is {thousands} + {hundreds} + {tens} + {ones} = {sum}. ")
