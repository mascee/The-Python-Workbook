# 145. Scrabble Score
# In the game of scrabble each letter has points associated with it. 
# The total score of a word is a sum of the scores of its letter.
# More common letter are worth fewer points while less common letters are worth 
# more points.
# Write a program that computes and displays the Scrabble score for a word.
# Create a dictionary that maps from letters to point values.
# Then use the dictionary to compute the score.

Point_Letters = {
    1: ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}

score = 0
word = input("Enter a word: ").upper().strip(" ")

for ch in word:
    found = False
    for point, letters in Point_Letters.items():
        if ch in letters:
            score += point
            found = True
            break
    if not found:
        print(f"Skipping unsupported character: {ch}. ")

print(f"Total score is {score}. ")


