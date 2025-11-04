"""
https://leetcode.com/problems/coin-change/description

322. Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Constraints:

* 1 <= coins.length <= 12
* 1 <= coins[i] <= 2^31 - 1
* 0 <= amount <= 10^4
"""

from dataclasses import dataclass


def coin_change(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
       for c in coins:
          if a - c >= 0:
             dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != amount + 1 else -1


@dataclass
class TestCase:
    name: str
    coins: list[int]
    amount: int
    expected: int
    assertion_err_msg: str = "test case '{name}' want={want}, got={got}"


if __name__ == "__main__":
    test_cases = [
        TestCase(name="zero", coins=[1], amount=0, expected=0),
        TestCase(name="not enough change", coins=[2], amount=3, expected=-1),
        TestCase(name="enough change", coins=[1, 2, 5], amount=11, expected=3),
    ]
    for i, tc in enumerate(test_cases, 1):
        result = coin_change(tc.coins, tc.amount)
        assert result == tc.expected, tc.assertion_err_msg.format(name=tc.name, want=tc.expected, got=result)
