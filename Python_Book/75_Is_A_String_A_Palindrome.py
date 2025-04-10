# This program determines if a word is a palindrome

user_input = input("Please enter a string and I will tell you if it's a palindrome: ").strip(" ")
user_input_lowered = user_input.replace(" ", "").replace(",", "").replace(".", "").lower()

if user_input_lowered == user_input_lowered[::-1]:
    print(f"{user_input} is a Palindrome")
else: 
    print(f"{user_input} is not a Palindrome")

