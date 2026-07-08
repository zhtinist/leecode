"""
LeetCode #77 - Combinations
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers chosen
from the range [1, n].

Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
    Input: n = 1, k = 1
    Output: [[1]]

Constraints:
    1 <= n <= 20
    1 <= k <= n
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path: List[int] = []

        def dfs(start: int) -> None:
            if len(path) == k:
                result.append(path[:])
                return

            need = k - len(path)
            for num in range(start, n - need + 2):
                path.append(num)
                dfs(num + 1)
                path.pop()

        dfs(1)
        return result
