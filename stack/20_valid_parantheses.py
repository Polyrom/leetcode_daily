"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

from dataclasses import dataclass

BRACKETS = {
    "}": "{",
    "]": "[",
    ")": "(",
}


# O(n) memory and space
def is_valid(s: str) -> bool:
    stack = []
    for bracket in s:
        if bracket in BRACKETS:
            if not stack or stack.pop() != BRACKETS[bracket]:
                return False
        else:
            stack.append(bracket)
    return len(stack) == 0


@dataclass
class TestCase:
    s: str
    expected: bool
    name: str
    assertion_err_msg: str = "name='{name}', s={s}, want={want}, got={got}"


if __name__ == "__main__":
    test_cases = [
        TestCase("()", True, "basic valid"),
        TestCase("()[]{}", True, "invalid consequtive"),
        TestCase("([])", True, "valid nested"),
        TestCase("([)]", False, "invalid"),
        TestCase("((", False, "opening only"),
        TestCase("]", False, "closing only"),
    ]
    for tc in test_cases:
        result = is_valid(tc.s)
        assert result == tc.expected, tc.assertion_err_msg.format(name=tc.name, s=tc.s, want=tc.expected, got=result)
