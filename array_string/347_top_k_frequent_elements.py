"""
https://leetcode.com/problems/top-k-frequent-elements/

347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
Constraints:

* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
* k is in the range [1, the number of unique elements in the array].
* It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import Counter
from dataclasses import dataclass


# Bucket sort approach. O(n) time and space.
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    result = [0] * k
    num_count = Counter(nums)
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in num_count.items():
        buckets[freq].append(num)
    result: list[int] = []
    for freq in range(len(buckets) - 1, -1, -1):
        if buckets[freq]:
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
    return result


@dataclass
class TestCase:
    name: str
    nums: list[int]
    k: int
    expected: list[int]


if __name__ == "__main__":
    test_cases = [
        TestCase(name="1", nums=[1], k=1, expected=[1]),
        TestCase(name="2", nums=[1, 1, 1, 2, 2, 3], k=2, expected=[1, 2]),
        TestCase(name="3", nums=[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2, expected=[1, 2]),
    ]
    for tc in test_cases:
        actual = top_k_frequent(tc.nums, tc.k)
        assert actual == tc.expected, f"Test case {tc.name}: expected={tc.expected}, {actual=}"
