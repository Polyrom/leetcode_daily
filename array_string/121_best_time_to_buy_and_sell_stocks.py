"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from dataclasses import dataclass


def max_profit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    max_profit = 0
    min_price = prices[0]
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
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
        TestCase(name="basic", prices=[7, 1, 5, 3, 6, 4], want=5),
    ]
    for tc in test_cases:
        got = max_profit(tc.prices)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
