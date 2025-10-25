"""
https://leetcode.com/problems/longest-consecutive-sequence

128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from dataclasses import dataclass


# Time: O(n). Space: O(n)
def longest_consecutive(nums: list[int]) -> int:
    s = set(nums)
    longest = 0

    for n in s:
        if n - 1 not in s:
            next_num = n + 1
            length = 1
            while next_num in s:
                length += 1
                next_num += 1
            longest = max(longest, length)
    
    return longest


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="4", nums=[100, 4, 200, 1, 3, 2], want=4),
        TestCase(name="8", nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], want=9),
        TestCase(name="3", nums=[1, 0, 1, 2], want=3),
    ]
    for tc in test_cases:
        got = longest_consecutive(tc.nums)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
        
