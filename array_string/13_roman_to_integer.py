"""
https://leetcode.com/problems/roman-to-integer

13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

from dataclasses import dataclass

roman_to_int_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(s: str) -> int:
    result = 0
    greatest = 0
    for i in range(len(s) - 1, -1, -1):
        num = roman_to_int_map[s[i]]
        if num >= greatest:
            greatest = num
            result += num
        else:
            result -= num
    return result


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        s: str
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="III", s="III", want=3),
        TestCase(name="LVIII", s="LVIII", want=58),
        TestCase(name="MCMXCIV", s="MCMXCIV", want=1994),
    ]
    for tc in test_cases:
        got = roman_to_int(tc.s)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
