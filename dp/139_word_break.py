"""
https://leetcode.com/problems/word-break

139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Constraints:

* 1 <= s.length <= 300
* 1 <= wordDict.length <= 1000
* 1 <= wordDict[i].length <= 20
* s and wordDict[i] consist of only lowercase English letters.
* All the strings of wordDict are unique.
"""

from dataclasses import dataclass


def word_break(s: str, word_dict: list[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[n] = True

    for i in range(n - 1, -1, -1):
        for w in word_dict:
            if i + len(w) <= n and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]


@dataclass
class TestCase:
    name: str
    s: str
    word_dict: list[str]
    expected: bool
    assertion_err_msg: str = "test case '{name}' want={want}, got={got}"


if __name__ == "__main__":
    test_cases = [
        TestCase(name="leetcode", s="leetcode", word_dict=["leet", "code"], expected=True),
        TestCase(name="codecodecode", s="codecodecode", word_dict=["leet", "code"], expected=True),
        TestCase(name="applepenapple", s="applepenapple", word_dict=["apple", "pen"], expected=True),
        TestCase(name="catsandog", s="catsandog", word_dict=["cats", "dog", "sand", "and", "cat"], expected=False),
        TestCase(name="aaaaaaa", s="aaaaaaa", word_dict=["aaaa", "aaa"], expected=True),
    ]
    for i, tc in enumerate(test_cases, 1):
        result = word_break(tc.s, tc.word_dict)
        assert result == tc.expected, tc.assertion_err_msg.format(name=tc.name, want=tc.expected, got=result)
