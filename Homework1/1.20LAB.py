#BRYANCHAVARRIA
#1657040

import math

height = int(input("Enter wall height (feet) :\n"))

width = int(input("Enter wall width (feet) :\n"))

wall_area = height * width

paint_needed = wall_area / 350

cans = math.ceil(paint_needed)

paint_colors_cost={'red':35,'blue':25,'green':23}

print("Wall area: " + str(wall_area) + " square feet")

print("Paint needed: {:.2f} gallons".format(paint_needed))

print("Cans needed: " + str(cans) + " can(s)")

color=input("\nChoose a color to paint the wall:\n")

cost=cans * paint_colors_cost[color.lower()]

print ("Cost of purchasing " + str(color) + " paint: $" + str(cost))