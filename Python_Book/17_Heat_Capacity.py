# The amount of energy required to increase the temperature of one gram 
# of material by one degree Celsius is the material's specific eat capacity, C.
# The total amount of energy, q, required to raise m grams of material by delta T degrees Celcius
# can be computed using the formula: q = m*C*deltaT
#Write a program that reads the mass of some water and temperature change from the user.
#This program should display the total amount of energy that must be added or removed
# to achieve the desired temperature change.
#Water heat capacity is 4.186

#Bonus: Compute the cost of boiling water for a cup of coffee, assuming that electricity cost is 8.9 cents per kilowatt hour

import math

mass = float(input("How much water in ml or grams do you need to heat/cool down?"))

t1 = float(input("What is a temperature of the water in C? "))

t2 = float(input("What is the desired water temperature in C? "))

q = mass* 4.186 *(t2 - t1)

if q > 0:
    {
        print(f"You need {q:.2f} Joules to heat the {mass} ml of water from {t1}C to {t2}C. ")
    }
elif q == 0:
    {
    print("Your water is already at desired temperature. ")
    }
elif q < 0:
    {
    print(f"You need {abs(q):.2f} Joules to cool down {mass} ml of water from {t1}C to {t2}C. ")
    }


# Compute the cost of boiling water for a cup of coffee, assuming that electricity cost is 8.9 cents per kilowatt hour

#kwh = q/360000

cup_of_cofee = 200 #200 ml or grams

# To heat water from room temperature 20 C to boiling temperature 100 C
t2 = 100
t1 = 20

q_coffee = cup_of_cofee* 4.186 *(t2 - t1)

total_cost = (8.9 * (q_coffee/360000))/100 # Converted to dollars

print(f"It costs ${total_cost:.2f} to heat a cup of coffee. ")
