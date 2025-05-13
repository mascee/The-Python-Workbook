# Exercise 163
# Read files with baby names and display most popular baby names during one year.
# There should be 2 lists: One with baby girl names, and one with baby boys names.


FIRST_YEAR = 1900
LAST_YEAR = 2012

# Load the first line from the file, extract the name, and add it 
# to the names list if it is not already presents.
def LoadAndAdd(fname, names):
    inf = open(fname, "r")
    line = inf.readline()
    inf.close()
    parts = line.split()
    name = parts[0]

    #Add the name to the list if it is not already present
    if name not in names:
        names.append(name)


# Display the girls and boys names that reached #1 in at least one year
# between 1900 and 2012
def main():
    girls = []
    boys = []
    for year in range(FIRST_YEAR, LAST_YEAR + 1):
        girl_fname = "BabyNames/" + str(year) + "_GirlsNames.txt"
        boy_names = "BabyNames/" + str(year) + "_BoysNames.txt"
        LoadAndAdd(girl_fname, girls)
        LoadAndAdd(boy_names, boys)
    print("Girls names that reached #1: ")
    for name in girls:
        print(" ", name)
    print()

    print("Boys names that reached #1: ")
    for name in boys:
        print(" ", name)


main()
