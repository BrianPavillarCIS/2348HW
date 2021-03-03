# Name: Brian Pavillar
# ID: 1863509

# Function Definition

def isPalindrome(string):
    string = string.replace(" ","")
    return string == string[::-1]

# Input & Function Call
palintest = str(input())
test = isPalindrome(palintest)

# If statement
if test:
    print(palintest, "is a palindrome")
else:
    print(palintest, "is not a palindrome")