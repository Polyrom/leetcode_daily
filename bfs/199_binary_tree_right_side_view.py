"""
https://leetcode.com/problems/binary-tree-right-side-view

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
you can see ordered from top to bottom.
"""

from collections import deque
from dataclasses import dataclass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time and space
def right_side_view(root: TreeNode | None) -> list[int]:
    if not root:
        return []

    right_nodes = []
    q = deque([root])

    while q:
        lvl_len = len(q)

        for _ in range(lvl_len):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        right_nodes.append(node.val)

    return right_nodes


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        root: TreeNode | None
        want: list[int]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(
            name="empty",
            root=None,
            want=[],
        ),
        TestCase(
            name="four right nodes",
            root=TreeNode(
                1,
                left=TreeNode(2, left=None, right=TreeNode(5)),
                right=TreeNode(
                    3,
                    left=None,
                    right=TreeNode(4),
                ),
            ),
            want=[1, 3, 4],
        ),
        TestCase(
            name="two right nodes",
            root=TreeNode(1, left=TreeNode(2, left=TreeNode(4, left=TreeNode(5))), right=TreeNode(3)),
            want=[1, 3, 4, 5],
        ),
    ]
    for tc in test_cases:
        got = right_side_view(tc.root)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
