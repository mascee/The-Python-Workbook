# Exercise 169. Redacting Text in a file.
# Write a program that redacts all occurances of sensitive words
# in a file by replacing them with asterisk, even if they occur in the middle of a word.
# The list of sensitive words will be provided in a separate file.
# The name of the original file, sensitive words file and redacted file will be provided by the user.

inf_name = input("Please enter the name of the file to redact: ")
inf = open(inf_name, "r")

sens_inf = input("Please enter file name with sensitive words: ")
sens = open(sens_inf, "r")

redact_file = input("Please enter where to save redacted text: ")
redact = open(redact_file, "w")

# Load all sensitive words to a list
words = []
line = sens.readline()
while line != "":
    line = line.rstrip()
    words.append(line)

    line = sens.readline()
sens.close()

# Read each line in the input file. Replace all sensitive words with asterisks.
# Then write a line into an output file.
line = inf.readline()
while line != "":
    for word in words:
        line = line.replace(word, "*" * len(word))
    redact.write(line)
    line = inf.readline()
inf.close()
redact.close()
