# Write a program that computes body mass index (BMI) for an individual.
# Your program should begin by reading a height(m) and weight(kg) from the user.
# Then use this formula to compute: BMI = weight/(height*height)

height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in killogramms. "))

BMI = weight / (height**2)

print(f"Your BMI is {BMI:.2f}. ")