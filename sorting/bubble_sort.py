# Bubble sort
# Runtime: O(N^2) average and worst case
# Memory: O(1)

import random


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


if __name__ == "__main__":
    random_numbers = [random.randrange(0, 99) for num in range(0, 10)]
    print('list before sorting: ', random_numbers)
    bubble_sort(random_numbers)
    print('list after sorting: ', random_numbers)
