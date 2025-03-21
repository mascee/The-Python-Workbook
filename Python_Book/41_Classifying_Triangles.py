# This program reads all sides of a triangle and determines what kind of a triangle this is.

side1, side2, side3 = map(float, input("Please enter three sides of a triangle, separated by spaces: ").split())

if side1 == side2 and side2 == side3 and side3 == side1:
    {
        print("This is an equilateral triangle. ")
    }
elif side1 == side2 or side2 == side3 or side3 == side1:
    {
        print("This is isosceles triangle. ")
    }
elif side1 != side2 and side2 != side3 and side3 != side1:
    {
        print("This is a scalene triangle. ")
    }
else:
    {
        print("Error. ")
    }