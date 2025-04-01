# This program rounds up the price to 5 pennies.
# This is needed for places where pennies are discontinued.


pennies_per_nickel = 5
nickel = 0.05  # Corrected from 0.5 to 0.05 (5 cents)

total = 0.0

line = input("Please enter the price (Enter to quit): ")

while line != "":
    total += float(line)
    line = input("Please enter the price (Enter to quit): ")

print(f"The exact amount payable is ${total:.2f}")

rounding_indicator = (total * 100) % pennies_per_nickel

if rounding_indicator < pennies_per_nickel / 2:
    cash_total = total - (rounding_indicator / 100)
else:
    cash_total = total + ((pennies_per_nickel - rounding_indicator) / 100)

print(f"Cash amount payable is ${cash_total:.2f}")
