"""
https://leetcode.com/problems/jump-game-ii
45. Jump Game II

Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at index i, you can jump to any index (i + j) where:
0 <= j <= nums[i] and i + j < n

Return the minimum number of jumps to reach index n - 1.
The test cases are generated such that you can reach index n - 1.
"""

from dataclasses import dataclass


# greedy (BFS in array) approach
# O(n) time, 0(1) space
def jump(nums: list[int]) -> int:
    n = len(nums)
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
            if cur_end >= n - 1:
                return jumps

    return jumps


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="one element", nums=[1], want=0),
        TestCase(name="basic 2-step reach 1", nums=[2, 3, 1, 1, 4], want=2),
        TestCase(name="basic 2-step reach 2", nums=[2, 3, 1, 0, 4], want=2),
    ]
    for tc in test_cases:
        got = jump(tc.nums)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
