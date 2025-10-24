"""
https://leetcode.com/problems/happy-number

202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which
  does not include 1.

Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Constraints:
1 <= n <= 231 - 1
"""

from dataclasses import dataclass


def is_happy(n: int) -> bool:
    visited = set()
    while n != 1:
        if n in visited:
            return False
        visited.add(n)
        n = sum(int(x) ** 2 for x in str(n))
    return True


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        n: int
        want: bool

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="happy", n=19, want=True),
        TestCase(name="unhappy", n=2, want=False),
    ]
    for tc in test_cases:
        got = is_happy(tc.n)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
        
