"""
https://leetcode.com/problems/course-schedule

207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [a_i, b_i] indicates
that you must take course b_i first if you want to take course a_i.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from dataclasses import dataclass


# DFS approach. Time: O(n + e), space: O(e)
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    pre_map = {i: [] for i in range(num_courses)}
    for crs, pre in prerequisites:
        pre_map[crs].append(pre)

    visited = set()

    def dfs(course: int) -> bool:
        if course in visited:
            return False
        if pre_map.get(course) == []:
            return True
        visited.add(course)
        for pre in pre_map[course]:
            if not dfs(pre):
                return False
        visited.remove(course)
        pre_map[course] = []
        return True

    return all(dfs(crs) for crs in range(num_courses))


@dataclass
class TestCase:
    name: str
    num_courses: int
    prerequisites: list[list[int]]
    expected: bool


if __name__ == "__main__":
    test_cases = [
        TestCase(
            name="basic true",
            num_courses=2,
            prerequisites=[[1, 0]],
            expected=True,
        ),
        TestCase(
            name="complicated true",
            num_courses=5,
            prerequisites=[[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]],
            expected=True,
        ),
        TestCase(
            name="basic false",
            num_courses=2,
            prerequisites=[[1, 0], [0, 1]],
            expected=False,
        ),
        TestCase(
            name="complicated false",
            num_courses=3,
            prerequisites=[[1, 0], [2, 1], [0, 2]],
            expected=False,
        ),
    ]
    for tc in test_cases:
        actual = can_finish(tc.num_courses, tc.prerequisites)
        assert actual == tc.expected, f"test case '{tc.name}': {actual=}, {tc.expected=}"
