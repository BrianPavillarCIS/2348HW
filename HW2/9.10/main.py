# Name: Brian Pavillar
# ID: 1863509

# With statement, using input1.csv as an example
with open('input1.csv', 'r') as file:

    # Read file
    read_file = file.read()

    # Split List with comma delimiter
    split_file = read_file.split(",")

    # Using set to set apart unique words
    unique_words = set(split_file)

    # Count each instance
    for words in unique_words:
        print(words, split_file.count(words))