"""
https://leetcode.com/problems/add-two-numbers

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from dataclasses import dataclass

from helpers import ListNode, array_from_list, list_from_array

# Time: O(n). Space: O(1)
def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = ListNode(val=-1)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        l1: list[int]
        l2: list[int]
        want: list[int]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic", l1=[2, 4, 3], l2=[5, 6, 4], want=[7, 0, 8]),
        TestCase(name="zeroes", l1=[0], l2=[0], want=[0]),
        TestCase(
            name="variable length nines",
            l1=[9, 9, 9, 9, 9, 9, 9],
            l2=[9, 9, 9, 9],
            want=[8, 9, 9, 9, 0, 0, 0, 1],
        ),
    ]
    for tc in test_cases:
        got_list = add_two_numbers(list_from_array(tc.l1), list_from_array(tc.l2))
        got = array_from_list(got_list)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
