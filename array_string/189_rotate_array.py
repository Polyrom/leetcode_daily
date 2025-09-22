"""
https://leetcode.com/problems/rotate-array
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

from dataclasses import dataclass


def reverse(nums: list[int], i: int, j: int) -> None:
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k = k % n
    if k == 0:
        return
    if k < 0:
        k += n
    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        k: int
        want: list[int]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="rotate by 3", nums=[1, 2, 3, 4, 5, 6, 7], k=3, want=[5, 6, 7, 1, 2, 3, 4]),
        TestCase(name="rotate by 2", nums=[-1, -100, 3, 99], k=2, want=[3, 99, -1, -100]),
        TestCase(name="rotate by 0", nums=[1, 2, 3, 4, 5, 6, 7], k=0, want=[1, 2, 3, 4, 5, 6, 7]),
    ]
    for tc in test_cases:
        original_arr = tc.nums
        rotate(original_arr, tc.k)
        assert original_arr == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=original_arr)
