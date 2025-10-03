"""
https://leetcode.com/problems/surrounded-regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region
cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board.
You do not need to return anything.
"""

from collections import deque
from copy import deepcopy
from dataclasses import dataclass

UNCAPTURED = "O"
CAPTURED = "X"
MARKED = "#"


def is_in_bounds(n: int, m: int, i: int, j: int) -> bool:
    return 0 <= i < n and 0 <= j < m


# O(n * m) time and space
def solve(board: list[list[str]]) -> None:
    n = len(board)
    m = len(board[0])
    q = deque()

    for j in range(m):
        if board[0][j] == UNCAPTURED:
            q.append((0, j))
            board[0][j] = MARKED
        if board[n - 1][j] == UNCAPTURED:
            q.append((n - 1, j))
            board[n - 1][j] = MARKED

    for i in range(n - 1):
        if board[i][0] == UNCAPTURED:
            q.append((i, 0))
            board[i][0] = MARKED
        if board[i][m - 1] == UNCAPTURED:
            q.append((i, m - 1))
            board[i][m - 1] = MARKED

    while q:
        i, j = q.popleft()

        for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if is_in_bounds(n, m, ii, jj) and board[ii][jj] == UNCAPTURED:
                board[ii][jj] = MARKED
                q.append((ii, jj))

    for i in range(n):
        for j in range(m):
            if board[i][j] == UNCAPTURED:
                board[i][j] = CAPTURED
            if board[i][j] == MARKED:
                board[i][j] = UNCAPTURED


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        board: list[list[str]]
        want: list[list[str]]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(
            name="one square",
            board=[["X"]],
            want=[["X"]],
        ),
        TestCase(
            name="basic",
            board=[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
            want=[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]],
        ),
    ]
    for tc in test_cases:
        board_cp = deepcopy(tc.board)
        solve(board_cp)
        assert board_cp == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=board_cp)
