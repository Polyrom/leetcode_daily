"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).
"""

from collections import deque
from dataclasses import dataclass


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val: int = val
        self.left: "TreeNode | None" = left
        self.right: "TreeNode | None" = right


# Time: O(n)
def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    levels = []
    q = deque([root])
    is_left_to_right = True
    while q:
        level = deque()
        level_len = len(q)
        for _ in range(level_len):
            item = q.popleft()
            if is_left_to_right:
                level.append(item.val)
            else:
                level.appendleft(item.val)
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
        levels.append(list(level))
        is_left_to_right = not is_left_to_right
    return levels


@dataclass
class TestCase:
    name: str
    root: TreeNode | None
    expected: list[list[int]]


if __name__ == "__main__":
    test_cases = [
        TestCase(name="empty", root=None, expected=[]),
        TestCase(name="single_node", root=TreeNode(1), expected=[[1]]),
        TestCase(
            name="basic",
            root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
            expected=[[3], [20, 9], [15, 7]],
        ),
        TestCase(
            name="left_skewed",
            root=TreeNode(1, TreeNode(2, TreeNode(3))),
            expected=[[1], [2], [3]],
        ),
        TestCase(
            name="complete_tree",
            root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))),
            expected=[[1], [3, 2], [4, 5, 6, 7]],
        ),
    ]
    for tc in test_cases:
        got = zigzag_level_order(tc.root)
        assert got == tc.expected, f"{tc.name}: got={got}, expected={tc.expected}"
