"""
https://leetcode.com/problems/maximum-subarray

53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

from dataclasses import dataclass


# Kadane's algorithm
def max_sub_array(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


@dataclass
class TestCase:
    name: str
    nums: list[int]
    expected: int


if __name__ == "__main__":
    test_cases = [
        TestCase(name="1", nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4], expected=6),
        TestCase(name="2", nums=[1], expected=1),
        TestCase(name="3", nums=[5, 4, -1, 7, 8], expected=23),
    ]
    for tc in test_cases:
        actual = max_sub_array(tc.nums)
        assert actual == tc.expected, f"Test case '{tc.name}': {actual=}, expected={tc.expected}"
