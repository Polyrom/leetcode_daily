"""
https://leetcode.com/problems/length-of-last-word

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""

from dataclasses import dataclass

WHITESPACE = " "


def length_of_last_word(s: str) -> int:
    count = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == WHITESPACE and count != 0:
            return count
        if s[i] != WHITESPACE:
            count += 1
    return count


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        s: str
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="two words", s="Hello World", want=5),
        TestCase(name="multiple words", s="luffy is still joyboy", want=6),
        TestCase(name="spaces all over the place", s="   fly me   to   the moon  ", want=4),
        TestCase(name="all spaces", s="       ", want=0),
    ]
    for tc in test_cases:
        got = length_of_last_word(tc.s)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
