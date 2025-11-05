"""
A Google interview problem, they say.

Given an array arr. Return True if it is an almost sorted array, and False if it's not.
arr is almost sorted if there is an element arr[i] such that the rest of the array are sorted.
i.e. arr[0] <= arr[1] <= ... <= arr[i-2] <= arr[i-1] <= arr[i+1] <= arr[i+2] <= ... <= arr[n-2] <= arr[n-1]
"""

from dataclasses import dataclass


def is_almost_sorted(nums: list[int]) -> bool:
    n = len(nums)
    if n <= 1:
        return True

    count = 0
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            count += 1
            if count > 1:
                return False
            if i > 0 and nums[i - 1] > nums[i + 1] and i + 2 < n and nums[i] > nums[i + 2]:
                return False
    return True


@dataclass
class TestCase:
    name: str
    nums: list[int]
    expected: bool


if __name__ == "__main__":
    test_cases = [
        TestCase(name="1", nums=[1, 2, 3, 6, 9], expected=True),
        TestCase(name="2", nums=[1, 4, 3, 7, 9], expected=True),
        TestCase(name="3", nums=[1, 3, 2, 6], expected=True),
        TestCase(name="4", nums=[1, 3, 4, 1], expected=True),
        TestCase(name="5", nums=[1, -8, 3, 4, 1, 8, 9, 11], expected=False),
        TestCase(name="6", nums=[1, 0, -1, -2, -3], expected=False),
        TestCase(name="7", nums=[], expected=True),
        TestCase(name="8", nums=[1], expected=True),
    ]
    for tc in test_cases:
        got = is_almost_sorted(tc.nums)
        assert got == tc.expected, f"test case '{tc.name}': {got=}, {tc.expected=}'"
