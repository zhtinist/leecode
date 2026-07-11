"""
LeetCode #491 - Non-decreasing Subsequences
中文题名：非递减子序列
https://leetcode.com/problems/non-decreasing-subsequences/

Given an integer array, your task is to find all the different possible increasing
subsequences of the given array, and the length of an increasing subsequence should be at
least 2.

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Note:

The length of the given array will not exceed 15.

The range of integer in the given array is [-100,100].

The given array may contain duplicates, and two equal integers should also be considered
as a special case of increasing sequence.

【中文翻译】
给定一个整数数组，找出所有不同的递增子序列，递增子序列的长度至少为 2。

示例：
    输入：[4, 6, 7, 7]
    输出：[[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

注意：
    给定数组的长度不超过 15。
    数组中整数的范围为 [-100, 100]。
    数组可能包含重复数字，相等的两个数字也应视为递增的一种特殊情况。
"""

from typing import List, Optional


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        n = len(nums)

        def backtrack(start: int, path: List[int]) -> None:
            if len(path) >= 2:
                result.append(path[:])

            used = set()  # 同层去重
            for i in range(start, n):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用回溯（DFS）枚举所有子序列。需注意两处去重：
# 1. 同层去重：在当前递归层用 set 记录已使用过的值，跳过重复数字避免产生重复子序列
# 2. 序列顺序去重：通过 start 参数保证按索引递增顺序选择，避免生成同一子集的不同排列
# 对于每个位置，若 path 为空或当前数字 >= path 最后一个数字（满足非递减），则加入并递归。
# 当 path 长度 >= 2 时，将其加入结果。
#
# 时间复杂度: O(2^N * N) — 最坏情况每个元素选或不选，共有 2^N 种子序列，每次复制 O(N)
# 空间复杂度: O(N) — 递归栈深度和 path 长度最多为 N（N <= 15）
#
# 关键点:
# - 同层去重使用 set，避免生成重复子序列（如 [4,6,7] 和 [4,6,7] 来自两个不同的 7）
# - start 参数保证索引递增，避免排列重复
# - N <= 15 使得 O(2^N) 的回溯方法可行
# - 相等元素（7,7）也被视为非递减，所以条件是 nums[i] >= path[-1]
