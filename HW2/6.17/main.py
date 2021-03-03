# Name: Brian Pavillar
# ID: 1863509

# Input Statement
password = str(input())

# After looking through Ch.8, using "replace()" looks like the best option.
password = password.replace("i", "!")
password = password.replace("a", "@")
password = password.replace("m", "M")
password = password.replace("B", "8")
password = password.replace("o", ".")

# Append String & Print
password = password + "q*s"
print(password)
