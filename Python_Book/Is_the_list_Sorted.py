# Excercise 127. Is a list already in Sorted Order?
# This program has a function that determines if a list is sorted in ascending or decsending order.

list = []

def is_sorted(list):
    if len(list) <=1:
        return True
    ascending = all(list[i] <= list[i + 1] for i in range(len(list) - 1))
    descending = all(list[i] >= list[i + 1] for i in range(len(list) - 1))     
    return ascending or descending     

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    # numbers = [2, 10, 5, 7]
    if is_sorted(numbers) == True:
        print("The list is sorted. ")
    else:
        print("The list is not sorted. ")

if __name__ == "__main__":
    main()
