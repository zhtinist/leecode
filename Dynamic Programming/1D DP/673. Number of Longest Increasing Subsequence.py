"""
LeetCode #673 - Number of Longest Increasing Subsequence
中文题名：最长递增子序列的个数
https://leetcode.com/problems/number-of-longest-increasing-subsequence/

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:

Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Note:
Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in
32-bit signed int.

【中文翻译】
给定一个未排序的整数数组，找出最长递增子序列的个数。

示例 1：

输入：[1,3,5,4,7]
输出：2
解释：两个最长递增子序列是 [1, 3, 4, 7] 和 [1, 3, 5, 7]。

示例 2：

输入：[2,2,2,2,2]
输出：5
解释：最长递增子序列的长度是 1，并且有 5 个长度为 1 的子序列，所以输出 5。

注意：
给定数组的长度不超过 2000，且结果保证在 32 位有符号整数范围内。
"""

from typing import List, Optional


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        lengths = [1] * n
        counts = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_len = max(lengths)
        return sum(c for l, c in zip(lengths, counts) if l == max_len)











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划，同时维护两个数组：
# - lengths[i]：以 nums[i] 结尾的最长递增子序列的长度
# - counts[i]：以 nums[i] 结尾的最长递增子序列的个数
#
# 对于每个位置 i，遍历之前的所有位置 j：
# 如果 nums[j] < nums[i]（可以接到后面）：
#   1. 如果 lengths[j] + 1 > lengths[i]：
#      发现更长的子序列，更新 lengths[i]，counts[i] 重置为 counts[j]
#   2. 如果 lengths[j] + 1 == lengths[i]：
#      发现相同长度的不同子序列，counts[i] 累加 counts[j]
#
# 最后，找到全局最优长度 max_len，
# 将所有 lengths[i] == max_len 的 counts[i] 求和即得答案。
#
# 时间复杂度: O(n^2) - 双重循环
# 空间复杂度: O(n) - lengths 和 counts 数组
#
# 关键点:
# - 这是 #300（最长递增子序列）的进阶版：不仅求长度，还求个数
# - 两条 DP 规则覆盖了"更长"和"等长不同路径"两种情况
# - 初始化：lengths[i] = 1, counts[i] = 1（每个元素本身是一个子序列）
# - 注意不是简单求和所有 counts，而是只统计达到 max_len 的那些
