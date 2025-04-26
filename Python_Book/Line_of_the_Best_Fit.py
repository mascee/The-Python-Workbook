# A line of the best fit is a straight line that best approximates a collection 
# of n data points. In this excercise each point in the collection has an x coordinate and a y coordinate.
# The line of the best fit is represented by the equation y = mx + b where m and b are calculated using formulas:
# m = (sum(xy) - (sum(x)sum(y)/n)) / (sum(x^2) - (sum(x))^2 /n). b = avg(y) - m(avg(x))

x_list = []
y_list = []

while True:
    x = input("Please enter x coordinate: ")
    y = input("Please enter y coordinate: ")

    if x == "" or y == "":
        break  # exit loop if user enters empty string

    x_list.append(float(x))
    y_list.append(float(y))

# Only calculate if we have at least 2 points
if len(x_list) >= 2:
    n = len(x_list)
    sum_xy = sum(x*y for x,y in zip(x_list, y_list))

    sum_xy_over_n = ((sum(x_list))*(sum(y_list))) / n

    numerator = sum_xy + sum_xy_over_n
    
    denominator = (sum(x**2 for x in x_list)) - ((sum(x_list))**2) / n

    m = numerator / denominator

    b = sum(y_list)/len(y_list) - m * (sum(x_list) / len(x_list))

#line_of_best_fit = m * x + b
print(f"Line of best fit: y = {m:.2f} * x + {b:.2f}")








