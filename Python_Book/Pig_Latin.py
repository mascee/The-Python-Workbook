# Excercise 122. Pig Latin
# If a word begins with a consonant, then all the letters at the begining of the word,
# up to the first vowel are removed and then added to the end of the word followed by "ay".
# If the word beging with a vowel, then way is added to the end of the word.

def pigLatin(word):
    vowels = "aeiou"
    word.lower()

    if word[0] in vowels:
        return word + "way"
    
    for i, char in enumerate(word):
        if char in vowels:
            return word[i:] + word[:i] + "ay"
        
    return word + "ay"

def main():
    text = input("Enter a text to translate to Pig Latin: ")
    words = text.split()

    pig_latin_words = [pigLatin(word) for word in words]
    pig_latin_sentence = ' '.join(pig_latin_words)
    print("Pig Latin Version: ")
    print(pig_latin_sentence)

if __name__ == "__main__":
    main()