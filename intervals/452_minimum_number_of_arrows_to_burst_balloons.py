"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

452. Minimum Number of Arrows to Burst Balloons

There are some spherical balloons taped onto a flat wall that represents the XY-plane.
The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon
whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely,
bursting any balloons in its path.
Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Constraints:
* 1 <= points.length <= 10^5
* points[i].length == 2
* -23^1 <= xstart < xend <= 23^1 - 1
"""

from dataclasses import dataclass


# Time: O(n logn), space: O(1)
def find_min_arrow_shots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[1])
    arrows = 1
    curr = points[0][1]
    for start, end in points[1:]:
        if start > curr:
            arrows += 1
            curr = end
    return arrows


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        points: list[list[int]]
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="2 arrows #1", points=[[10, 16], [2, 8], [1, 6], [7, 12]], want=2),
        TestCase(name="2 arrows #2", points=[[1, 2], [2, 3], [3, 4], [4, 5]], want=2),
        TestCase(
            name="2 arrows #3",
            points=[[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]],
            want=2,
        ),
        TestCase(name="4 arrows", points=[[1, 2], [3, 4], [5, 6], [7, 8]], want=4),
    ]
    for tc in test_cases:
        got = find_min_arrow_shots(tc.points)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
