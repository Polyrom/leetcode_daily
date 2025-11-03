"""
https://leetcode.com/problems/evaluate-division

399. Evaluate Division
You are given an array of variable pairs equations and an array of real numbers values,
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must
find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries
will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined
for them.
"""

import collections
from dataclasses import dataclass

UNKNOWN_VAR_RESULT = -1.0


def calc_equation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # Step 1. Create a Directed Weighed Graph numerator -> denominator & vice versa
    adj = collections.defaultdict(list)
    for i, (numerator, denominator) in enumerate(equations):
        adj[numerator].append([denominator, values[i]])
        adj[denominator].append([numerator, 1 / values[i]])

    def bfs(src: str, target: str) -> int | float:
        if src not in adj or target not in adj:
            return UNKNOWN_VAR_RESULT
        q, visited = collections.deque([[src, 1]]), {src}
        while q:
            n, w = q.popleft()
            if n == target:
                return w
            for neighbor, weight in adj[n]:
                if neighbor not in visited:
                    q.append([neighbor, w * weight])
                    visited.add(neighbor)
        return UNKNOWN_VAR_RESULT

    # Step 2. Actually calculate results using graph built in step 1
    return [bfs(src, target) for src, target in queries]


@dataclass
class TestCase:
    name: str
    equations: list[list[str]]
    values: list[float]
    queries: list[list[str]]
    expected: list[float]


if __name__ == "__main__":
    test_cases = [
        TestCase(
            name="a, b, c",
            equations=[["a", "b"], ["b", "c"]],
            values=[2.0, 3.0],
            queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            expected=[6.00000, 0.50000, -1.00000, 1.00000, -1.00000],
        ),
        TestCase(
            name="a, b, c, bc, cd",
            equations=[["a", "b"], ["b", "c"], ["bc", "cd"]],
            values=[1.5, 2.5, 5.0],
            queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            expected=[3.75000, 0.40000, 5.00000, 0.20000],
        ),
    ]
    for tc in test_cases:
        actual = calc_equation(tc.equations, tc.values, tc.queries)
        assert actual == tc.expected, f"test case '{tc.name}': {actual=}, {tc.expected=}"
