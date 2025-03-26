# A particulat phone bill includes 50 minutes of air time and 50 text messages for $15 a month.
# Each additional minute costs $0.25, while additional text messages cost $0.15. 
# All cell phone bills include an additional charge of $0.44 to support 911 calls and the entire bill
# is subject to 5% sales tax.
#This program reads the user input of number of minutes used and number off messages and 
# displays base charge, additional charges, tax amount, 911 fee and total charge.

calls = int(input("How many minutes used this month for the phone calls?: "))
texts = int(input("How many messages used?: "))
base_plan = 15
base_minutes = 50
base_texts = 50
charge_911 = 0.44
tax = 5

if calls <= 50 and texts <= 50:
    total_tax = (base_plan + charge_911)*tax/100
    total = base_plan + charge_911 + total_tax
    print(f"Base plan is ${base_plan}. 911 charges ${charge_911}. Tax is ${total_tax:.2f}. Total is ${total:.2f}. ")

elif calls > 50 or texts > 50:
    total_tax = (base_plan + charge_911 + (calls - base_minutes)*0.25 + (texts - base_texts)*0.15)*tax/100
    total = base_plan + charge_911 + total_tax
    print(f"Base plan is ${base_plan}. Additional minutes {calls - base_minutes} minutes. Additional texts {texts - base_texts}. 911 charges ${charge_911}. Tax is ${total_tax:.2f}. Total is ${total:.2f}. ")
else:
    total = 0
    print("Error. ")
