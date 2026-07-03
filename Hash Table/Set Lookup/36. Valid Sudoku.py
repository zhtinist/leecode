"""
LeetCode #36 - Valid Sudoku
https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
   without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not necessarily
    solvable.
    Only the filled cells need to be validated according to the mentioned rules.

Example 1:
    Input: board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Output: true

Example 2:
    Input: board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner
    being modified to 8. Since there are two 8's in the top left 3x3 sub-box,
    it is invalid.

Example 3:
    Input: board = [
        [".","8","7","6","5","4","3","2","1"],
        ["2",".",".",".",".",".",".",".","."],
        ["3",".",".",".",".",".",".",".","."],
        ["4",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".",".","."],
        ["6",".",".",".",".",".",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        ["8",".",".",".",".",".",".",".","."],
        ["9",".",".",".",".",".",".",".","."]
    ]
    Output: false
    Explanation: Each row, column, and 3x3 sub-box must contain the digits
    1-9 without repetition. The first column contains two 8's.

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self._valid_rows(board)
            and self._valid_cols(board)
            and self._valid_boxes(board)
        )

    def _valid_rows(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        return True

    def _valid_cols(self, board: List[List[str]]) -> bool:
        for col in range(9):
            seen = set()
            for row in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        return True

    def _valid_boxes(self, board: List[List[str]]) -> bool:
        for box in range(9):
            seen = set()
            start_row = (box // 3) * 3
            start_col = (box % 3) * 3
            for i in range(3):
                for j in range(3):
                    cell = board[start_row + i][start_col + j]
                    if cell == ".":
                        continue
                    if cell in seen:
                        return False
                    seen.add(cell)
        return True
