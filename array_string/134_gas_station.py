"""
https://leetcode.com/problems/gas-station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
"""

from dataclasses import dataclass


# O(n) time and O(1) space
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    n = len(cost)
    surplus = 0
    tank = 0
    start = 0

    for i in range(n):
        surplus += gas[i] - cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:
            tank = 0
            start = i + 1

    return -1 if surplus < 0 else start


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        gas: list[int]
        cost: list[int]
        want: int

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="doable", gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2], want=3),
        TestCase(name="undoable", gas=[2, 3, 4], cost=[3, 4, 3], want=-1),
    ]
    for tc in test_cases:
        got = can_complete_circuit(tc.gas, tc.cost)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
