"""
LeetCode #168 - Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/

Given an integer columnNumber, return its corresponding column title as it
appears in an Excel sheet.

Example 1:
    Input: columnNumber = 1
    Output: "A"

Example 2:
    Input: columnNumber = 28
    Output: "AB"

Example 3:
    Input: columnNumber = 701
    Output: "ZY"

Constraints:
    1 <= columnNumber <= 2^31 - 1
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber:
            columnNumber -= 1
            result.append(chr(ord("A") + columnNumber % 26))
            columnNumber //= 26

        return "".join(reversed(result))
