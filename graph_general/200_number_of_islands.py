"""
200. Number of Islands.
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""

from dataclasses import dataclass

WATER = "0"
ISLAND = "1"


# O(m * n) time and space
def number_of_islands(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]

    def dfs(grid: list[list[str]], i: int, j: int) -> None:
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == WATER or visited[i][j]:
            return
        visited[i][j] = True
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == ISLAND and not visited[i][j]:
                dfs(grid, i, j)
                count += 1

    return count


@dataclass
class TestCase:
    grid: list[list[str]]
    expected: int
    assertion_err_msg: str = "want={}, got={got}"


if __name__ == "__main__":
    test_cases = [
        TestCase(
            grid=[
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            expected=1,
        ),
    ]
    for i, tc in enumerate(test_cases, 1):
        result = number_of_islands(tc.grid)
        assert result == tc.expected, f"test case #{i}: {tc.assertion_err_msg.format(want=tc.expected, got=result)}"
