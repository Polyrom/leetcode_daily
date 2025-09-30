"""
https://leetcode.com/problems/average-of-levels-in-binary-tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10^-5 of the actual answer will be accepted.
"""

from collections import deque
from dataclasses import dataclass


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


# O(n) time, O(w) space, where w is tree width, O(n) worst-case
def average_of_levels(root: TreeNode | None) -> list[float]:
    if not root:
        return []

    avg = []
    q = deque([root])

    while q:
        cur_lvl_len = len(q)
        lvl_total = 0

        for _ in range(cur_lvl_len):
            node = q.popleft()
            lvl_total += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        avg.append(lvl_total / cur_lvl_len)

    return avg


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        root: TreeNode | None
        want: list[float]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(
            name="three-level 1",
            root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
            want=[3.0, 14.5, 11.0],
        ),
        TestCase(
            name="three-level 2",
            root=TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20)),
            want=[3.0, 14.5, 11.0],
        ),
        TestCase(
            name="one-level",
            root=TreeNode(3),
            want=[3.0],
        ),
    ]
    for tc in test_cases:
        got = average_of_levels(tc.root)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
