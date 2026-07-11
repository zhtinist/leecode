"""
LeetCode #1043 - Partition Array for Maximum Sum
中文题名：分隔数组以得到最大和
https://leetcode.com/problems/partition-array-for-maximum-sum/

Given an integer array `A`, you partition the array into (contiguous) subarrays of
length at most `K`.  After partitioning, each subarray has their values
changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

Example 1:

Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]

Note:

`1 <= K <= A.length <= 500`

`0 <= A[i] <= 10^6`

【中文翻译】
给定一个整数数组 A，你将数组划分为长度最多为 K 的（连续）子数组。划分后，每个子数组的值变为该子数组中的最大值。

返回划分后数组的最大可能总和。

示例 1：

输入：A = [1,15,7,9,2,5,10], K = 3
输出：84
解释：A 变为 [15,15,15,9,10,10,10]

注意：

1 <= K <= A.length <= 500
0 <= A[i] <= 10^6
"""

from typing import List, Optional


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            cur_max = 0
            # Check partitions of length 1..k ending at i-1
            for j in range(1, min(k, i) + 1):
                cur_max = max(cur_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + cur_max * j)

        return dp[n]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划。定义 dp[i] 为前 i 个元素（A[0..i-1]）划分后的最大总和。
# 对于每个位置 i，考虑以 A[i-1] 结尾的最后一个子数组的长度 j（1 <= j <= min(k, i)）。
# 当最后一个子数组长度为 j 时，该子数组包含 A[i-j..i-1]，
# 子数组的最大值为 cur_max = max(A[i-j..i-1])。
# dp[i] = max(dp[i-j] + cur_max * j)，遍历所有可能的 j。
# 在遍历 j 的过程中可以同时维护 cur_max，避免重复计算。
#
# 时间复杂度: O(N * K) - 外层N，内层最多K
# 空间复杂度: O(N) - DP数组
#
# 关键点:
# - dp[i] 表示前i个元素的最优解
# - 从后往前考虑最后一个分区，长度从1到K
# - 一边扩展分区一边维护分区内的最大值
