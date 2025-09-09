"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
from curses.ascii import isalnum
from dataclasses import dataclass


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while not isalnum(s[left]) and left < right:
            left += 1
        while not isalnum(s[right]) and left < right:
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


@dataclass
class TestCase:
    s: str
    expected: bool


if __name__ == '__main__':
    test_cases = [
        TestCase(s='A man, a plan, a canal: Panama', expected=True),
        TestCase(s='race a car', expected=False),
        TestCase(s=' ', expected=True),
        TestCase(s='898898', expected=True),
        TestCase(s='!, ?&*+-', expected=True),
    ]
    for tc in test_cases:
        assert is_palindrome(tc.s) == tc.expected
