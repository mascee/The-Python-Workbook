# Exercise 133. Does a list contain a sublist.

def isSublist(larger, smaller):
    if smaller == 0:
        return True
    elif len(smaller) > len(larger):
        return False
    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i+len(smaller)] == smaller:
            return True
    return False

def main():
     # smaller = [2, 3]
    # larger = [1, 2, 3, 4, 5, 6]

    smaller = ['a', 'b', 'c']
    larger = ['a', 'b', 'c', 'd']
    if isSublist(larger, smaller):
        print(f"The {smaller} is a sublist of {larger}. ")
    else:
        print(f"The {smaller} is not a sublist of {larger}. ")


if __name__ == "__main__":
    main()
    
