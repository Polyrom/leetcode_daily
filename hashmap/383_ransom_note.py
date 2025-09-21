"""
383. Ransom Note
Given two strings ransomNote and magazine, return true if ransomNote can be constructed
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""

from collections import Counter
from dataclasses import dataclass


def can_construct(ransom_note: str, magazine: str) -> bool:
    magazine_map = Counter(magazine)
    for char in ransom_note:
        if not (char_count := magazine_map.get(char)):
            return False
        magazine_map[char] = char_count - 1
    return True


@dataclass
class TestCase:
    ransom_note: str
    magazine: str
    expected: bool


if __name__ == "__main__":
    test_cases = [
        TestCase(ransom_note="a", magazine="b", expected=False),
        TestCase(ransom_note="aa", magazine="ab", expected=False),
        TestCase(ransom_note="faskj", magazine="flkjkjbahh", expected=False),
        TestCase(ransom_note=" ", magazine="   ", expected=True),
    ]
    for tc in test_cases:
        assert can_construct(tc.ransom_note, tc.magazine) == tc.expected
