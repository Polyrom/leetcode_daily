"""
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

from dataclasses import dataclass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS approach. O(n) time, O(n) space
def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)



@dataclass
class TestCase:
    tree1: TreeNode | None
    tree2: TreeNode | None
    expected: bool


def build_tree(data):
    """Helper to build a tree from nested tuples/lists or None."""
    if data is None:
        return None
    val, left, right = data
    return TreeNode(val, build_tree(left), build_tree(right))


if __name__ == "__main__":
    test_cases = [
        # Both trees are None
        TestCase(tree1=None, tree2=None, expected=True),
        # Both trees are single node with same value
        TestCase(tree1=TreeNode(1), tree2=TreeNode(1), expected=True),
        # Both trees are single node with different value
        TestCase(tree1=TreeNode(1), tree2=TreeNode(2), expected=False),
        # Trees with same structure and values
        TestCase(
            tree1=build_tree((1, (2, None, None), (3, None, None))),
            tree2=build_tree((1, (2, None, None), (3, None, None))),
            expected=True,
        ),
        # Trees with different structure
        TestCase(
            tree1=build_tree((1, (2, None, None), None)),
            tree2=build_tree((1, None, (2, None, None))),
            expected=False,
        ),
        # Trees with same structure but different values
        TestCase(
            tree1=build_tree((1, (2, None, None), (1, None, None))),
            tree2=build_tree((1, (2, None, None), (3, None, None))),
            expected=False,
        ),
        # One tree is None, the other is not
        TestCase(tree1=None, tree2=TreeNode(0), expected=False),
        TestCase(tree1=TreeNode(0), tree2=None, expected=False),
    ]
    for tc in test_cases:
        assert is_same_tree(tc.tree1, tc.tree2) == tc.expected
