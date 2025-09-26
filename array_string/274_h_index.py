"""
https://leetcode.com/problems/h-index

274. H-Index
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith
paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia:
The h-index is defined as the maximum value of h such that the given researcher has published at least h papers
that have each been cited at least h times.
"""

from dataclasses import dataclass


# O(log n) time, O(1) space
def h_index(citations: list[int]) -> int:
    n = len(citations)
    citations.sort()
    for i, cit in enumerate(citations):
        if n - i <= cit:
            return n - i
    return 0


# O(n) time, O(n) space
def h_index_1(citations: list[int]) -> int:
    n = len(citations)
    tmp = [0] * (n + 1)
    for i, cit in enumerate(citations):
        if cit > n:
            tmp[n] += 1
        else:
            tmp[cit] += 1
    total = 0
    for i in range(n, -1, -1):
        total += tmp[i]
        if total >= i:
            return i
    return 0


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        citations: list[int]
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic short", citations=[1, 3, 1], want=1),
        TestCase(name="basic longer", citations=[1, 3, 0, 6, 1, 5], want=3),
    ]
    for tc in test_cases:
        got = h_index(tc.citations)
        got_1 = h_index_1(tc.citations)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
        assert got_1 == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got_1)
