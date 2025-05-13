# Exercise 165.
# Most Births in a given time period.
# Write a program that uses the baby names from BabyNames folder to determine which names 
# were used most often within a time period. Have the user supply the first and last years of the range
# to analyze. Display the boys' name and the girl's name given to the most children during the indicated years.

FIRST_YEAR = 1900
LAST_YEAR = 2012
import os

def LoadNamesWithCounts(fname, counts_dict):
    with open(fname, 'r') as inf:
        for line in inf:
            parts = line.split()
            name = parts[0]
            count = int(parts[1])
            if name in counts_dict:
                counts_dict[name] += count
            else:
                counts_dict[name] = count

def main():
    # Get year range from user
    start_year = int(input(f"Enter the first year ({FIRST_YEAR}–{LAST_YEAR}): "))
    end_year = int(input(f"Enter the last year ({FIRST_YEAR}–{LAST_YEAR}): "))

    # Validate input
    if start_year < FIRST_YEAR or end_year > LAST_YEAR or start_year > end_year:
        print("Invalid year range.")
        return

    boy_counts = {}
    girl_counts = {}

    # Process files in range
    for year in range(start_year, end_year + 1):
        girl_file = f"BabyNames/{year}_GirlsNames.txt"
        boy_file = f"BabyNames/{year}_BoysNames.txt"

        if os.path.exists(girl_file):
            LoadNamesWithCounts(girl_file, girl_counts)
        else:
            print(f"Missing file: {girl_file}")

        if os.path.exists(boy_file):
            LoadNamesWithCounts(boy_file, boy_counts)
        else:
            print(f"Missing file: {boy_file}")

    # Find most popular names
    most_popular_girl = max(girl_counts, key=girl_counts.get)
    most_popular_boy = max(boy_counts, key=boy_counts.get)

    print(f"\nFrom {start_year} to {end_year}:")
    print(f"Most popular girl's name: {most_popular_girl} ({girl_counts[most_popular_girl]} times)")
    print(f"Most popular boy's name: {most_popular_boy} ({boy_counts[most_popular_boy]} times)")

main()



