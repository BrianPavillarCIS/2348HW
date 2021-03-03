# Name: Brian Pavillar
# ID: 1863509

# Input Statements
eq1x = int(input())
eq1y = int(input())
eq1z = int(input())
eq2x = int(input())
eq2y = int(input())
eq2z = int(input())

# Make Default boolean as False
default = False

# For loops
for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        # Checks whether equation works. Returns True if it does and prints variables
       if eq1x * x + eq1y * y == eq1z and eq2x * x + eq2y * y == eq2z:
           default = True
           print(x, y)

# If the statement does not return true, there is no solution.
if default == False:
    print('No solution')