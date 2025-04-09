# This program approximates pi up to the 15 digits.
# The first approximation for the first term.
# Each additional approximation includes one more term in the series, 
# making it better approximation then previous.
pi = 3

for i in range(0, 256, 2):
    if i == 0 or i % 4 == 0:
        pi += 4 / ((2+i) * (3+i) * (4+i))
        print(pi)
    else:
        pi = pi - 4 / ((2+i) * (3+i) * (4+i))
        print(pi)
