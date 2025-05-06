# Opean and read a file, display each line with its number

fname = input("Enter the name of the file: ")
inf = open(fname, "r")

num = 1
line = inf.readline()

while line != "":
    print(f"{num}, {line}")
    num+=1
    line = inf.readline()

inf.close()