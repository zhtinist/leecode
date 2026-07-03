"""
LeetCode #47 - Permutations II
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all
the possible unique permutations in any order.

Example 1:
    Input: nums = [1,1,2]
    Output: [[1,1,2],[1,2,1],[2,1,1]]

Example 2:
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []
        path: List[int] = []
        used = [False] * len(nums)

        def dfs() -> None:
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i, num in enumerate(nums):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(num)
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return result
