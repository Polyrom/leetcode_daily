"""
https://leetcode.com/problems/climbing-stairs

70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

from dataclasses import dataclass


# Fundamental DP problem
def climb_stairs(n: int) -> int:
    if n <= 3:
        return n

    dp = [-1] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = sum(dp[i - 2 : i])
    return dp[n]


@dataclass
class TestCase:
    name: str
    n: int
    expected: int
    assertion_err_msg: str = "test case '{name}' want={want}, got={got}"


if __name__ == "__main__":
    test_cases = [
        TestCase(name="2", n=2, expected=2),
        TestCase(name="3", n=3, expected=3),
        TestCase(name="5", n=5, expected=8),
    ]
    for i, tc in enumerate(test_cases, 1):
        result = climb_stairs(tc.n)
        assert result == tc.expected, tc.assertion_err_msg.format(name=tc.name, want=tc.expected, got=result)
