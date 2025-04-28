# Excercise 129. Tokenizing a String
# Tikenizing is the process of converting a string into a list of substrings,
# known as tokens. 
# This program takes mathematica expression and breaks it into a list of tokens.

# Tockens are *, /, ^, -, +

def tokenList(s):
    count = 0
    s = s.replace(" ", "")
    i = 0
    tokens = []
    while i < len(s):
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or s[i] == "-" or s[i] == "+" or i == "(" or i == ")":
            tokens.append(s[i])
            i += 1
        elif s[i] >= "0" and s[i] <= "9":
            num = ""
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num += s[i]
                i += 1
            tokens.append(num)
        else:
            return []
    return tokens

def main():
    exp = input("Enter math expression: ")
    tokens = tokenList(exp)
    print(tokens)

if __name__ == "__main__":
    main()