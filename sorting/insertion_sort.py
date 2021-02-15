# Insertion sort
# Stable: yes
# In-place: yes
# Runtime: O(N²)
# Memory: O(1)

from typing import Callable, List
from termcolor import colored

import random


def insertion_sort(nums: List[int]) -> None:
    n = len(nums)
    if n < 2:
        return
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


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
                f"PASSED {func.__name__} => {original} sorted is {nums}, but expected: {expected}",
                "red",
            )
        )


if __name__ == "__main__":
    rand_nums = [random.randint(1, 99) for _ in range(10)]
    test_sort(insertion_sort, rand_nums, sorted(rand_nums))