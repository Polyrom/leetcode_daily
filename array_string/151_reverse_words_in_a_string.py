"""
https://leetcode.com/problems/reverse-words-in-a-string

151. Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

from dataclasses import dataclass

WHITESPACE = " "


# Time: O(n). Space: O(n)
def reverse_words(s: str) -> str:
    words = [w.strip() for w in s.strip().split(WHITESPACE) if w]
    i, j = 0, len(words) - 1
    while i <= j:
        words[i], words[j] = words[j], words[i]
        i += 1
        j -= 1

    return WHITESPACE.join(words)


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        s: str
        want: str

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic", s="the sky is blue", want="blue is sky the"),
        TestCase(name="leading/trailing spaces", s="  hello world  ", want="world hello"),
        TestCase(name="extra spaces between words", s="a good   example", want="example good a"),
        TestCase(name="one word", s=" example   ", want="example"),
    ]
    for tc in test_cases:
        got = reverse_words(tc.s)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
