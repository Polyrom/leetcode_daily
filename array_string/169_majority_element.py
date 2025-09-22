"""
https://leetcode.com/problems/majority-element/
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

from dataclasses import dataclass
from collections import defaultdict


def majority_element(nums: list[int]) -> int:
    hm = defaultdict(int)
    for n in nums:
        hm[n] += 1
        if hm[n] > len(nums) // 2:
            return n
    return 0


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic", nums=[1], want=1),
        TestCase(name="basic", nums=[3, 2, 3], want=3),
        TestCase(name="basic", nums=[2, 2, 1, 1, 1, 2, 2], want=2),
    ]
    for tc in test_cases:
        got = majority_element(tc.nums)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
