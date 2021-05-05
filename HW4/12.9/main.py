# Name: Brian Pavillar
# ID: 1863509

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except ValueError as excpt:
        age = 0
        print('{} {}'.format(name,age))

    # Get next line
    parts = input().split()
    name = parts[0]