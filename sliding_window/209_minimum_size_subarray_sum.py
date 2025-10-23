"""
https://leetcode.com/problems/minimum-size-subarray-sum

209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose
sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Constraints:

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
"""

from dataclasses import dataclass


MAX_LEN = 100_001  # from problem constraints, and to avoid type hint warnings while using float("inf")


# O(n) time, O(1) space
def min_sub_array_len(target: int, nums: list[int]) -> int:
    min_len = MAX_LEN
    current_window_sum = 0
    left = 0
    for right in range(len(nums)):
        current_window_sum += nums[right]
        while current_window_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_window_sum -= nums[left]
            left += 1
    return min_len if min_len != MAX_LEN else 0


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        target: int
        nums: list[int]
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="multiple", target=7, nums=[2, 3, 1, 2, 4, 3], want=2),
        TestCase(name="single", target=4, nums=[1, 4, 4], want=1),
        TestCase(name="none", target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1], want=0),
    ]
    for tc in test_cases:
        got = min_sub_array_len(tc.target, tc.nums)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
