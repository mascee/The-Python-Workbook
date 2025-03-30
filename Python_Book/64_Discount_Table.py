# This program shows prices $4.95, $9.95, $14.95, $19.95, $24.95
# Discount is 60%
# It creates a table with prices, discounted amount and a new price.

prices = [4, 95, 9.95, 14.95, 19.95, 24.95]
discount = 0.6

print(f"{'Original Price':<20}{'Discounted Amount':<20}{'Discounted Price':<20}")
print("="*60)

for price in prices:
    discounted_amount = price*discount
    discounted_price = price - discounted_amount
    print(f"{price:<20.2f}{discounted_amount:<20.2f}{discounted_price:<20.2f}")