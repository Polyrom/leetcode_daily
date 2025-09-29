"""
https://leetcode.com/problems/path-sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""

from dataclasses import dataclass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target_sum

    left_sum = has_path_sum(root.left, target_sum - root.val)
    right_sum = has_path_sum(root.right, target_sum - root.val)

    return left_sum or right_sum


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        root: TreeNode | None
        target_sum: int
        want: bool

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(
            name="basic true",
            root=TreeNode(
                5,
                TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1))),
            ),
            target_sum=22,
            want=True,
        ),
        TestCase(name="basic false", root=TreeNode(1, TreeNode(2), TreeNode(3)), target_sum=5, want=False),
    ]
    for tc in test_cases:
        got = has_path_sum(tc.root, tc.target_sum)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
