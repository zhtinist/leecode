"""
LeetCode #90 - Subsets II
https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible
subsets (the power set).

Example 1:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path: List[int] = []

        def dfs(start: int) -> None:
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result
