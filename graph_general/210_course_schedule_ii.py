"""
https://leetcode.com/problems/course-schedule-ii

210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates
that you must take course b_i first if you want to take course a_i.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.
"""

from dataclasses import dataclass


# Basically, a topological sorting problem
def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    pre_map = {i: [] for i in range(num_courses)}
    for pre, crs in prerequisites:
        pre_map[pre].append(crs)
    path = []
    visited, cycle = set(), set()

    def dfs(crs: int) -> bool:
        if crs in cycle:
            return False
        if crs in visited:
            return True
        cycle.add(crs)
        for pre in pre_map[crs]:
            if dfs(pre) is False:
                return False
        cycle.remove(crs)
        visited.add(crs)
        path.append(crs)
        return True

    for crs in range(num_courses):
        if not dfs(crs):
            return []
    return path


@dataclass
class TestCase:
    name: str
    num_courses: int
    prerequisites: list[list[int]]
    expected: list[list[int]]


if __name__ == "__main__":
    test_cases = [
        TestCase(
            name="basic true",
            num_courses=2,
            prerequisites=[[1, 0]],
            expected=[[0, 1]],
        ),
        TestCase(
            name="complicated true",
            num_courses=5,
            prerequisites=[[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]],
            expected=[[4, 3, 1, 2, 0]],
        ),
        TestCase(
            name="basic false",
            num_courses=2,
            prerequisites=[[1, 0], [0, 1]],
            expected=[[]],
        ),
        TestCase(
            name="complicated false",
            num_courses=3,
            prerequisites=[[1, 0], [2, 1], [0, 2]],
            expected=[[]],
        ),
    ]
    for tc in test_cases:
        actual = find_order(tc.num_courses, tc.prerequisites)
        assert actual in tc.expected, f"test case '{tc.name}': {actual=}, {tc.expected=}"
