"""
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

from dataclasses import dataclass


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode(-1)
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return dummy.next


if __name__ == "__main__":

    def is_lists_equal(l1: ListNode | None, l2: ListNode | None) -> bool:
        while l1 and l2:
            if l1.val == l2.val:
                l1 = l1.next
                l2 = l2.next
            else:
                return False
        return l1 is None and l2 is None

    @dataclass
    class TestCase:
        name: str
        list1: ListNode | None
        list2: ListNode | None
        want: ListNode | None

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(
            name="empty",
            list1=None,
            list2=None,
            want=None,
        ),
        TestCase(
            name="same length",
            list1=ListNode(1, ListNode(2, ListNode(4))),
            list2=ListNode(1, ListNode(3, ListNode(4))),
            want=ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))),
        ),
        TestCase(
            name="different length",
            list1=ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            list2=ListNode(1, ListNode(3, ListNode(4))),
            want=ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4))))))),
        ),
    ]
    for tc in test_cases:
        got = merge_two_lists(tc.list1, tc.list2)
        assert is_lists_equal(got, tc.want), ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
