"""
LeetCode #3176 - Find the Maximum Length of a Good Subsequence I
求出最长好子序列 I
https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i/

给你一个整数数组 `nums` 和一个 非负 整数 `k` 。如果一个整数序列 `seq` 满足在下标范围 `[0, seq.length - 2]` 中 最多只有 `k` 个下标 `i` 满足 `seq[i] != seq[i + 1]` ，那么我们称这个整数序列为 好 序列。
请你返回 `nums` 中 好 子序列 的最长长度。

示例 1：

输入：nums = [1,2,1,1,3], k = 2
输出：4
解释：
最长好子序列为 `[1,2,1,1,3]` 。
示例 2：

输入：nums = [1,2,3,4,5,1], k = 0
输出：2
解释：
最长好子序列为 `[1,2,3,4,5,1]` 。

提示：
`1 <= nums.length <= 500`
`1 <= nums[i] <= 10^9`
`0 <= k <= min(nums.length, 25)`
"""

from typing import List, Optional


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i][c] = 以i结尾且有c个不等相邻对的最长子序列长度
        dp = [[1] * (k + 1) for _ in range(n)]
        ans = 1

        for i in range(n):
            for c in range(k + 1):
                for j in range(i):
                    if nums[j] == nums[i]:
                        dp[i][c] = max(dp[i][c], dp[j][c] + 1)
                    elif c > 0:
                        dp[i][c] = max(dp[i][c], dp[j][c - 1] + 1)
                ans = max(ans, dp[i][c])

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Dynamic Programming
#
# 解题思路:
# 动态规划：dp[i][c]表示以第i个元素结尾、恰好有c个不等相邻对的子序列最大长度。
# 转移：枚举j<i，若nums[j]==nums[i]则dp[i][c]=max(dp[j][c]+1)；
# 若nums[j]!=nums[i]且c>0则dp[i][c]=max(dp[j][c-1]+1)。
# n<=500, k<=25, O(n^2*k)=6.25M可接受。
#
# 时间复杂度: O(n^2 * k)
# 空间复杂度: O(n * k)
#
# 关键点:
# - "好序列"允许最多k次相邻不等
# - dp状态包含改变次数维度
# - 相邻相等不增加改变次数，不等则c+1
