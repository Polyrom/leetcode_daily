"""
530. Minimum Absolute Difference in BST
Given the root of a Binary Search Tree (BST), return the minimum absolute difference
between the values of any two different nodes in the tree.
"""

from dataclasses import dataclass


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_difference(root: TreeNode | None) -> int | float:
    prev = None
    min_diff = float("inf")

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        nonlocal prev, min_diff
        dfs(node.left)
        if prev is not None:
            min_diff = min(min_diff, node.val - prev)
        prev = node.val
        dfs(node.right)
    dfs(root)
    return min_diff
    


@dataclass
class TestCase:
    root: TreeNode | None
    expected: int
    assertion_err_msg: str = "want={want}, got={got}"


def build_bst_from_list(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    for val in vals[1:]:
        insert_bst(root, val)
    return root


def insert_bst(node, val):
    if val < node.val:
        if node.left:
            insert_bst(node.left, val)
        else:
            node.left = TreeNode(val)
    else:
        if node.right:
            insert_bst(node.right, val)
        else:
            node.right = TreeNode(val)


if __name__ == "__main__":
    test_cases = [
        TestCase(root=build_bst_from_list([1, 3]), expected=2),  # Two nodes
        TestCase(root=build_bst_from_list([4, 2, 6, 1, 3]), expected=1),  # Balanced BST
        TestCase(root=build_bst_from_list([-10, -20, -3, -15]), expected=5),  # Negative values
        TestCase(root=build_bst_from_list([2, 2, 2]), expected=0),  # Duplicate values
    ]
    for i, tc in enumerate(test_cases, 1):
        result = get_minimum_difference(tc.root)
        assert result == tc.expected, f"test case #{i}: {tc.assertion_err_msg.format(want=tc.expected, got=result)}"
