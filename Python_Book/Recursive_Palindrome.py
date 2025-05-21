# 178. Recursive Palindrome
# This program determines if the word is a palindrome, using recursion.

def palindrome(word):
    word = word.lower()
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return False
    

def main():
    word = input("Enter a word and I will tell if its a palindrome:   ")
    if palindrome(word):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

if __name__ == "__main__":
    main()
