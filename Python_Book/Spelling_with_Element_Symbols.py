# Exercise 182. Spelling with Element Symbols
# Each chemical element has a standard symbol that is one, two or three letters long.
# Write a recursive function that determines whether or not a word can be spelled using only element symbols.

# Function takes a word and a list of symbols. 
# Returns a string containing the symbols used to achieve the spelling.

symbols = []
with open ("Data/Chemical_Elements.txt", "r") as file:
    for line in file:
        parts = line.strip().lower().split(",")
        if len(parts) >=2:
            symbols.append(parts[1])


def spell_elements(word, symbols):
    word = word.lower()
    if word == "":
        return []
    for length in range(1, 4):
        prefix = word[:length]
        if prefix in symbols:
            rest = spell_elements(word[length:], symbols)
            if rest is not None:
                return [prefix] + rest
    return None

def main():
    word = input("Enter a word and I will tell if you can spell it with Chemical Elements: ").strip().lower()
    result = spell_elements(word, symbols)
    if result is not None:
        print("Word {word} can be spelled as:","-".join(s.capitalize() for s in result))
    else:
        print("Word cannot be spelled using element symbols. ")


if __name__ == "__main__":
    main()



