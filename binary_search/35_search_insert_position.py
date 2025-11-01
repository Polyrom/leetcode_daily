"""
https://leetcode.com/problems/search-insert-position

35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from dataclasses import dataclass


# Classic binary search implementation: O(log n) time, O(1) space.
# It is guaranteed that the insertion position is always at left, because throughout the algo we always maintain
# the invariant where elements at nums[< left] < target.
def search_insert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        target: int
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="5", nums=[1, 3, 5, 6], target=5, want=2),
        TestCase(name="2", nums=[1, 3, 5, 6], target=2, want=1),
        TestCase(name="7", nums=[1, 3, 5, 6], target=7, want=4),
    ]
    for tc in test_cases:
        got = search_insert(tc.nums, tc.target)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
