"""
LeetCode #118 - Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]

Constraints:
    1 <= numRows <= 30
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for _ in range(1, numRows):
            prev = triangle[-1]
            row = [1]
            for i in range(1, len(prev)):
                row.append(prev[i - 1] + prev[i])
            row.append(1)
            triangle.append(row)

        return triangle
