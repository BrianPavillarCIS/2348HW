# Brian Pavillar
# ID: 1863509

# Main Menu
print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12")
print("")

# Input
serve1 = input("Select first service:\n")
serve2 = input("Select second service:\n")
print("")
print("Davy's auto shop invoice")
print("")
# If Statements
s1 = 0
if serve1 == 'Oil change':
    s1 = 35
    print("Service 1: Oil change, $35")
elif serve1 == 'Tire rotation':
    s1 = 19
    print("Service 1: Tire rotation, $19")
elif serve1 == 'Car wash':
    s1 = 7
    print("Service 1: Car wash, $7")
elif serve1 == 'Car wax':
    s1 = 12
    print("Service 1: Car wax, $12")
elif serve1 == "-":
    print("Service 1: No service")

s2 = 0
if serve2 == 'Oil change':
    s2 = 35
    print("Service 2: Oil change, $35")
elif serve2 == 'Tire rotation':
    s2 = 19
    print("Service 2: Tire rotation, $19")
elif serve2 == 'Car wash':
    s2 = 7
    print("Service 2: Car wash, $7")
elif serve2 == 'Car wax':
    s2 = 12
    print("Service 2: Car wax, $12")
elif serve2 == "-":
    print("Service 2: No service")

# Total
tot = s1 + s2
print("")
print("Total: $", tot)