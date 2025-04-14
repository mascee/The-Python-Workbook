# This program determines if three given lenght can form a triangle
# Returns boolean result

def triangle(side_1, side_2, side_3):
    if side_1 < 0 or side_2 < 0 or side_3 < 0:
        return False
    elif side_1 > (side_2 + side_3) or side_2 > (side_1 + side_3) or side_3 > (side_1 + side_2):
        return False
    else:
        return True
    
def main():
    side_1, side_2, side_3 = map(float, input("Please enter 3 sides separated by space: ").split())
    result = triangle(side_1, side_2, side_3)
    if result == False:
        print(f"Sides {side_1}, {side_2} and {side_3} can't form a triangle. ")
    else:
        print(f"Sides {side_1}, {side_2} and {side_3} can form a triangle. ")

main()