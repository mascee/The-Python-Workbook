# Exercise 134. Generate all Sublists of a list.

def allSublists(data):
    sublists = [[]]
    for lenght in range (1, len(data)+1):
        for i in range(0, len(data) - lenght + 1):
            sublists.append(data[i:i+lenght])
    return sublists

def main():
    data = [1, 2, 3, 4, 5, 6]
    print(f"Sublists of {data} are: ")
    print(allSublists(data))

if __name__ == "__main__":
    main()