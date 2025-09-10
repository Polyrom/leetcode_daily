"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from dataclasses import dataclass


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

# O(1) memory implementation
def has_cycle(head: ListNode | None) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


@dataclass
class TestCase:
    head: ListNode | None
    expected: bool


def build_linked_list(values: list[int] | None, pos: int | None) -> ListNode | None:
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos is not None:
        nodes[-1].next = nodes[pos]

    return nodes[0]


if __name__ == "__main__":
    test_cases = [
        # Empty list
        TestCase(build_linked_list([], None), False),
        # Single node, no cycle
        TestCase(build_linked_list([1], None), False),
        # Single node, self-cycle
        TestCase(build_linked_list([1], 0), True),
        # Two nodes, no cycle
        TestCase(build_linked_list([1, 2], None), False),
        # Two nodes, cycle to first
        TestCase(build_linked_list([1, 2], 0), True),
        # Two nodes, cycle to second
        TestCase(build_linked_list([1, 2], 1), True),
        # Multiple nodes, no cycle
        TestCase(build_linked_list([3, 2, 0, -4], None), False),
        # Multiple nodes, cycle in the middle
        TestCase(build_linked_list([3, 2, 0, -4], 1), True),
        # Cycle including all nodes
        TestCase(build_linked_list([1, 2, 3, 4], 0), True),
        # Longer list, cycle near end
        TestCase(build_linked_list([1, 2, 3, 4, 5, 6], 4), True),
        # Longer list, cycle at last node to itself
        TestCase(build_linked_list([1, 2, 3, 4, 5, 6], 5), True),
        # List with negative values, no cycle
        TestCase(build_linked_list([-1, -2, -3, -4], None), False),
        # List with duplicate values, cycle in the middle
        TestCase(build_linked_list([1, 2, 2, 1], 2), True),
        # Large list, no cycle
        TestCase(build_linked_list(list(range(1000)), None), False),
        # Large list, cycle at start
        TestCase(build_linked_list(list(range(1000)), 0), True),
        # Large list, cycle at middle
        TestCase(build_linked_list(list(range(1000)), 500), True),
    ]
    for i, tc in enumerate(test_cases, 1):
        assert has_cycle(tc.head) == tc.expected, f"test case #{i} failed"
