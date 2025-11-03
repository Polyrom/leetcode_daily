"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

105. Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""

from dataclasses import dataclass


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: "TreeNode") -> bool:
        if not isinstance(other, self.__class__):
            return False

        def is_nodes_equal(node1: "TreeNode | None", node2: "TreeNode | None") -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return is_nodes_equal(node1.left, node2.left) and is_nodes_equal(node1.right, node2.right)

        return is_nodes_equal(self, other)

    def __str__(self) -> str:
        return f"TreeNode({self.val}, left={self.left}, right={self.right})"


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    inorder_map = {val: i for i, val in enumerate(inorder)}
    idx = 0

    def helper(start: int, end: int) -> TreeNode | None:
        nonlocal idx
        if start > end:
            return None
        root_val = preorder[idx]
        idx += 1
        root = TreeNode(root_val)
        mid = inorder_map[root_val]
        root.left = helper(start, mid - 1)
        root.right = helper(mid + 1, end)
        return root

    return helper(0, len(inorder) - 1)


@dataclass
class TestCase:
    name: str
    preorder: list[int]
    inorder: list[int]
    expected: TreeNode | None
    assertion_err_msg: str = "test case '{name}' want={want}, got={got}"


if __name__ == "__main__":
    test_cases = [
        TestCase(
            name="basic",
            preorder=[3, 9, 20, 15, 7],
            inorder=[9, 3, 15, 20, 7],
            expected=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
        ),
        TestCase(
            name="-1",
            preorder=[-1],
            inorder=[-1],
            expected=TreeNode(-1),
        ),
    ]
    for i, tc in enumerate(test_cases, 1):
        result = build_tree(tc.preorder, tc.inorder)
        assert result == tc.expected, tc.assertion_err_msg.format(name=tc.name, want=tc.expected, got=result)
