"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

80. Remove Duplicates from Sorted Array II
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

from dataclasses import dataclass



def remove_duplicates(nums: list[int]) -> int:
    i = 0
    for n in nums:
        if i < 2 or n > nums[i - 2]:
            nums[i] = n
            i += 1
    return i


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
        TestCase(name="basic no dups", nums=[1, 2, 3, 4], want=4, nums_deduped=[1, 2, 3, 4]),
        TestCase(name="basic with dups", nums=[1, 1, 1, 2, 2, 3], want=5, nums_deduped=[1, 1, 2, 2, 3]),
        TestCase(
            name="advanced with dups",
            nums=[0, 0, 1, 1, 1, 1, 2, 3, 3],
            want=7,
            nums_deduped=[0, 0, 1, 1, 2, 3, 3],
        ),
    ]
    for tc in test_cases:
        original_arr = tc.nums
        got = remove_duplicates(original_arr)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
        assert len(tc.nums_deduped) == got
        assert original_arr[:got] == tc.nums_deduped, ASSERTION_ERR_FMT.format(
            name=tc.name,
            want=tc.nums_deduped,
            got=original_arr[:got],
        )
        print(f"{tc.name}: passed")
