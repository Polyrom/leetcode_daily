"""
https://leetcode.com/problems/reverse-linked-list-ii

92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.
"""

from dataclasses import dataclass

from helpers import ListNode, array_from_list, list_from_array


# Time: O(n). Space: O(1)
def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    if not head or left == right:
        return head
    
    dummy = ListNode(-1, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    
    curr = prev.next
    for _ in range(right - left):
        tmp = curr.next
        curr.next = tmp.next
        tmp.next = prev.next
        prev.next = tmp

    return dummy.next


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        head: list[int]
        left: int
        right: int
        want: list[int]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic", head=[1, 2, 3, 4, 5], left=2, right=4, want=[1, 4, 3, 2, 5]),
        TestCase(name="basic2", head=[1, 2, 3, 4, 5, 6, 7, 8], left=3, right=8, want=[1, 2, 8, 7, 6, 5, 4, 3]),
        TestCase(name="single element", head=[5], left=1, right=1, want=[5]),
    ]
    for tc in test_cases:
        got_list = reverse_between(list_from_array(tc.head), tc.left, tc.right)
        got = array_from_list(got_list)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
