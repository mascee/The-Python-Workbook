# Exercise 163
# Read files with baby names and display most popular baby names during one year.
# There should be 2 lists: One with baby girl names, and one with baby boys names.

import os
from pathlib import Path

folder = Path("BabyNames")

def get_most_popular_name(file_path):
    most_popular = ("", 0)
    with open(file_path, "r") as f:
        for line in f:
            name, count = line.strip().split(" ")
            count = int(count)
            if count > most_popular[1]:
                most_popular = (name, count)
    return most_popular

# Ask user for a year
year = input("Enter a year between 1900 and 2012: ").strip()

try:
    year_int = int(year)
    if not (1900 <= year_int <= 2012):
        raise ValueError

    boy_file = folder / f"{year}_BoysNames.txt"
    girl_file = folder / f"{year}_GirlsNames.txt"

    if not boy_file.exists() or not girl_file.exists():
        print("Name files for the selected year are missing:", boy_file, girl_file)
    else:
        boy_name, boy_count = get_most_popular_name(boy_file)
        girl_name, girl_count = get_most_popular_name(girl_file)

        print(f"Most popular boy name in {year}: {boy_name} ({boy_count} births)")
        print(f"Most popular girl name in {year}: {girl_name} ({girl_count} births)")

except ValueError as e:
    print(f"Invalid year. Please enter a number between 1900 and 2012: {e}")
    raise