# Name: Brian Pavillar
# ID: 1863509

# Import datetime
import datetime

# Function converting month into number
def month_converter(month):
    month = month.replace("January", "1")
    month = month.replace("February", "2")
    month = month.replace("March", "3")
    month = month.replace("April", "4")
    month = month.replace("May", "5")
    month = month.replace("June", "6")
    month = month.replace("July", "7")
    month = month.replace("August", "8")
    month = month.replace("September", "9")
    month = month.replace("October", "10")
    month = month.replace("November", "11")
    month = month.replace("December", "12")
    return month

# Get Input and split string, create empty string
date = str(input())
new_date = []

# Convert into delimiter and split string
new_date= date.replace(" ",",")
new_date= date.split(",")

# Call function for month change via month[0]
month_converter(new_date[0])

print(new_date)

# Call for Current Date
x = datetime.datetime.now()
x = x.strftime("%x")
