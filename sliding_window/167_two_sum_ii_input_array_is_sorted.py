"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""

from dataclasses import dataclass

# Two-pointer approach, O(n) time O(1) space
def two_sum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while numbers[left] + numbers[right] != target:
        if numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
    return [left + 1, right + 1]


# Binary-search-based approach: for each index i, binary search for target - numbers[i]
# Time: O(n log n), Space: O(1)
def two_sum_binary_search(numbers: list[int], target: int) -> list[int]:
    n = len(numbers)
    for i in range(n - 1):
        complement = target - numbers[i]
        lo, hi = i + 1, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]
            if numbers[mid] < complement:
                lo = mid + 1
            else:
                hi = mid - 1
    return [0, 0]


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        numbers: list[int]
        target: int
        want: list[int]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="target_9", numbers=[1, 2, 7, 11, 15], target=9, want=[2, 3]),
        TestCase(name="target_6", numbers=[1, 2, 3, 4], target=6, want=[2, 4]),
        TestCase(name="target_1_negatives", numbers=[-1, 0], target=-1, want=[1, 2]),
    ]
    for tc in test_cases:
        got = two_sum(tc.numbers, tc.target)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)

        got_bs = two_sum_binary_search(tc.numbers, tc.target)
        assert got_bs == tc.want, ASSERTION_ERR_FMT.format(name=tc.name + " (bs)", want=tc.want, got=got_bs)
