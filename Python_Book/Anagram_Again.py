# 144 Anagram Again.
# This program checks if multiple words are anagrams

from Anagrams import characterCounts

def main():
    s1 = input("Enter the first sentence: ").upper().strip(" ")
    s2 = input("Enter the second sentence: ").upper().strip(" ")

    count_s1 = characterCounts(s1)
    count_s2 = characterCounts(s2)
    if count_s1 == count_s2:
        print("Those sentences are anagrams. ")
    else:
        print("Those sentences are not anagrams. ")


if __name__ == "__main__":
    main()