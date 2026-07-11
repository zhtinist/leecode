"""
LeetCode #718 - Maximum Length of Repeated Subarray
中文题名：最长重复子数组
https://leetcode.com/problems/maximum-length-of-repeated-subarray/

Given two integer arrays `A` and `B`, return the maximum length of an
subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].

Note:

1 <= len(A), len(B) <= 1000

0 <= A[i], B[i] < 100

【中文翻译】
给两个整数数组 A 和 B，返回两个数组中公共的、长度最长的子数组的长度。

示例 1：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1]。

注意：

1 <= len(A), len(B) <= 1000

0 <= A[i], B[i] < 100
"""

from typing import List, Optional


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划（DP），定义 dp[i][j] 表示以 nums1[i-1] 和 nums2[j-1] 结尾的最长公共子数组的长度。
# 状态转移方程：
# - 如果 nums1[i-1] == nums2[j-1]，则 dp[i][j] = dp[i-1][j-1] + 1
# - 否则 dp[i][j] = 0
# 在遍历过程中记录 dp[i][j] 的最大值即为答案。
# 可以优化为一维 DP，使用滚动数组将空间复杂度降至 O(min(m, n))。
#
# 时间复杂度: O(m * n) - 其中 m, n 分别是两个数组的长度
# 空间复杂度: O(m * n) - 可优化为 O(min(m, n)) 使用滚动数组
#
# 关键点:
# - dp[i][j] 定义为以 nums1[i-1] 和 nums2[j-1] 结尾的最长子数组，而非全局最长
# - 子数组（subarray）要求连续，与子序列（subsequence）不同
# - 可使用一维 DP 优化空间，但需要逆序遍历列
