# Name: Brian Pavillar
# ID: 1863509

input_vals = input()

numbers = input_vals.split()

list_vals = []
for number in numbers:
    list_vals.append(int(number))

new_list = []

for number in list_vals:
    if number >= 0:
        new_list.append(int(number))

new_list.sort()

for i in new_list:
    print(i, end = " ")

