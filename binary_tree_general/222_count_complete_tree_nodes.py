"""
leetcode.com/problems/count-complete-tree-nodes

Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible.

It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Constraints:

* The number of nodes in the tree is in the range [0, 5 * 104].
* 0 <= Node.val <= 5 * 104
* THE TREE IS GUARANTEED TO BE COMPLETE.
"""

from dataclasses import dataclass


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


# O(log n) time, O(1) space
def count_nodes(root: TreeNode | None) -> int:
    def get_height(node: TreeNode | None, go_left: bool) -> int:
        height = 0
        while node:
            height += 1
            node = node.left if go_left else node.right
        return height

    if not root:
        return 0

    left_height = get_height(root, go_left=True)
    right_height = get_height(root, go_left=False)

    # if heights are equal, then the tree is perfect, and its number of nodes is 2**h - 1
    if left_height == right_height:
        return 2**left_height - 1

    # otherwise, we have to count the nodes recursively
    return 1 + count_nodes(root.right) + count_nodes(root.left)


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        root: TreeNode | None
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(
            name="empty",
            root=None,
            want=0,
        ),
        TestCase(
            name="one node",
            root=TreeNode(1),
            want=1,
        ),
        TestCase(
            name="two nodes",
            root=TreeNode(1, TreeNode(2)),
            want=2,
        ),
        TestCase(
            name="six nodes",
            root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6))),
            want=6,
        ),
    ]
    for tc in test_cases:
        got = count_nodes(tc.root)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
