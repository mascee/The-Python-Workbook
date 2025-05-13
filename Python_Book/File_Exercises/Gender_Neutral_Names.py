# Exercise 164
# Gender Neutral Names
# This program determines and displays all of the baby names that were used
# for both boys and girls in a year specified by the user.


FIRST_YEAR = 1900
LAST_YEAR = 2012

def LoadAllNames(fname):
    names = []
    with open(fname, 'r') as inf:
        for line in inf:
            parts = line.split()
            name = parts[0]
            names.append(name)
    return names

def main():
    year = int(input(f"Enter a year between {FIRST_YEAR} and {LAST_YEAR}:  "))
    if year < FIRST_YEAR or year > LAST_YEAR:
        print("Invalid year. Please enter a year in the range. ")
        return
    
    girl_fname = f"BabyNames/{year}_GirlsNames.txt"
    boy_fname = f"BabyNames/{year}_BoysNames.txt"

    try:
        girls = LoadAllNames(girl_fname)
        boys = LoadAllNames(boy_fname)

        gender_neutral = sorted(set(girls) & set(boys))

        print(f"\nGender-Neutral names in {year} year: ")
        if gender_neutral:
            for name in gender_neutral:
                print(" ", name)
        else:
            print(" No gender-neutral names found. ")

    except FileNotFoundError:
        print(f"File for year {year} not found. ")

main()

