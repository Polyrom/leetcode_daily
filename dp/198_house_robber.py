"""
https://leetcode.com/problems/house-robber

198. House Robber
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
can rob tonight without alerting the police.
"""

from dataclasses import dataclass


def rob(nums: list[int]) -> int:
    n = len(nums)
    if n <= 2:
        return max(nums)

    dp = [0] * n
    dp[0], dp[1] = nums[0], max(nums[:2])
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[n - 1]


@dataclass
class TestCase:
    name: str
    nums: list[int]
    expected: int
    assertion_err_msg: str = "test case '{name}' want={want}, got={got}"


if __name__ == "__main__":
    test_cases = [
        TestCase(name="3", nums=[1, 3], expected=3),
        TestCase(name="4 #1", nums=[1, 2, 3, 1], expected=4),
        TestCase(name="4 #2", nums=[2, 1, 1, 2], expected=4),
        TestCase(name="12", nums=[2, 7, 9, 3, 1], expected=12),
        TestCase(name="2", nums=[1, 1, 1], expected=2),
        TestCase(name="103", nums=[1, 3, 1, 3, 100], expected=103),
    ]
    for i, tc in enumerate(test_cases, 1):
        result = rob(tc.nums)
        assert result == tc.expected, tc.assertion_err_msg.format(name=tc.name, want=tc.expected, got=result)
