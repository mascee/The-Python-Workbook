# Excercise 128. Count the Elements
# This is a function CountRange that returns number of elements within a list that are greater 
# then or equal to some minimum value and less than some maximum value.

def countRange(list, min, max):
    count = 0
    for element in list:
        if element > min and element < max:
            count +=1 

    return count

def main():
    list = [0, 1, 2, 3, 4, 5]
    print(f"There are {countRange(list, 1, 5)} numbers between 1 and 5. ")


if __name__ == "__main__":
    main()
        
