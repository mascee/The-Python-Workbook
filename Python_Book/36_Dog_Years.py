# It is commonly said that one human year is equivalent to 7 dog years.
# However this simple conversation fails to recognize that dogs reach adulthood in approximately
# two years. As a result, some people believe that it is better to count each of the first two
# human years as 10.5 dog years, and then count each additional human years as 4 dog years.
# This program converts dog years to human years using this formula.

dog_years = int(input("How old is your dog? "))

if dog_years == 1:
    print ("It's 10.5 in human years. ")
elif dog_years == 2:
    print("It's 21 in human years. ")
else:
    total_years = 10.5 * 2 + (dog_years - 2) * 7
    print (f"It's {total_years} in human years. ")