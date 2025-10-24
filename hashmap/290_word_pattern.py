"""
https://leetcode.com/problems/word-pattern

290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
"""

from dataclasses import dataclass


# O(n) time, O(n) space
def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    if len(set(pattern)) != len(set(words)):
        return False
    
    char_to_word_map = {}
    for i in range(len(pattern)):
        if (matching_word := char_to_word_map.get(pattern[i])) and matching_word != words[i]:
            return False
        char_to_word_map[pattern[i]] = words[i]

    return True


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        pattern: str
        s: str
        want: bool

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="abba__true", pattern="abba", s="dog cat cat dog", want=True),
        TestCase(name="abba__false1", pattern="abba", s="dog dog dog dog", want=False),
        TestCase(name="abba__false2", pattern="abba", s="dog cat cat fish", want=False),
        TestCase(name="aaaa__false", pattern="aaaa", s="dog cat cat dog", want=False),
    ]
    for tc in test_cases:
        got = word_pattern(tc.pattern, tc.s)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
        
