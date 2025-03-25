# This program reads employee rating 0.0 or 0.4 or 0.6 or more
# and converts it to letter performance. 
# The appropriate raise is calculated.

rating = float(input("Please enter employee rating (0.0, 0.4 or 0.6): "))

if rating == 0.0:
    letter_rating = "Unacceptable Performance"
    raise_amount = rating * 2400
    print(f"{rating} rating is {letter_rating}. Raise amount is ${raise_amount}. ")
elif rating == 0.4:
    letter_rating = "Acceptable Performance"
    raise_amount = rating * 2400
    print(f"{rating} rating is {letter_rating}. Raise amount is ${raise_amount}. ")
elif rating == 0.6:
    letter_rating = "Meritorious Performance"
    raise_amount = rating * 2400
    print(f"{rating} rating is {letter_rating}. Raise amount is ${raise_amount}. ")
else:
    print("Invalid rating. ")