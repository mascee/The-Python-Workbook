# Counting characters using recursion

def count(s, ch):
    if s == "":
        return 0
    tail = s[1 : len(s)]
    if ch == s[0]:
        return 1 + count(tail, ch)
    else:
        return count(tail, ch)
    
def main():
    s = input("Enter a string: ")
    ch = input("Enter the character to count: ")
    print(f"Character {ch} appears {count(s, ch)} times in the string {s}. ")

main()