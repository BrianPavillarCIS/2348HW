# Name: Brian Pavillar
# ID: 1863509

# Function Definition
def exact_change (change):

    # Define Variable
    numdollars = 0
    numquarters = 0
    numdimes = 0
    numnickels = 0
    numpennies = 0

    # If there is no change
    if change == 0:
        print("no change")

    # While Loop
    while change > 0:
        if change >= 100:
            numdollars += 1
            change -= 100
        elif change >= 25:
            numquarters +=1
            change -= 25
        elif change >= 10:
            numdimes +=1
            change -= 10
        elif change >= 5:
            numnickels += 1
            change -= 5
        elif change >= 1:
            numpennies += 1
            change -= 1

    # Calculate for plurals
    if numdollars == 1:
        print("1 dollar")
    elif numdollars >= 1:
        print(numdollars, "dollars")
    if numquarters == 1:
        print("1 quarter")
    elif numquarters >= 1:
        print(numquarters, "quarters")
    if numdimes == 1:
        print("1 dime")
    elif numdimes >= 1:
        print(numdimes, "dimes")
    if numnickels == 1:
        print("1 nickel")
    elif numnickels >= 1:
        print(numnickels, "nickels")
    if numpennies == 1:
        print("1 penny")
    elif numpennies >=1:
        print(numpennies, "pennies")

# Input and Call Function
inputval = int(input())
exact_change(inputval)