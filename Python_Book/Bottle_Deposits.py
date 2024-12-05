#Excercise 5
import math

small_bottle = int(input("How many bottles lest then 1 liter do you have?"))
big_bottle = int(input("How many bottles more then one liter do you have?"))

total = small_bottle*0.1 + big_bottle*0.25

print(f"Your total refund is ${total:.2f}")


                         