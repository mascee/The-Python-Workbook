# An online retailer provides express shipping for many of its item at a rate of $ 10.95
# for the first item in an order, and $2.95 for each subsequent item in the same order.
# This program creates a function that takes the number of items in the order
# as the only parameter.
# Return the shipping charge for the order as the function's result

def shipping_calculator(number_items):
    FIRST_ITEM_COST = 10.95
    EACH_ITEM_COST = 2.95
    if number_items == 0:
        return 0
    else:
        total = FIRST_ITEM_COST + EACH_ITEM_COST * (number_items-1)
        return total

def main():
    number_items = int(input("How many items in your order? "))
    total = shipping_calculator(number_items)
    print(f"Your total shipping cost is ${total:.2f}. ")

main()