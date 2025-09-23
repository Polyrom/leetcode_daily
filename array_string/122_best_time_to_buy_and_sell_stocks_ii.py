"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

121. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can sell and buy the stock multiple times on the same day,
ensuring you never hold than one share of the stock.

Find and return the maximum profit you can achieve.
"""

from dataclasses import dataclass


# TODO: return when going over DP
# Greedy approach, O(n) time, O(1) memory
def max_profit(prices: list[int]) -> int:
    max_profit = 0
    for i in range(len(prices) - 1):
        if (gain := prices[i + 1] - prices[i]) > 0:
            max_profit += gain
    return max_profit


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        prices: list[int]
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="empty", prices=[], want=0),
        TestCase(name="no profit", prices=[7, 6, 4, 3, 1], want=0),
        TestCase(name="basic", prices=[7, 1, 5, 3, 6, 4], want=7),
    ]
    for tc in test_cases:
        got = max_profit(tc.prices)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
