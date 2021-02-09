# Brian Pavillar
# ID: 1863509

import math

# Define Variables and Print Area
height = float(input("Enter wall height (feet):\n"))
width = float(input("Enter wall width (feet):\n"))
area = int(height * width)
print("Wall area:", area, "square feet")

# Paint Gallons
gallon = 350
ppg = float(area / gallon)
print("Paint needed: {:.2f}".format(ppg), "gallons")

# Cans needed
cans = math.ceil(ppg)
print("Cans needed:", cans, "can(s)")
print("")

# I decided to use an if-else instead of a dictionary
clr = input("Choose a color to paint the wall:\n")
cost = 0
if clr == 'red':
    cost = cans * 35
    print("Cost of purchasing red paint: $",cost)
elif clr == 'blue':
    cost = cans * 25
    print("Cost of purchasing blue paint: $",cost)
elif cost == 'green':
    cost = cans * 23
    print("Cost of purchasing green paint: $",cost)
else:
    print("Not a valid color.")




