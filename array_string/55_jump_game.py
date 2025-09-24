"""
https://leetcode.com/problems/jump-game
55. Jump Game
You are given an integer array nums. You are initially positioned at the array's first index, and each element
in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

from dataclasses import dataclass


# "Car and gas approach", kudos to:
# https://leetcode.com/problems/jump-game/solutions/4534808/super-simple-intuitive-8-line-python-solution-beats-99-92-of-users/?envType=study-plan-v2&envId=top-interview-150
# O(n) time, O(1) space
def can_jump(nums: list[int]) -> bool:
    gas = 0
    for n in nums:
        if gas < 0:
            return False
        if n > gas:
            gas = n
        gas -= 1
    return True


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        nums: list[int]
        want: bool

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="one element", nums=[1], want=True),
        TestCase(name="reachable", nums=[2, 3, 1, 1, 4], want=True),
        TestCase(name="unreachable", nums=[3, 2, 1, 0, 4], want=False),
    ]
    for tc in test_cases:
        got = can_jump(tc.nums)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
