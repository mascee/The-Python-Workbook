# Excercise 108. Reduce Measures
# This program reduces recipe measures to largest possible unit.
# For example for 59 teaspoons it returns 1 cup, 3 tablespoons, 2 teaspoons

TSP_PER_TBSP = 3
TSP_PER_CUP = 48

def reduceMeasure(num, unit):
    if unit == "teaspoon" or unit == "teaspoons":
        teaspoons = num
    elif unit == "tablespoon" or unit == "tablespoons":
        teaspoons = num * TSP_PER_TBSP
    elif unit == "cup" or unit == "cups":
        teaspoons = num * TSP_PER_CUP

    # Convert number of teaspoons to the largest possible units
    cups = teaspoons // TSP_PER_CUP
    teaspoons = teaspoons - cups * TSP_PER_CUP
    tablespoons = teaspoons // TSP_PER_TBSP
    teaspoons = teaspoons - tablespoons * TSP_PER_TBSP

    result = ""

    if cups > 0:
        result = result + str(cups) + " cup"
        if cups > 1:
            result = result + "s"

    if tablespoons > 0:
        if result  != "":
            result = result + ", "
        result = result + str(tablespoons) + " tablespoon"
        if tablespoons > 1:
            result = result + "s"

    if teaspoons > 0:
        if result != "":
            result = result + ", "
        result = result + str(teaspoons) + " teaspoons"
        if teaspoons > 1:
            result = result + "s"
    
    if result == "":
        result = "0 teaspoons"

    return result

def main():
    print(f"59 teaspoons is {reduceMeasure(59, 'teaspoons')}")
    print(f"59 tablespoons is {reduceMeasure(59, 'tablespoons')}")
    print(f"1 teaspoon is {reduceMeasure(1, 'teaspoon')}")
    print(f"1 cup is {reduceMeasure(1, 'cup')}")
    print(f"3 cups is {reduceMeasure(3, 'cups')}")
    print(f"99 teaspoons is {reduceMeasure(99, 'teaspoons')}")

main()