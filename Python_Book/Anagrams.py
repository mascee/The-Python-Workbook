# Exercise 143. Anagrams
# Two words are anagrams if they contain all of the same letters, but in a different order.
# For example "live" and "evil" are anagrams.
# Create a program that reads two strings from the user, determines whether or not they are anagrams.

def characterCounts(s):
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    return counts

def main():
    s1 = input("Enter the first word: ").upper()
    s2 = input("Enter the second word: ").upper()

    count_s1 = characterCounts(s1)
    count_s2 = characterCounts(s2)
    if count_s1 == count_s2:
        print("Those words are anagrams. ")
    else:
        print("Those words are not anagrams. ")


if __name__ == "__main__":
    main()