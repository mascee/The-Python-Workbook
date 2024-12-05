#Excercise 6
import math
 
Price = float(input("Enter the price in $: "))
Tip = Price*0.18
Tax = Price*0.10

Total = Price + Tax + Tip

print(f"Your total is: ${Total:.2f}")