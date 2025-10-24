"""
https://leetcode.com/problems/group-anagrams

49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

from dataclasses import dataclass
from collections import Counter


# O(n * (m * log m)) time, O(n) space
def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams_grouped = {}
    for word in strs:
        word_sorted = "".join(sorted(word))
        if word_sorted not in anagrams_grouped:
            anagrams_grouped[word_sorted] = [word]
        else:
            anagrams_grouped[word_sorted].append(word)
    return list(anagrams_grouped.values())


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        strs: list[str]
        want: list[list[str]]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(
            name="basic",
            strs=["eat", "tea", "tan", "ate", "nat", "bat"],
            want=[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        TestCase(
            name="empty",
            strs=[""],
            want=[[""]],
        ),
        TestCase(
            name="one element",
            strs=["a"],
            want=[["a"]],
        ),
    ]
    def normalize(groups: list[list[str]]) -> Counter:
        # sort each inner group and convert to tuple so they can be counted
        return Counter(tuple(sorted(g)) for g in groups)

    for tc in test_cases:
        got = group_anagrams(tc.strs)
        got_n = normalize(got)
        want_n = normalize(tc.want)
        assert got_n == want_n, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
        
