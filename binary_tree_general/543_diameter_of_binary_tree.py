"""
leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

from dataclasses import dataclass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    diameter = 0

    def dfs(node: TreeNode | None) -> int:
        nonlocal diameter

        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    dfs(root)
    return diameter


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        root: TreeNode | None
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic", root=TreeNode(1, TreeNode(2)), want=1),
        TestCase(name="unbalanced", root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)), want=3),
    ]
    for tc in test_cases:
        got = diameter_of_binary_tree(tc.root)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
