"""
LeetCode #119 - Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the
Pascal's triangle.

Example 1:
    Input: rowIndex = 3
    Output: [1,3,3,1]

Example 2:
    Input: rowIndex = 0
    Output: [1]

Example 3:
    Input: rowIndex = 1
    Output: [1,1]

Constraints:
    0 <= rowIndex <= 33
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for _ in range(rowIndex):
            for i in range(len(row) - 1, 0, -1):
                row[i] += row[i - 1]

        return row
