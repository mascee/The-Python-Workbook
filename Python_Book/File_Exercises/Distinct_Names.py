# Exercise 166
# This program reads every file in BabyNames folder and displays the list
# of girls names and the list of boys names without duplicates.


FIRST_YEAR = 1900
LAST_YEAR = 2012


def LoadTopName(fname, names):
    with open(fname, "r") as inf:
        line = inf.readline()
        name = line.split()[0]
        if name not in names:
            names.append(name)

def main():
    girls = []
    boys = []

    for year in range(FIRST_YEAR, LAST_YEAR + 1):
        girl_fname = f"BabyNames/{year}_GirlsNames.txt"
        boy_fname = f"BabyNames/{year}_BoysNames.txt"

        LoadTopName(girl_fname, girls)
        LoadTopName(boy_fname, boys)

    print("Girls names that reached #1: ")
    for name in girls:
        print(" ", name)
    print()

    print("Boys names that reached #1: ")
    for name in boys:
        print(" ", name)

main()


