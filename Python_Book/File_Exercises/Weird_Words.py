# Exercise 160. Weird Words.
# This program reads a file with words and checks for "I before E except after C rule".
# It makes 2 lists: One with words containing "E" that follow the rule,
# The second one is with "E" words that are exceptions.
# There are no repeated words in the lists.

word_file = "test5.txt"

with open(word_file, "r") as inf:

    #Using set to add words because it avoids duplicates automatically
    rule_words = set()
    exceptions = set()
    
    #For every line: 
    for line in inf:
        word = line.strip().lower()
        if "ei" in word or "ie" in word:
            if "cie" in word:
                exceptions.add(word)
            elif "cei" in word:
                rule_words.add(word)
            elif "ie" in word and "cie" not in word:
                rule_words.add(word)
            elif "ei" in word and "cei" not in word:
                exceptions.add(word)

    rule_words = sorted(rule_words)
    exceptions = sorted(exceptions)

    print(f"Rule words: {rule_words}")
    print(f"Exceptions: {exceptions}")

        

