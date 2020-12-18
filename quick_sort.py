# Quick Sort
# Runtime: O(n log(n)) average, O(n^2) worst case
# Memory: O(log(n))
#
# QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array
# around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.
#
# 1. Always pick first element as pivot.
# 2. Always pick last element as pivot (implemented below)
# 3. Pick a random element as pivot.
# 4. Pick median as pivot.
#
# The key process in quickSort is partition(). Target of partitions is, given an array and an element x of
# array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x)
# before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

import random


partition_count = 0
swap_count = 0


# Python program for implementation of Quicksort Sort
#
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(numbers, low, high):
    global partition_count, swap_count
    idx = low - 1
    pivot = numbers[high]
    print(f'\trunning partition {partition_count} with pivot as {pivot}')

    for j in range(low, high):
        if numbers[j] <= pivot:
            idx = idx + 1
            numbers[idx], numbers[j] = numbers[j], numbers[idx]
            swap_count += 1
            print(f'\t\tfor j is {j}, idx is {idx} => swap {numbers[j]} with {numbers[idx]}, numbers: {numbers}')

    numbers[idx+1], numbers[high] = numbers[high], numbers[idx+1]
    print(f'\tswap {numbers[high]} with {numbers[idx+1]}, numbers: {numbers}')
    swap_count += 1
    partition_count += 1
    return idx + 1


def quick_sort(numbers, low, high):
    if len(numbers) == 1:
        return numbers
    if low < high:
        partition_index = partition(numbers, low, high)

        quick_sort(numbers, low, [partition_index - 1])
        quick_sort(numbers, partition_index + 1, high)


if __name__ == '__main__':
    rand_numbers = [random.randrange(0, 100) for num in range(0, 10)]
    print('numbers: ', rand_numbers)
    partition(rand_numbers, 0, len(rand_numbers) - 1)
    print('numbers after partition: ', rand_numbers)
    print('particular ', partition_count)
