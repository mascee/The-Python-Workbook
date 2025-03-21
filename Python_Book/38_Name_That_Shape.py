# This program determines shape from number of sides from 3 to 10.

side = int(input("How many sides are in the shape? Enter from 3 to 10: "))

if side == 3:
    {
        print("It's a triangle. ")
    }
elif side == 4:
    {
        print("It's a rectangle. ")
    }
elif side == 5:
    {
        print("It's a pentagon. ")
    }
elif side == 6:
    {
        print("It's a hexagon. ")
    }
elif side == 7:
    {
        print("It's a heptagon. ")
    }
elif side == 8:
    {
        print("It's an octagon. ")
    }
elif side == 9:
    {
        print("It's a nonagon. ")
    }
elif side == 10:
    {
        print("It's a decagon. ")
    }
else:
    {
        print("Shape is out of range. ")
    }