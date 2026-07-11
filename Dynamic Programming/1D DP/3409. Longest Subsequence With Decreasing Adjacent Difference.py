"""
LeetCode #3409 - Longest Subsequence With Decreasing Adjacent Difference
最长相邻绝对差递减子序列
https://leetcode.cn/problems/longest-subsequence-with-decreasing-adjacent-difference/

给你一个整数数组 `nums` 。
你的任务是找到 `nums` 中的 最长 子序列 `seq` ，这个子序列中相邻元素的 绝对差 构成一个 非递增 整数序列。换句话说，`nums` 中的序列 `seq_0`, `seq_1`, `seq_2`, ..., `seq_m` 满足 `|seq_1 - seq_0| >= |seq_2 - seq_1| >= ... >= |seq_m - seq_m - 1|` 。
请你返回这个子序列的长度。

示例 1：

输入：nums = [16,6,3]
输出：3
解释：
最长子序列是 `[16, 6, 3]` ，相邻绝对差值为 `[10, 3]` 。
示例 2：

输入：nums = [6,5,3,4,2,1]
输出：4
解释：
最长子序列是 `[6, 4, 2, 1]` ，相邻绝对差值为 `[2, 2, 1]` 。
示例 3：

输入：nums = [10,20,10,19,10,20]
输出：5
解释：
最长子序列是 `[10, 20, 10, 19, 10]` ，相邻绝对差值为 `[10, 10, 9, 9]` 。

提示：
`2 <= nums.length <= 10^4`
`1 <= nums[i] <= 300`
"""

from typing import List, Optional


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        max_val = max(nums)
        # best[v][d] = longest subsequence ending with value v and last diff >= d
        best = [[1] * (max_val + 2) for _ in range(max_val + 1)]

        for i, x in enumerate(nums):
            cur = [1] * (max_val + 2)
            for v in range(1, max_val + 1):
                diff = abs(x - v)
                if best[v][diff] > 0:
                    cur[diff] = max(cur[diff], best[v][diff] + 1)
            # propagate to smaller differences
            for d in range(max_val, -1, -1):
                cur[d] = max(cur[d], cur[d + 1])
                best[x][d] = max(best[x][d], cur[d])

        return max(best[v][0] for v in range(1, max_val + 1))



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# DP，best[val][d]表示以值val结尾且最后一个相邻差>=d的最长子序列长度。
# 因为nums[i]<=300，所以max_diff<=300。对每个新元素x，枚举前一个值v（1..300），
# 计算diff=|x-v|，尝试从best[v][diff]+1转移。然后向后传播cur[d]=max(cur[d], cur[d+1])。
# 更新best[x]。
#
# 时间复杂度: O(n * max_val)，max_val <= 300
# 空间复杂度: O(max_val^2)
#
# 关键点:
# - 值域小（<=300），用值代替索引做DP
# - dp[d]表示最后差值>=d的最大长度，通过后缀max传播
