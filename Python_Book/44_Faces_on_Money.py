# THis program reads banknote from the user and displays what president appears on it.

user_input = input("Please enter what banknote do you have in a format $1, $ 10 etc. ")
banknote = int(user_input.replace("$", "").strip())

banknotes = {
    1: "George Washington",
    2: "Thomas Jefferson",
    5: "Abraham Lincoln",
    10: "Alexander Hamilton",
    20: "Andrew Jackson",
    50: "Ulysses S. Grant",
    100: "Benjamin Franklin"
}


if banknote in banknotes:
    print(f"{banknotes[banknote]} appears on the ${banknote} bill.")
else:
    print("Unknown banknote.")