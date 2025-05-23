# Exercise 184. Flatten a List
# Python's lists can contain other lists.
# When one list occurs inside another the inner list is said to be nested inside the outer list.
# Each of the inner lists nested within the outer list may also contain nested lists,
# and those lists may contain additional nested lists to any depth.
# Example: [1, [2, 3], [4, [5, [6, 7]]], [[[8, 9], [10]]]
# Flattening a list is a process of converting a list that may contain multiple levels
# of nested lists into a list that contains all of the same elements without nesting.
# Write a function that implements the recursive flattening algorithm.


def flatten(data):
    # If the data is empty, return empty list
    if data == []:
        return []
    if type(data[0]) == list:
        # Set l1 to the  result of flattening the first element in data
        # Set l2 to the result of flattening all of the elements in data except the first 
        #Return concatenation of l1 and l2
        return flatten(data[0]) + flatten(data[1:])
    else:
        #Set l1 to a list containing only the first element in data
        #Set l2 to the result of flattening all of the elements in data, except first
        #Return concatenation of l1 and l2
        return [data[0]] + flatten(data[1:])
    

def main():
    print(flatten([1, 2, [3, 4, [5]]]))

if __name__ == "__main__":
    main()



    