"""
https://leetcode.com/problems/simplify-path

71. Simplify Path

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name.
For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.
"""

from dataclasses import dataclass

SLASH = "/"
CURRENT_DIR = "."
PARENT_DIR = ".."


# Time: O(2n). Space: O(2n). Can be optimized though 
def simplify_path(path: str) -> str:
    path_stack = [p for p in path.split(SLASH) if p and p != SLASH]
    canonical = []
    for path_item in path_stack:
        if path_item not in (CURRENT_DIR, PARENT_DIR):
            canonical.append(path_item)
        elif path_item == PARENT_DIR and canonical:
            canonical.pop()
    return SLASH + SLASH.join(canonical)


if __name__ == "__main__":

    @dataclass
    class TestCase:
        name: str
        path: str
        want: str

    ASSERTION_ERR_FMT = "test case '{name}': want={want}, got={got}"

    test_cases = [
        TestCase(name="trailing slash", path="/home/", want="/home"),
        TestCase(name="consecutive slashes", path="/home//foo/", want="/home/foo"),
        TestCase(name="parent dir", path="/home/user/Documents/../Pictures", want="/home/user/Pictures"),
        TestCase(name="multiple parent dirs", path="/a/./b/../../c/", want="/c"),
        TestCase(name="higher than root", path="/../", want="/"),
        TestCase(name="three dots as dirname", path="/.../a/../b/c/../d/./", want="/.../b/d"),
    ]
    for tc in test_cases:
        got = simplify_path(tc.path)
        assert got == tc.want, ASSERTION_ERR_FMT.format(name=tc.name, want=tc.want, got=got)
