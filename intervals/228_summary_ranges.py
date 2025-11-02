"""
228. Summary Ranges
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x
such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
"""

from dataclasses import dataclass


# O(n) time, O(1) space
def summary_ranges(nums: list[int]) -> list[str]:
    if not nums:
        return []

    ranges = []
    left = 0
    for right in range(1, len(nums) + 1):
        if right == len(nums) or nums[right] - nums[right - 1] > 1:
            if right == left + 1:
                ranges.append(str(nums[left]))
            else:
                ranges.append(f"{nums[left]}->{nums[right - 1]}")
            left = right

    return ranges


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        want: list[str]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic 1", nums=[0, 1, 2, 4, 5, 7], want=["0->2", "4->5", "7"]),
        TestCase(name="basic 2", nums=[0, 2, 3, 4, 6, 8, 9], want=["0", "2->4", "6", "8->9"]),
        TestCase(name="no intervals", nums=[0, 2, 4, 6, 8], want=["0", "2", "4", "6", "8"]),
    ]
    for tc in test_cases:
        got = summary_ranges(tc.nums)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
