"""
380. Insert Delete GetRandom O(1)
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present,
false otherwise.

- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present,
false otherwise.

- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element
exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

from random import randint


class RandomizedSet:
    def __init__(self):
        self._index_map = {}
        self._nums = []

    def insert(self, val: int) -> bool:
        if val in self._index_map:
            return False
        self._index_map[val] = len(self._nums)
        self._nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._index_map:
            return False
        idx = self._index_map[val]
        if idx < len(self._nums) - 1:  # not the last element
            last_elem = self._nums[len(self._nums) - 1]
            self._nums[idx] = last_elem
            self._index_map[last_elem] = idx
        self._index_map.pop(val)
        self._nums.pop()
        return True

    def getRandom(self) -> int:
        return self._nums[randint(0, len(self._nums) - 1)]


if __name__ == "__main__":
    rs = RandomizedSet()
    op = rs.insert(1)
    assert op is True
    op = rs.remove(2)
    assert op is False
    op = rs.insert(2)
    assert op is True
    rand1 = rs.getRandom()
    assert rand1 in (1, 2)
    op = rs.remove(rand1)
    assert op is True
    remaining = 2 if rand1 == 1 else 1
    op = rs.insert(remaining)
    assert op is False
    assert rs.getRandom() == remaining
