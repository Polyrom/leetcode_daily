"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""

from dataclasses import dataclass


# O(n * m) time, O(1) space
def str_str(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i : i + m] == needle:
            return i
    return -1


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        haystack: str
        needle: str
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="found beginning", haystack="sadbutsad", needle="sad", want=0),
        TestCase(name="found middle", haystack="hello", needle="ll", want=2),
        TestCase(name="found middle overlap", haystack="mississippi", needle="issip", want=4),
        TestCase(name="not found", haystack="leetcode", needle="leeto", want=-1),
    ]
    for tc in test_cases:
        got = str_str(tc.haystack, tc.needle)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
