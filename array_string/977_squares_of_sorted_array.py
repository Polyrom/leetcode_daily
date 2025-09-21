"""
977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""

from dataclasses import dataclass


# O(n) memory and space, not pretty, hard to reason about and needs extra space for splitted arrays
def sorted_squares(nums: list[int]) -> list[int]:
    result = []
    smallest_pos_idx = None
    for i in range(len(nums)):
        if nums[i] >= 0:
            smallest_pos_idx = i
            break
    negs = nums if smallest_pos_idx is None else nums[:smallest_pos_idx]
    pos = [] if smallest_pos_idx is None else nums[smallest_pos_idx:]
    i = 0
    j = len(negs) - 1
    while i < len(pos) and j >= 0:
        pos_sqrd, neg_sqrd = pos[i] ** 2, negs[j] ** 2
        if pos_sqrd <= neg_sqrd:
            result.append(pos_sqrd)
            i += 1
        else:
            result.append(neg_sqrd)
            j -= 1
    if i < len(pos):
        result.extend([num**2 for num in pos[i:]])
    if j >= 0:
        result.extend(reversed([num**2 for num in negs[: j + 1]]))
    return result

# O(n) memory and space as well, three pointers, nice exquisite touch and easy to reason about
def sorted_squares_nicer(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    left, right, pos = 0, n - 1, n - 1
    while left <= right:
        left_sqrd, right_sqrd = nums[left] ** 2, nums[right] ** 2
        if left_sqrd >= right_sqrd:
            result[pos] = left_sqrd
            left += 1
        else:
            result[pos] = right_sqrd
            right -= 1
        pos -= 1
    return result

@dataclass
class TestCase:
    array: list[int]
    expected: list[int]
    assertion_err_msg: str = "array={array}, want={want}, got={got}"


if __name__ == "__main__":
    test_cases = [
        TestCase([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        TestCase([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        TestCase([-10, -7, -2, -1], [1, 4, 49, 100]),
        TestCase([1, 2, 7, 10], [1, 4, 49, 100]),
    ]
    for i, tc in enumerate(test_cases, 1):
        result = sorted_squares(tc.array)
        assert result == tc.expected, (
            f"test case #{i}: {tc.assertion_err_msg.format(array=tc.array, want=tc.expected, got=result)}"
        )
        result1 = sorted_squares_nicer(tc.array)
        assert result1 == tc.expected, (
            f"test case #{i}: {tc.assertion_err_msg.format(array=tc.array, want=tc.expected, got=result1)}"
        )
