"""
LeetCode #22 - Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]

Constraints:
    1 <= n <= 8
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs(n, 0, 0, "", result)
        return result

    def dfs(
        self,
        n: int,
        open_count: int,
        close_count: int,
        path: str,
        result: List[str],
    ) -> None:
        if len(path) == 2 * n:
            result.append(path)
            return

        if open_count < n:
            self.dfs(n, open_count + 1, close_count, path + "(", result)

        if close_count < open_count:
            self.dfs(n, open_count, close_count + 1, path + ")", result)
