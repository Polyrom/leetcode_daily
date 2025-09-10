"""
27. Remove Element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
  The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""

from dataclasses import dataclass


def remove_element(nums: list[int], val: int) -> int:
    non_target_idx = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[non_target_idx] = nums[i]
            non_target_idx += 1
    return non_target_idx


@dataclass
class TestCase:
    arr: list[int]
    val: int
    expected: int
    assert_err_msg: str = "got={got}, want={want}"


if __name__ == "__main__":
    test_cases = [
        TestCase(arr=[3, 2, 2, 3], val=3, expected=2),
        TestCase(arr=[0, 1, 2, 2, 3, 0, 4, 2], val=2, expected=5),
    ]
    for tc in test_cases:
        actual = remove_element(tc.arr, tc.val)
        assert actual == tc.expected, tc.assert_err_msg.format(got=actual, want=tc.expected)
        assert all(x != tc.val for x in tc.arr[: tc.expected])
