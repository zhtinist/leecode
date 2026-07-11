"""
LeetCode #368 - Largest Divisible Subset
中文题名：最大整除子集
https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers, find the largest subset such that every
pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

【中文翻译】
给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si, Sj) 都要满足：
Si % Sj = 0 或 Sj % Si = 0。

如果有多个目标子集，返回其中任何一个均可。

示例 1：

输入：[1,2,3]
输出：[1,2]（当然，[1,3] 也正确）

示例 2：

输入：[1,2,4,8]
输出：[1,2,4,8]
"""

from typing import List, Optional


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        # dp[i] = 以 nums[i] 结尾的最大整除子集的大小
        dp = [1] * n
        # prev[i] = 子集中 nums[i] 前一个元素的下标，用于重建子集
        prev = [-1] * n
        # 最大子集结尾元素的下标
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i

        # 重建最大整除子集
        res = []
        idx = max_idx
        while idx != -1:
            res.append(nums[idx])
            idx = prev[idx]
        return res[::-1]  # 反转为从小到大的顺序










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 首先将数组排序，排序后整除关系具有传递性：若 a < b < c 且 b % a == 0, c % b == 0，则 c % a == 0。
# 因此问题转化为类似 LIS（最长递增子序列）的 DP 问题。
# 定义 dp[i] 为以 nums[i] 结尾的最大整除子集的长度。
# 状态转移：对于 j < i，若 nums[i] % nums[j] == 0，则 dp[i] = max(dp[i], dp[j] + 1)。
# 同时用 prev[i] 记录前驱下标，方便回溯重建具体子集。
# 遍历结束后，从 dp 最大值对应的下标出发，沿 prev 数组回溯，收集所有元素。
# 最后反转得到从小到大排序的结果。
#
# 时间复杂度: O(n^2) - 两层循环遍历所有数对
# 空间复杂度: O(n) - dp 和 prev 数组各 O(n)
#
# 关键点:
# - 先排序是利用整除传递性的关键步骤
# - 排序后问题退化为 LIS 变种，只需检查两两整除关系
# - prev 数组用于回溯重建子集（类似 LIS 的路径记录）
# - 结果需反转以保持从小到大的顺序
