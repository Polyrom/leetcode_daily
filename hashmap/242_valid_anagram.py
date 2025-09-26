"""
https://leetcode.com/problems/valid-anagram

242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

from collections import Counter
from dataclasses import dataclass


def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        s: str
        t: str
        want: bool

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase("basic true", s="anagram", t="ramgana", want=True),
        TestCase("basic false", s="tata", t="fsdf", want=False),
    ]
    for tc in test_cases:
        got = valid_anagram(tc.t, tc.s)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
