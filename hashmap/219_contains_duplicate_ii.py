"""
https://leetcode.com/problems/contains-duplicate-ii

219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from dataclasses import dataclass


# O(n) time, O(n) space
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    occurences = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in occurences and abs(occurences[num] - i) <= k:
            return True
        occurences[num] = i
    return False


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        k: int
        want: bool

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic_true", nums=[1, 2, 3, 1], k=3, want=True),
        TestCase(name="ones_zeroes_true", nums=[1, 0, 1, 1], k=1, want=True),
        TestCase(name="basic_false", nums=[1, 2, 3, 1, 2, 3], k=2, want=False),
    ]
    for tc in test_cases:
        got = contains_nearby_duplicate(tc.nums, tc.k)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
        
