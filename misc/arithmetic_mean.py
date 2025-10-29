"""
An Interview Question.

You are given an array nums and an integer value w representing window size.
For each consecutive w elements of nums calculate their arithmetic mean and return a new array of results.
Length of the resulting array should be equal to nums, as the window size 'shrinks' up to 1 towards its end.
It is not guaranteed that w <= len(nums).
Non-integer values should be rounded to 1 decimal digit.
"""

from dataclasses import dataclass


def convert(num: float) -> int | float:
    rounded = round(num, 1)
    return int(rounded) if rounded.is_integer() else rounded


def arithmetic_means(nums: list[int], w: int) -> list[int | float]:
    n = len(nums)
    if n == 0:
        return []

    result = []
    current_sum = sum(nums[: min(w, n)])

    for i in range(n):
        right = min(i + w, n)
        window_size = right - i
        if i > 0:
            current_sum -= nums[i - 1]
            if i + w - 1 < n:
                current_sum += nums[i + w - 1]
        result.append(convert(current_sum / window_size))

    return result


def arithmetic_means_right_to_left(nums: list[int], w: int) -> list[int | float]:
    n = len(nums)
    res, curr = [0] * n, 0
    for i in range(n - 1, -1, -1):
        curr += nums[i]
        if i + w < n:
            curr -= nums[i + w]
        res[i] = convert(curr / min(w, n - i))
    return res


@dataclass
class TestCase:
    name: str
    nums: list[int]
    w: int
    expected: list[int | float]


if __name__ == "__main__":
    test_cases = [
        TestCase(name="empty nums", nums=[], w=3, expected=[]),
        TestCase(name="basic", nums=[5, 7, 3, 5, 4, 3], w=3, expected=[5, 5, 4, 4, 3.5, 3]),
        TestCase(name="w > len(nums)", nums=[5, 7, 3, 5, 4, 3], w=7, expected=[4.5, 4.4, 3.8, 4, 3.5, 3]),
    ]
    for tc in test_cases:
        actual = arithmetic_means(tc.nums, tc.w)
        assert actual == tc.expected, f"Test case '{tc.name}': {tc.expected=}, {actual=}"
        actual = arithmetic_means_right_to_left(tc.nums, tc.w)
        assert actual == tc.expected, f"Test case '{tc.name}': {tc.expected=}, {actual=}"
