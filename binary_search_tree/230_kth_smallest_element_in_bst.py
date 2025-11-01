"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst

230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest
value (1-indexed) of all the values of the nodes in the tree.

Constraints:
The number of nodes in the tree is n.
* 1 <= k <= n <= 104
* 0 <= Node.val <= 104
"""

from dataclasses import dataclass
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


# Iterative approach. O(n) time, O(n) space
def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    n = 0
    stack: list[TreeNode] = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        n += 1
        if n == k:
            return curr.val
        curr = curr.right
    return -1


@dataclass
class TestCase:
    name: str
    root: Optional[TreeNode]
    k: int
    expected: int


if __name__ == "__main__":
    test_cases = [
        TestCase(
            name="k=1",
            root=TreeNode(3, left=TreeNode(1, left=None, right=TreeNode(2)), right=TreeNode(4)),
            k=1,
            expected=1,
        ),
        TestCase(
            name="k=3",
            root=TreeNode(
                5,
                left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)),
                right=TreeNode(6),
            ),
            k=3,
            expected=3,
        ),
    ]
    for tc in test_cases:
        actual = kth_smallest(tc.root, tc.k)
        assert actual == tc.expected, f"{tc.name}: {tc.expected=}, {actual=}"
