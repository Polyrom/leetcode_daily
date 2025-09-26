"""
https://leetcode.com/problems/two-sum

1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from dataclasses import dataclass


def two_sum(nums: list[int], target: int) -> list[int]:
    hm = {}
    for i, n in enumerate(nums):
        diff = target - n
        if (diff_idx := hm.get(diff)) is not None:
            return [diff_idx, i]
        hm[n] = i
    return [0, 0]


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        target: int
        want: list[int]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic", nums=[2, 7, 11, 15], target=9, want=[0, 1]),
        TestCase(name="basic short", nums=[3, 3], target=6, want=[0, 1]),
        TestCase(name="basic again", nums=[3, 2, 4], target=6, want=[1, 2]),
    ]
    for tc in test_cases:
        got = two_sum(tc.nums, tc.target)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
