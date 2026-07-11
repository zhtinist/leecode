"""
LeetCode #1027 - Longest Arithmetic Subsequence
中文题名：最长等差数列
https://leetcode.com/problems/longest-arithmetic-subsequence/

Given an array `A` of integers, return the length of the longest
arithmetic subsequence in `A`.

Recall that a subsequence of `A` is a list `A[i_1], A[i_2], ...,
A[i_k]` with `0 <= i_1 < i_2 < ... < i_k <= A.length - 1`,
and that a sequence `B` is arithmetic if `B[i+1] - B[i]`
are all the same value (for `0 <= i < B.length - 1`).

Example 1:

Input: [3,6,9,12]
Output: 4
Explanation:
The whole array is an arithmetic sequence with steps of length = 3.

Example 2:

Input: [9,4,7,2,10]
Output: 3
Explanation:
The longest arithmetic subsequence is [4,7,10].

Example 3:

Input: [20,1,15,3,10,5,8]
Output: 4
Explanation:
The longest arithmetic subsequence is [20,15,10,5].

【中文翻译】
给定一个整数数组 A，返回 A 中最长等差子序列的长度。

回想一下，A 的子序列是一个列表 A[i_1], A[i_2], ..., A[i_k]，其中 0 <= i_1 < i_2 < ... < i_k <= A.length - 1，并且如果序列 B 是等差的，则 B[i+1] - B[i] 对于 0 <= i < B.length - 1 都是相同的值。

示例 1：

输入：[3,6,9,12]
输出：4
解释：
整个数组是一个公差为 3 的等差数列。

示例 2：

输入：[9,4,7,2,10]
输出：3
解释：
最长的等差子序列是 [4,7,10]。

示例 3：

输入：[20,1,15,3,10,5,8]
输出：4
解释：
最长的等差子序列是 [20,15,10,5]。
"""

from typing import List, Optional


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # dp[i][diff] = length of longest arithmetic subsequence ending at i with difference diff
        dp = [{} for _ in range(n)]
        max_len = 2

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                max_len = max(max_len, dp[i][diff])

        return max_len










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划。定义 dp[i] 为一个字典，其中 dp[i][diff] 表示以索引 i 结尾、公差为 diff
# 的最长等差子序列的长度。对于每个 i，遍历所有 j < i，计算 diff = nums[i] - nums[j]。
# 如果 dp[j] 中存在 diff，则 dp[i][diff] = dp[j][diff] + 1；否则 dp[i][diff] = 2（只有 nums[j] 和 nums[i] 两个元素）。
# 全局最大长度在遍历过程中更新。
#
# 时间复杂度: O(N^2) - 双重循环遍历所有 (i, j) 对
# 空间复杂度: O(N^2) - 最坏情况下每个 dp[i] 存储 O(N) 个不同的 diff
#
# 关键点:
# - 使用字典而非二维数组存储，因为 diff 的取值范围很大
# - dp[i][diff] = dp[j].get(diff, 1) + 1 巧妙处理了初始化
# - 最少两个元素即可构成等差子序列（长度为2）
