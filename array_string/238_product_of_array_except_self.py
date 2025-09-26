"""
https://leetcode.com/problems/product-of-array-except-self/
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from dataclasses import dataclass


# https://youtu.be/bNvIQI2wAjk
# O(n) time, O(1) space
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    products = [1] * n
    prefix, postfix = 1, 1

    for i in range(n):
        products[i] = prefix
        prefix *= nums[i]
    for i in range(n - 1, -1, -1):
        products[i] *= postfix
        postfix *= nums[i]

    return products


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        want: list[int]

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic positive", nums=[1, 2, 3, 4], want=[24, 12, 8, 6]),
        TestCase(name="basic negative", nums=[-1, 1, 0, -3, 3], want=[0, 0, 9, 0, 0]),
    ]
    for tc in test_cases:
        got = product_except_self(tc.nums)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
