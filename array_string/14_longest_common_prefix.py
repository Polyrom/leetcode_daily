"""
https://leetcode.com/problems/longest-common-prefix

14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

from dataclasses import dataclass


def longest_common_prefix(strs: list[str]) -> str:
    common = []
    strs.sort()
    first, last = strs[0], strs[-1]
    if first == last:
        return first
    i = 0
    while i  < min(len(first), len(last)):
        if first[i] == last[i]:
            common.append(first[i])
        else:
            return "".join(common)
        i += 1
    return "".join(common)


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        strs: list[str]
        want: str

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="no common prefix", strs=["dog","racecar","car"], want=""),
        TestCase(name="basic", strs=["flower","flow","flight"], want="fl"),
    ]
    for tc in test_cases:
        got = longest_common_prefix(tc.strs)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
