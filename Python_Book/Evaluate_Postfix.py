# Exercise 132. Evaluate Postfix

from Unary_and_Binary_Operators import identifyUnary

from Infix_to_Postfix import infixPostfix


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
        elif token == "u-":
            #Remove an item from the end of values
            #Negate the item and append the result of the negation to values
            val = values.pop()
            values.append(-val)
        elif token == "u+":
            val = values.pop()
            values.append(+val)

        # Else if the token is a binary operator then
        elif token in {"+", "-", "*", "/"}:
            #Remove an item from the end of values[] and call it right
            #Remove an item from the end of valuse and call it left
            #Compute the result of applying the operator to "left" and "right".
            # Append the result to values[]
            right = values.pop()
            left = values.pop()
            if token == "+":
                values.append(left+right)
            elif token == "-":
                values.append(left - right)
            elif token == "*":
                values.apend(left*right)
            elif token == "/":
                values.append(left/right)

        #Return the first item in values[] as value of the expression.
        return values[0] if values else None




def main():
    exp = input("Enter math expression: ")
    tokens = identifyUnary(exp)
    print("Tokens:", tokens)
    postfix = infixPostfix(tokens)
    print("Postfix:", postfix)
    eval_postfix = evaluatePostfix(postfix)
    print("Evaluated postfix: ", eval_postfix)

if __name__ == "__main__":
    main()
