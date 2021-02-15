# Bubble sort
# Stable (leaves relative ordering of 'equal' elements intact)
# In-place (input is sorted and modified "in place")
# Runtime: O(N^2) average and worst case, best case O(N)
# Memory: O(1)


from typing import Callable, List
from termcolor import colored

import random


def bubble_sort_simple(nums: List[int]) -> None:
    n = len(nums)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def bubble_sort_optimized(nums: List[int]) -> None:
    n = len(nums) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = False
        n -= 1


SortFunc = Callable[[List[int]], None]


def test_sort(func: SortFunc, nums: List[int], expected: List[int]):
    original = list(nums)
    func(nums)
    if nums == expected:
        print(
            colored(f"PASSED {func.__name__} => {original} sorted is {nums}", "green")
        )
    else:
        print(
            colored(
                f"PASSED {func.__name__} => {original} sorted is {nums}, but expected {expected}",
                "red",
            )
        )


if __name__ == "__main__":
    random_numbers = [random.randrange(0, 99) for _ in range(0, 10)]
    test_sort(bubble_sort_simple, random_numbers, sorted(random_numbers))
    test_sort(bubble_sort_optimized, random_numbers, sorted(random_numbers))
