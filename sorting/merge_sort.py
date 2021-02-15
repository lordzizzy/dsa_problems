# Merge sort
# Stable sort
# Non In-place
# Runtime: O(N LogN)
# Memory: O(N)

from typing import Callable, List
from termcolor import colored

import random

# Implemented with ideas from:
# https://stackoverflow.com/questions/18761766/mergesort-with-python
def mergesort_simple(nums: List[int]) -> List[int]:
    def merge(left: List[int], b: List[int]) -> List[int]:
        res = []
        i = j = 0
        while i < len(left) and j < len(b):
            if left[i] < b[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        res += left[i:]
        res += b[j:]
        return res

    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    l = mergesort_simple(nums[:mid])
    r = mergesort_simple(nums[mid:])
    return merge(l, r)


SortFunc = Callable[[List[int]], List[int]]


def test_sort(func: SortFunc, nums: List[int], expected: List[int]):
    r = func(nums)
    if r == expected:
        print(colored(f"PASSED {func.__name__} => {nums} sorted is {r}", "green"))
    else:
        print(
            colored(
                f"FAILED {func.__name__} => {nums} sorted is {r}, but expected: {expected}",
                "red",
            )
        )


if __name__ == "__main__":
    rand_nums = [random.randint(1, 99) for _ in range(10)]
    test_sort(mergesort_simple, rand_nums, sorted(rand_nums))