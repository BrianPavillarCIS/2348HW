# Brian Pavillar
# ID: 1863509

# Define Variables
lemj = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
serve = float(input("How many servings does this make?\n"))

# Print Servings
print("")
print("Lemonade ingredients - yields {:.2f}".format(serve), "servings")
print("{:.2f}".format(lemj), "cup(s) lemon juice")
print("{:.2f}".format(water), "cup(s) water")
print("{:.2f}".format(agave), "cup(s) agave nectar")
print("")

# Increase serving size
servesize = float(input("How many servings would you like to make?\n"))
newsize = float(servesize / serve)
newlemj = lemj * newsize
newwater = water * newsize
newagave = agave * newsize

# Print New Servings
print("")
print("Lemonade ingredients - yields {:.2f}".format(servesize), "servings")
print("{:.2f}".format(newlemj), "cup(s) lemon juice")
print("{:.2f}".format(newwater), "cup(s) water")
print("{:.2f}".format(newagave), "cup(s) agave nectar")

# In Gallons
gallemj = newlemj / 16
galwater = newwater / 16
galagave = newagave / 16

# Print in gallons
print("")
print("Lemonade ingredients - yields {:.2f}".format(servesize), "servings")
print("{:.2f}".format(gallemj), "gallon(s) lemon juice")
print("{:.2f}".format(galwater), "gallon(s) water")
print("{:.2f}".format(galagave), "gallon(s) agave nectar")