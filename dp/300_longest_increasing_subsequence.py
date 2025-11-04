"""
https://leetcode.com/problems/longest-increasing-subsequence

300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""

from dataclasses import dataclass


def length_of_LIS(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


@dataclass
class TestCase:
    name: str
    nums: list[int]
    expected: int
    assertion_err_msg: str = "test case '{name}' want={want}, got={got}"


if __name__ == "__main__":
    test_cases = [
        TestCase(name="4 #1", nums=[10, 9, 2, 5, 3, 7, 101, 18], expected=4),
        TestCase(name="4 #2", nums=[0, 1, 0, 3, 2, 3], expected=4),
        TestCase(name="1", nums=[7, 7, 7, 7, 7, 7, 7], expected=1),
    ]
    for i, tc in enumerate(test_cases, 1):
        result = length_of_LIS(tc.nums)
        assert result == tc.expected, tc.assertion_err_msg.format(name=tc.name, want=tc.expected, got=result)
