# Exercise 180. String Edit Distance
# Write a recursive function that computes the edit distance between two strings.

def string_edit_dist(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0 if s[-1] == t[-1] else 1

        d1 = string_edit_dist(s[:-1], t) + 1
        d2 = string_edit_dist(s, t[:-1]) + 1     
        d3 = string_edit_dist(s[:-1], t[:-1]) + cost 
        return min(d1, d2, d3)

def main():
    str_1 = input("Enter a string: ")
    str_2 = input("Enter a second string: ")
    print(f"edit distance between string {str_1} and {str_2} is {string_edit_dist(str_1, str_2)}")

if __name__ == "__main__":
    main()

