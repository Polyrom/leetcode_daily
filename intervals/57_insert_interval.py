"""
57. Insert Interval
You are given an array of non-overlapping intervals intervals where intervals[i] = [start.i, end.i]
represent the start and the end of the ith interval and intervals is sorted in ascending order by start.i.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start.i and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.

Constraints:

* 0 <= intervals.length <= 10^4
* intervals[i].length == 2
* 0 <= start.i <= end.i <= 10^5
* intervals is sorted by start.i in ascending order.
* newInterval.length == 2
* 0 <= start <= end <= 10^5
"""

from dataclasses import dataclass


# O(n) time, O(1) space
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    merged = []
    n = len(intervals)
    i = 0
    while i < n and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    merged.append(new_interval)
    while i < n:
        merged.append(intervals[i])
        i += 1
    return merged


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        intervals: list[list[int]]
        new_interval: list[int]
        want: list[list[int]]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic", intervals=[[1, 3], [6, 9]], new_interval=[2, 5], want=[[1, 5], [6, 9]]),
        TestCase(
            name="complex",
            intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            new_interval=[4, 8],
            want=[[1, 2], [3, 10], [12, 16]],
        ),
    ]
    for tc in test_cases:
        got = insert(tc.intervals, tc.new_interval)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
