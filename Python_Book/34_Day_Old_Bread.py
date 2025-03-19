# A bakery sells loaves of bread for $3.49
# Day old bread is discounted by 60 percent.
# Write a program that begins by reading the number of loaves of the day old bread
# beign purchased from the user. 
# The program should diplay the regular price of the bread, the discount, and the total price.

price = 3.49

discount = 60

discounted_price = 3.49 * 0.4

number_of_loaves = int(input("How many loaves of bread would you like to buy? "))

total_cost = number_of_loaves * discounted_price

print(f"All the bread that we have is day old. It's 60% discounted.  Regular price is ${price:.2f}. ")
print(f"The discounted price is ${discounted_price:.2f}. ")
print(f"Your total for {number_of_loaves} loaves is ${total_cost:.2f}. ")
