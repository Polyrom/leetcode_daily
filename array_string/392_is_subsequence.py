from dataclasses import dataclass


def is_subsequence(s: str, t: str) -> bool:
    n, m = len(s), len(t)
    if n > m:
        return False

    i, j = 0, 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == n



if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        s: str
        t: str
        want: bool

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="basic true", s="abc", t="ahbgdc", want=True),
        TestCase(name="basic false", s="axc", t="ahbgdc", want=False),
    ]
    for tc in test_cases:
        got = is_subsequence(tc.s, tc.t)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
