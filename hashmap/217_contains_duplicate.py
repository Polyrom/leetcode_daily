"""
https://leetcode.com/problems/contains-duplicate

217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
"""

from collections import Counter
from dataclasses import dataclass


def contains_duplicate(nums: list[int]) -> bool:
    return any(v > 1 for v in Counter(nums).values())


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        want: bool

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic has dups", nums=[1, 2, 3, 1], want=True),
        TestCase(name="basic no dups", nums=[2, 66, 4, 123, 33, 1, -3], want=False),
    ]
    for tc in test_cases:
        got = contains_duplicate(tc.nums)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
