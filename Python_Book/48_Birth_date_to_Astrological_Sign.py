# This program asks the user to enter his or her month and day of birth.
# Then the program reports the user's zodiac sign.

month, day = input("Enter month and date separated by space: ").split()

month = month.capitalize()
day = int(day)

if (month == "December" and day >=22 and day <=31) or (month == "January" and day <=19):
    print(" You are Capricorn. ")
elif (month == "January" and day >=20 and day <=31) or (month == "February" and day <= 18):
    print("You are Aquarius. ")
elif (month == "February" and day <=19) or (month == "March" and day <=20):
    print("You are Pisces. ")
elif (month == "March" and day > 21 and day <=31) or (month == "April" and day <= 19):
    print("You are Aries. ")
elif (month == "April" and day >19 and day <=30) or (month == "May" and day <=20):
    print("You are Taurus. ")
elif (month == "May" and day >20 and day <=31) or (month == "June" and day <=20):
    print("You are Gemini. ")
elif (month == "June" and day > 20 and day <=30) or (month == "July" and day <=22):
    print("You are Cancer. ")
elif (month == "July" and day >=23 and day <=31) or (month == "August" and day <=22):
    print("You are Leo. ")
elif (month == "August" and day >=23 and day <=31) or (month == "September" and day <=22):
    print("You are Virgio. ")
elif (month == "September" and day >=23 and day <=30) or (month == "October" and day <=22):
    print("You are Libra. ")
elif (month == "October" and day >=23 and day <=31) or (month == "November" and day <=21):
    print("You are Scorpio. ")
elif (month == "November" and day >=22 and day <=30) or (month == "December" and day <=21):
    print("You are Sagittarius. ")
else:
    print("Error. ")