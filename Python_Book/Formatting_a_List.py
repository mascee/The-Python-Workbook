# Excercise 120. Formatting a List
# This program has a function that takes a list of strings as its only parameter.
# This function returns a string that contains all of the items in the list, separated by commas with the last word separated by "and".
# If it's a one word in the list, it doesn't have any commas or "and".

def formatList(items):
    # If the string is empty return empty
    if len(items) == 0:
        return "<empty>"
    # If the string has only one word, return tis word
    elif len(items) == 1:
        return str(items[0])
    
    # Loop through all words until the last two and separate them by ","
    result = ""
    for i in range(0, len(items) - 2):
        result = result + str(items[i]) + ","

    # Put "and" between last two words
    result = result + str(items[len(items)-2]) + " and "
    result = result + str(items[len(items) -1])
    return result

def main():
    items = []
    word = input("Enter a list of items: ")
    while word != "":
        items.append(word)
        word = input("Enter a list of items: ")

    print(f"The items in the list are: \n {formatList(items)}")
    

if __name__ == "__main__":
    main()