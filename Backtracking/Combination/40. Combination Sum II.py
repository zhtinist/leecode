"""
LeetCode #40 - Combination Sum II
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to
target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
    Input: candidates = [2,5,2,1,2], target = 5
    Output: [[1,2,2],[5]]

Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        used = [False] * len(candidates)
        self.dfs(candidates, target, 0, [], used, result)
        return result

    def dfs(
        self,
        candidates: List[int],
        remain: int,
        start: int,
        path: List[int],
        used: List[bool],
        result: List[List[int]],
    ) -> None:
        if remain == 0:
            result.append(path[:])
            return
        if remain < 0:
            return

        for i in range(start, len(candidates)):
            if used[i]:
                continue
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            used[i] = True
            path.append(candidates[i])
            self.dfs(candidates, remain - candidates[i], i + 1, path, used, result)
            path.pop()
            used[i] = False
