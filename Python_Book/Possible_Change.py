# Exercise 181. Possible Change
# Create a program that determines whether or not it is possible to construct 
# a particular total using a specific number of coins.


quarter = 25
dime = 10
nickel = 5
penny = 1
coin_list = [quarter, dime, nickel, penny]

def Possible_Change(amount, coins):
    #Convert dollars to cents
    amount = round(amount * 100)
    return can_form_amount(amount, coins)



def can_form_amount(remaining_amount, remaining_coins):
    # Base cases
    if remaining_amount == 0 and remaining_coins == 0:
        return True
    if remaining_amount < 0 or remaining_coins <= 0:
        return False
    for coin in coin_list:
        if can_form_amount(remaining_amount - coin, remaining_coins - 1):
            return True
    return False

def main():
    amount = float(input("Enter dollar amount?: "))
    coins = int(input("How many coins do you have? "))
    if Possible_Change(amount, coins):
        print(f"You have coins to pay ${amount}. ")
    else:
        print(f"You can't form ${amount} with coins. ")

if __name__ == "__main__":
    main()

