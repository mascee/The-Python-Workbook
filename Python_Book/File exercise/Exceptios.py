# Trying exceptions

fname = input("Enter the file name: ")

file_opened = False

while file_opened == False:
    try:
        inf = open(fname, "r")
        file_opened = True
    except FileNotFoundError:
        print(f"{fname} wasn't found. Please try again: ")
        fname = input("Enter the file name: ")