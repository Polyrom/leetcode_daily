"""
https://leetcode.com/problems/merge-intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

from dataclasses import dataclass


def merge(intervals: list[list[int]]) -> list[list[int]]:
    merged = []
    for interval in sorted(intervals, key=lambda i: i[0]):
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(interval[1], merged[-1][1])
    return merged


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        intervals: list[list[int]]
        want: list[list[int]]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic", intervals=[[1, 3], [2, 6], [8, 10], [15, 18]], want=[[1, 6], [8, 10], [15, 18]]),
        TestCase(name="shrink into one", intervals=[[1, 4], [4, 5]], want=[[1, 5]]),
        TestCase(name="inverted", intervals=[[4, 7], [1, 4]], want=[[1, 7]]),
    ]
    for tc in test_cases:
        got = merge(tc.intervals)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
