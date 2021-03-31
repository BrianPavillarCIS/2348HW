# Name: Brian Pavillar
# ID: 1863509

J1 = input("Enter player 1's jersey number:")
R1 = input("Enter player 1's rating:")

J2 = input("Enter player 2's jersey number:")
R2 = input("Enter player 2's rating:")

J3 = input("Enter player 3's jersey number:")
R3 = input("Enter player 3's rating:")

J4 = input("Enter player 4's jersey number:")
R4 = input("Enter player 4's rating:")

J5 = input("Enter player 5's jersey number:")
R5 = input("Enter player 5's rating:")

country_capital = {}

for pair in entries:
    split_pair = pair.split(':')
    country_capital[split_pair[0]] = split_pair[1]
    # country_capital is a dictionary, Ex. { 'Germany': 'Berlin', 'France': 'Paris'

''' Your solution goes here '''

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Spain deleted?', end=' ')
if 'Spain' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Togo deleted?', end=' ')
if 'Togo' in country_capital:
    print('No.')
else:
    print('Yes.')