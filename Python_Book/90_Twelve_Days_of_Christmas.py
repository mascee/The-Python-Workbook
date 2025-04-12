# This program writes a function that completes Twelve Days of Chiristmas song with different verses

from int_ordinal import ordinal

def DisplayVerse(n):
    print(f"On the {ordinal(n)} day of Christmas")
    print("my true love sent to me ")

    if n >= 12:
        print("Twelve drummers drumming, ")
    if n >=11:
        print("Eleven pipers piping")
    if n >=10:
        print("Ten lords a-leaping")
    if n>=9:
        print("Nine ladies dancing")
    if n>=8:
        print("Eight maids a milking")
    if n>=7:
        print("Seven swans a swimming")
    if n>=6:
        print("Six geese a laying")
    if n>=5:
        print("Five golden rings")
    if n>=4:
        print("Four calling birds")
    if n>=3:
        print("Three French hens")
    if n>=2:
        print("Two turtle-doves")
        print("And a partridge on a pear tree.\n")
    elif n==1:
        print("A partridge on a pear tree.\n")


def main():
        for verse in range(1, 13):
            DisplayVerse(verse)

main()