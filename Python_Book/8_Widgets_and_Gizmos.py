# An online retailer sells 2 products: widgets and gizmos. Each widget weighs 75 grams.
# Each gizmo weighs 112 grams. Wrtie a program that reads the number of widgets and the number of gizmos from the user.
# Then your program should compute and display the total weight of the parts.

import math

widgets = int(input("Enter number of widgets: "))
gizmos = int(input("Enter number of gizmos: "))

total_weight = widgets * 75 + gizmos * 112

print(f"{widgets} widgets and {gizmos} gizmos weigh total of {total_weight} grams.")
