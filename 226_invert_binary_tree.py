"""
https://leetcode.com/problems/invert-binary-tree

226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
"""

from dataclasses import dataclass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

# DFS, O(n) memory and space
def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None
    root.right, root.left = invert_tree(root.left), invert_tree(root.right)
    return root



if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        tree: TreeNode | None
        expected: TreeNode | None
        assertion_err_msg: str = "'{name}': want={want}, got={got}"

    def build_tree(lst):
        """Builds a binary tree from a list (level-order), using None for missing nodes."""
        if not lst:
            return None
        nodes = [TreeNode(val) for val in lst]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    def trees_equal(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and trees_equal(a.left, b.left) and trees_equal(a.right, b.right)

    test_cases = [
        TestCase(
            name="empty tree",
            tree=None,
            expected=None,
        ),
        TestCase(
            name="single node",
            tree=build_tree([1]),
            expected=build_tree([1]),
        ),
        TestCase(
            name="two levels",
            tree=build_tree([1, 2, 3]),
            expected=build_tree([1, 3, 2]),
        ),
        TestCase(
            name="full three levels",
            tree=build_tree([4, 2, 7, 1, 3, 6, 9]),
            expected=build_tree([4, 7, 2, 9, 6, 3, 1]),
        ),
    ]
    for tc in test_cases:
        got = invert_tree(tc.tree)
        assert trees_equal(got, tc.expected), tc.assertion_err_msg.format(name=tc.name, want=tc.expected, got=got)
