# Exercise 132. Evaluate Postfix

def evaluatePostfix(tokens):
    # Create a new empty list, values:
    values = []

    #For each token in the postfix expression:
    for token in tokens:
        #If token is number then
        if token.isdigit():
            #Convert it to integer and append it to values
            values.append(int(token))
        # Else if the token is unary minus then    
        elif token == "-":
            #Remove an item from the end of values
            values[len(values) -1 ].pop()


def main():
    exp = input("Enter math expression: ")
    tokens = identifyUnary(tokenList(exp))
    print("Tokens:", tokens)
    postfix = infixPostfix(tokens)
    print("Postfix:", postfix)
    eval_postfix = evaluatePostfix(postfix)
    print("Evaluated postfix: ", eval_postfix)

if __name__ == "__main__":
    main()
