class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):  # noqa: A002
        self.val = val
        self.next = next


def list_from_array(arr: list[int]) -> ListNode | None:
    if not arr:
        return None
    head = ListNode(val=arr[0])
    current = head
    for n in arr[1:]:
        current.next = ListNode(val=n)
        current = current.next
    return head


def array_from_list(list_: ListNode | None) -> list[int]:
    arr = []
    while list_:
        arr.append(list_.val)
        list_ = list_.next
    return arr
