# Exercise 131. Infix to Postfix

from Unary_and_Binary_Operators import identifyUnary
from Tokenizing_a_String import tokenList

def precedence(op):
    if op == "=":
        return 0
    elif op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2
    elif op.startswith("u"):  # Unary operators
        return 3
    return -1

def infixPostfix(tokens):
    operators = []
    postfix = []

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                postfix.append(operators.pop())
            operators.pop()  # Remove the "("
        elif token in {"+", "-", "*", "/", "=", "u+", "u-"}:
            while (operators and operators[-1] != "(" and 
                   precedence(token) <= precedence(operators[-1])):
                postfix.append(operators.pop())
            operators.append(token)

    while operators:
        postfix.append(operators.pop())

    return postfix

def main():
    exp = input("Enter math expression: ")
    tokens = identifyUnary(tokenList(exp))
    print("Tokens:", tokens)
    postfix = infixPostfix(tokens)
    print("Postfix:", postfix)

if __name__ == "__main__":
    main()
