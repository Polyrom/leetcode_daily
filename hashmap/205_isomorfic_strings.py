"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""

from dataclasses import dataclass


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_chars = {}
    t_chars = {}
    for i in range(len(s)):
        if s[i] not in s_chars:
            s_chars[s[i]] = i
        if t[i] not in t_chars:
            t_chars[t[i]] = i
        if s_chars[s[i]] != t_chars[t[i]]:
            return False
    return True


def is_isomorphic_new(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    if len(set(s)) != len(set(t)):
        return False

    s_to_t = {}
    for i in range(len(s)):
        if (char_t := s_to_t.get(s[i])) and char_t != t[i]:
            return False
        s_to_t[s[i]] = t[i]
    return True


@dataclass
class TestCase:
    s1: str
    s2: str
    expected: bool


if __name__ == "__main__":
    test_cases = [
        TestCase(s1="add", s2="egg", expected=True),
        TestCase(s1="add", s2="ega", expected=False),
        TestCase(s1="foo", s2="bar", expected=False),
        TestCase(s1="germ", s2="germ", expected=True),
    ]
    for i, tc in enumerate(test_cases, 1):
        assert is_isomorphic(tc.s1, tc.s2) == tc.expected, f"test case #{i} failed"
        assert is_isomorphic_new(tc.s1, tc.s2) == tc.expected, f"test case #{i} failed"
