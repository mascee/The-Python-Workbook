# This program determines if a string represents an integer.

def isInteger(text):
    text = text.strip()

    if (text[0] == '+' or text[0] == '-') and text[1:].isdigit():
        return True
    if text.isdigit():
        return True
    return False
    
def main():
    text = input("Please enter your string: ")
    if isInteger(text):
        print("This string represents an integer. ")
    else:
        print("This string does not represent an integer. ")



if __name__ == "__main__":
    main()
