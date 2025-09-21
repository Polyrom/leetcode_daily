"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
 appears only once. The relative order of the elements should be kept the same.
 Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present
in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

from dataclasses import dataclass


def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        want: int
        nums_deduped: list[int]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="empty array", nums=[], want=0, nums_deduped=[]),
        TestCase(name="one-element array", nums=[1], want=1, nums_deduped=[1]),
        TestCase(name="basic with dups", nums=[1, 2, 2, 2, 3, 4], want=4, nums_deduped=[1, 2, 3, 4]),
        TestCase(name="basic no dups", nums=[1, 2, 3, 4], want=4, nums_deduped=[1, 2, 3, 4]),
    ]
    for tc in test_cases:
        original_arr = tc.nums
        got = remove_duplicates(original_arr)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
        assert len(tc.nums_deduped) == got
        assert original_arr[:got] == tc.nums_deduped
        print(f"{tc.name}: passed")
