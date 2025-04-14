# This function takes a string "s" as its first parameter,
# and the width of the window in characters "w" as its second parameter.
# The function returns a new string that includes whatever leading spaces are needed so that "s"
# will be centered in the window when the new string is printed.
# The new string should be constructed in the following manner:
# If the lenght of "s" is greater then or equal to the width of the window then "s"
# should be returned.
# If the length of "s" is less than the width of the window then a string containing 
# (len(s) -w) // 2 spaces followed by s should be returned.

WIDTH = 80

def center(s, width):
    if width < len(s):
        return s
    
    spaces = (width - len(s)) // 2
    result = " " * spaces + s
    return result


def main():
    print(center("Hello, World! ", WIDTH))
    print(center("Mirrow Mirrow on the Wall, Who is the Fairest of them all? ", WIDTH))
    print(center("Peppa Pig", WIDTH))
    print()
    print("Ones upon a time...")


main()