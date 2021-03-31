# Name: Brian Pavillar
# ID: 1863509

input_vals = input()

# Split List with comma delimiter
split_list = input_vals.split(" ")

# Count each instance
for words in split_list:
    print(words, split_list.count(words))
