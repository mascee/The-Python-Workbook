# Create a program that reads 3 integers from the user and displays them
# in sorted order (from smallest to largest).

integer1, integer2, integer3 = map(int, input("Please enter three integers separated by spaces: ").split())

max_value = max(integer1, integer2, integer3)
min_value = min(integer1, integer2, integer3)
middle_value = (integer1 + integer2 + integer3) - min_value - max_value

print(f"Here are sorted integers: {min_value}, {middle_value}, {max_value}. ")