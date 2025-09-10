"""
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.
"""

from collections import deque
from dataclasses import dataclass


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


# BFS approach, iterative: O(n) time, O(n) space
def max_depth_bfs(root: TreeNode | None) -> int:
    if not root:
        return 0
    q = deque()
    q.append(root)
    depth = 0

    while q:
        depth += 1

        for _ in range(len(q)):
            cur_node = q.popleft()
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)

    return depth


# DFS approach, iterative: O(n) time, O(n) space
def max_depth_dfs(root: TreeNode | None) -> int:
    if not root:
        return 0
    return 1 + max(max_depth_dfs(root.left), max_depth_dfs(root.right))


@dataclass
class TestCase:
    tree: TreeNode | None
    expected: int


if __name__ == "__main__":
    test_cases = [
        # Empty tree
        TestCase(tree=None, expected=0),
        # Single node tree
        TestCase(tree=TreeNode(1), expected=1),
        # Two-level tree
        TestCase(tree=TreeNode(1, TreeNode(2)), expected=2),
        # Complete binary tree of depth 3
        TestCase(
            tree=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))),
            expected=3,
        ),
        # Left-skewed tree
        TestCase(tree=TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)))), expected=4),
        # Right-skewed tree
        TestCase(tree=TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4)))), expected=4),
        # Unbalanced tree
        TestCase(tree=TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4)), expected=3),
    ]
    for tc in test_cases:
        assert max_depth_bfs(tc.tree) == tc.expected
        assert max_depth_dfs(tc.tree) == tc.expected
