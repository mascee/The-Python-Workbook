# Excercise 123. Pig Latin Improved
# This program adds capital letters and punctuation to the previous program.

import string

def pigLatinImproved(word):
    vowels = "aeiou"

    #Save punctuation if any from the end
    end_punct = ""
    if word[-1] in string.punctuation:
        end_punct = word[-1]
        #Remove punctuation
        word = word[:-1]

    #Check if the original word is capitalized
    is_capitalized = word[0].isupper()
    word_lower = word.lower()

    #Pig Latin Conversion
    if word_lower[0] in vowels:
        pig_word = word_lower + "way"
    else:
        for i, char in enumerate(word_lower):
            if char in vowels: 
                pig_word = word_lower[i:] + word_lower[:i] + "ay"
                break
            else:
                pig_word = word_lower +"ay"
    if is_capitalized:
        pig_word = pig_word.capitalize()

    pig_word += end_punct

    return pig_word


def main():
    sentence = input("Enter a sentence to convert to Pig Latin: ")
    words = sentence.split()
    pig_latin_sentence = ' '.join([pigLatinImproved(word) for word in words])
    print("Pig Latin version:", pig_latin_sentence)

if __name__ == "__main__":
    main()
