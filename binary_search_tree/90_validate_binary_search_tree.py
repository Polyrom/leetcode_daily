"""
https://leetcode.com/problems/validate-binary-search-tree

98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Constraints:
* The number of nodes in the tree is in the range [1, 10^4].
* -231 <= Node.val <= 231 - 1
"""

from dataclasses import dataclass
from typing import Optional

Number = int | float


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def is_valid(node: Optional[TreeNode], left: Number, right: Number) -> bool:
        if not node:
            return True
        if left >= node.val or right <= node.val:
            return False

        return is_valid(node.left, left, node.val) and is_valid(node.right, node.val, right)

    return is_valid(root, float("-inf"), float("inf"))


@dataclass
class TestCase:
    name: str
    root: Optional[TreeNode]
    expected: bool


if __name__ == "__main__":
    test_cases = [
        TestCase(
            name="basic valid BST",
            root=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
            expected=True,
        ),
        TestCase(
            name="basic invalid BST",
            root=TreeNode(
                5,
                left=TreeNode(1),
                right=TreeNode(4, left=TreeNode(3), right=TreeNode(6)),
            ),
            expected=False,
        ),
        TestCase(
            name="all twos invalid BST",
            root=TreeNode(
                2,
                left=TreeNode(2),
                right=TreeNode(2),
            ),
            expected=False,
        ),
        TestCase(
            name="more complicated invalid BST",
            root=TreeNode(
                5,
                left=TreeNode(4),
                right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)),
            ),
            expected=False,
        ),
    ]
    for tc in test_cases:
        actual = is_valid_bst(tc.root)
        assert actual == tc.expected, f"{tc.name}: {tc.expected=}, {actual=}"
