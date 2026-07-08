"""
LeetCode #79 - Word Search
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

Example 1:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

Example 2:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    Output: true

Example 3:
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    Output: false

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, index: int) -> bool:
            if index == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"
            found = (
                dfs(i + 1, j, index + 1)
                or dfs(i - 1, j, index + 1)
                or dfs(i, j + 1, index + 1)
                or dfs(i, j - 1, index + 1)
            )
            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
