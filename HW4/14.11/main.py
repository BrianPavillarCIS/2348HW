# Name: Brian Pavillar
# ID: 1863509

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_largest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_largest]:
                index_largest = j
                print(numbers)

        temp = numbers[i]
        numbers[i] = numbers[index_largest]
        numbers[index_largest] = temp


if __name__ == "__main__":
    # List Comprehension to read input into list
    numbers = [int(num) for num in input().split()]
    selection_sort_descend_trace(numbers)