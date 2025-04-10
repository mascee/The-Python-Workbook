# This program creates multiplication table from 1 to 10

i = 1
j = 1

for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        result = i* j
        print(f"{result:4}", end=" ")
    print()

