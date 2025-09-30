"""
https://leetcode.com/problems/binary-tree-level-order-traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

from collections import deque
from dataclasses import dataclass


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    lvls = []
    q = deque([root])

    while q:
        lvl_vals = []

        for _ in range(len(q)):
            node = q.popleft()
            lvl_vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        lvls.append(lvl_vals)

    return lvls


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        root: TreeNode | None
        want: list[list[int]]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(
            name="empty",
            root=None,
            want=[],
        ),
        TestCase(
            name="one node",
            root=TreeNode(3),
            want=[[3]],
        ),
        TestCase(
            name="three-level",
            root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
            want=[[3], [9, 20], [15, 7]],
        ),
    ]
    for tc in test_cases:
        got = level_order(tc.root)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
