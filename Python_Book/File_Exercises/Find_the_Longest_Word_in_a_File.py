# Exercise 153. 
# Find the longest word in a file. Display its length as well as all words with the same length.
# Treat any group of non-white space characters as a word, even if it includes digits or punctuation marks.



import sys
print(sys.argv)

if len(sys.argv) != 2:
    print("Provide a file name as a command line argument. ")
    quit()

try:
    inf = open(sys.argv[1], "r")
    largest_words = []
    max_length = 0

    for line in inf:
        words = line.split()
        for word in words:
            word_length = len(word)
            if word_length > max_length:
                max_length = word_length
                longest_words = [word]
            elif word_length == max_length:
                longest_words.append(word)
    print(f"Longest length: {max_length}. \nLongest words are: {longest_words}")
    inf.close()


except IOError as e:
    print("Error occured while processing the file. ")
    quit()
    
    


                

