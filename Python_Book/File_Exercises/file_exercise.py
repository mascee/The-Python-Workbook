# This exercise is for practicing with opening and reading files

fname = input("Enter the file name: ")
inf = open(fname, "r")

total = 0
line = inf.readline()
while line != "":
    total += float(line)
    line = inf.readline()

inf.close()

print(f"The total of the values in {fname} is {total}. ")