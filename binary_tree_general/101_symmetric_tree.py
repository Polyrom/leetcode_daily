"""
https://leetcode.com/problems/symmetric-tree

101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

from dataclasses import dataclass


class TreeNode:
    def __init__(self, val: int, left: "TreeNode", right: "TreeNode") -> None:
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode | None) -> bool:
    def is_mirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and is_mirror(t1.right, t2.left) and is_mirror(t1.left, t2.right)

    return is_mirror(root, root)


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        tree: TreeNode | None
        want: bool
        assertion_err_msg_fmt: str = "test case '{name}': want={want}, got={got}"

    def build_tree(lst: list[int] | None) -> TreeNode | None:
        if lst is None:
            return None
        val, left, right = lst
        return TreeNode(val, build_tree(left), build_tree(right))

    test_cases = [
        TestCase(name="empty tree", tree=build_tree(None), want=True),
        TestCase(
            name="symmetric tree",
            tree=build_tree([1, [2, [3, None, None], [4, None, None]], [2, [4, None, None], [3, None, None]]]),
            want=True,
        ),
        TestCase(
            name="asymmetric tree",
            tree=build_tree([1, [2, [3, None, None], [4, None, None]], [2, [3, None, None], [3, None, None]]]),
            want=False,
        ),
    ]
    for tc in test_cases:
        got = is_symmetric(tc.tree)
        assert got == tc.want, tc.assertion_err_msg_fmt.format(name=tc.name, want=tc.want, got=got)
