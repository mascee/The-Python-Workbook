# Exercise 130. Unary and Binary Operators
# This program implements a function identifyUnary that determines if operator is unary or binary.

from Tokenizing_a_String import tokenList

def identifyUnary(tokens):
    retval = []
    for i in range(len(tokens)):
        if i == 0 and (tokens[i] == "+" or tokens[i] == "-"):
            retval.append("u" + tokens[i])
        elif i > 0 and (tokens[i] == "+" or tokens[i] == "-") and \
             (tokens[i-1] in {"+", "-", "*", "/", "("}):
            retval.append("u" + tokens[i])
        else:
            retval.append(tokens[i])
    return retval

def main():
    exp = input("Enter math expression: ")
    tokens = tokenList(exp)
    print(f"Tokens are {tokens}. ")

    marked = identifyUnary(tokens)
    print(f"With unary operators marked: {marked}. ")


if __name__ == "__main__":
    main()
  