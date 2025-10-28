"""
https://leetcode.com/problems/flood-fill

733. Flood Fill
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel
value of the image. You are also given three integers sr, sc, and color.
Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel,
either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color
if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
"""

from dataclasses import dataclass
from typing import List


class Solution:
    def dfs(self, image: List[List[int]], sr: int, sc: int, old_color: int, color: int) -> None:
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != old_color:
            return

        # Update the color of the current pixel
        image[sr][sc] = color

        # Recursively call dfs for adjacent pixels
        self.dfs(image, sr - 1, sc, old_color, color)
        self.dfs(image, sr + 1, sc, old_color, color)
        self.dfs(image, sr, sc - 1, old_color, color)
        self.dfs(image, sr, sc + 1, old_color, color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        self.dfs(image, sr, sc, image[sr][sc], color)
        return image


@dataclass
class TestCase:
    name: str
    image: List[List[int]]
    sr: int
    sc: int
    color: int
    want: List[List[int]]


if __name__ == "__main__":
    test_cases = [
        TestCase(
            name="basic",
            image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]],
            sr=1,
            sc=1,
            color=2,
            want=[[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        )
    ]
    solution = Solution()
    for tc in test_cases:
        assert solution.floodFill(tc.image, tc.sr, tc.sc, tc.color) == tc.want
