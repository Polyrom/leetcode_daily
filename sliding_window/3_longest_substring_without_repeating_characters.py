"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
"""

from dataclasses import dataclass


# O(n) time, O(n) amortized space (if all characters are unique)
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    result = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        s: str
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="beginning", s="abcabcbb", want=3),
        TestCase(name="middle", s="pwwkew", want=3),
        TestCase(name="repeating", s="pppppppp", want=1),
    ]
    for tc in test_cases:
        got = length_of_longest_substring(tc.s)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
