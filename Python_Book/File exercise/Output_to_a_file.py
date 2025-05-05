# Writing output to  a file

fname = input("Where will the numbers be stored? ")
outf = open(fname, "w")

limit = int(input("What is the maximum value? "))
for num in range(1, limit + 1 ):
    outf.write(str(num) + "\n")

outf.close()
