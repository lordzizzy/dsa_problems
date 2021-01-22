
import random
import enum

from typing import List


class PivotChoice:
    FIRST = 0
    MID = 1
    LAST = 2


def partition(nums: List[int], begin: int, end: int,
              pivot: PivotChoice = PivotChoice.FIRST) -> int:

    def _partition_use_first_as_pivot(nums: List[int], begin: int, end: int) -> int:
        pivot = nums[begin]
        low = begin + 1
        high = end
        print(f"partition=> pivot: {pivot}, low: {low}, high: {high}")

        while True:
            while low <= high and nums[high] >= pivot:
                high -= 1
            while low <= high and nums[low] <= pivot:
                low += 1
            if low <= high:
                print(
                    f"    swap nums[{low}]: {nums[low]} with nums[{high}]: {nums[high]}")
                nums[low], nums[high] = nums[high], nums[low]
                print_list(nums, indent=4)
            else:
                print(f"    bailing out where low({low})>=high({high})")
                break
        print(
            f"    finally, swap nums[{begin}](pivot): {nums[begin]} with nums[{high}]: {nums[high]}")
        nums[begin], nums[high] = nums[high], nums[begin]
        print_list(nums, indent=4)
        print(f"    returning high: {high}")
        return high

    def _partition_use_mid_as_pivot(nums: List[int], begin: int, end: int) -> int:
        mid = (end-begin)//2
        pivot = nums[mid]
        low = begin
        high = end

        while True:
            while high > mid and nums[high] >= pivot:
                high -= 1
            while low < mid and nums[low] <= pivot:
                low += 1
            if low <= high:
                nums[low], nums[high] = nums[high], nums[low]
            else:
                break
        nums[mid], nums[high] = nums[high], nums[mid]
        return high

    def _partition_use_last_as_pivot(nums: List[int], begin: int, end: int) -> int:
        raise NotImplementedError

    # select implementation
    if pivot == PivotChoice.FIRST:
        return _partition_use_first_as_pivot(nums, begin, end)
    elif pivot == PivotChoice.MID:
        return _partition_use_mid_as_pivot(nums, begin, end)
    else:
        raise NotImplementedError


def quicksort(nums: List[int], begin: int, end: int):
    if (begin >= end):
        return
    p = partition(nums, begin, end, pivot=PivotChoice.FIRST)
    quicksort(nums, begin, p-1)
    quicksort(nums, p+1, end)


def test_quicksort(nums: List[int], expected: List[int]):
    quicksort(nums, 0, len(nums)-1)
    assert nums == expected, \
        f"nums: {print_list(nums)}, expected: {print_list(expected)}"


def print_list(nums: List[int], indent: int):
    if indent:
        print(" " * indent, end="")
    print("[", end="")
    for i in range(0, len(nums)):
        if i < len(nums)-1:
            print(f"{nums[i]},", end="")
        else:
            print(f"{nums[i]}", end="")
    print("]")


if __name__ == "__main__":
    test_quicksort([3, 2, 1, 5, 6, 4], [1, 2, 3, 4, 5, 6])

    # for i in range(0, 10):
    #     nums = [random.randrange(0, 100) for n in range(0, 10)]
    #     check_quicksort(nums, sorted(nums))

    # test partition
    # nums = [80,56,58,49,4,10,59,9,9,28]
    # nums = [3, 2, 1, 5, 6, 4]
    # print_list(nums)
    # print("partition:")
    # partition(nums, 0, len(nums) - 1)
    # print_list(nums)
