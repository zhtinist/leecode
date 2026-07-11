"""
LeetCode #2915 - Length of the Longest Subsequence That Sums to Target
和为目标值的最长子序列的长度
https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/

给你一个下标从 0 开始的整数数组 `nums` 和一个整数 `target` 。
返回和为 `target` 的 `nums` 子序列中，子序列 长度的最大值 。如果不存在和为 `target` 的子序列，返回 `-1` 。
子序列 指的是从原数组中删除一些或者不删除任何元素后，剩余元素保持原来的顺序构成的数组。

示例 1：
输入：nums = [1,2,3,4,5], target = 9 输出：3 解释：总共有 3 个子序列的和为 9 ：[4,5] ，[1,3,5] 和 [2,3,4] 。最长的子序列是 [1,3,5] 和 [2,3,4] 。所以答案为 3 。
示例 2：
输入：nums = [4,1,3,2,1,5], target = 7 输出：4 解释：总共有 5 个子序列的和为 7 ：[4,3] ，[4,1,2] ，[4,2,1] ，[1,1,5] 和 [1,3,2,1] 。最长子序列为 [1,3,2,1] 。所以答案为 4 。
示例 3：
输入：nums = [1,1,5,4,5], target = 3 输出：-1 解释：无法得到和为 3 的子序列。

提示：
`1 <= nums.length <= 1000`
`1 <= nums[i] <= 1000`
`1 <= target <= 1000`
"""

from typing import List, Optional


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        INF = -10**9
        dp = [INF] * (target + 1)
        dp[0] = 0
        for x in nums:
            for w in range(target, x - 1, -1):
                if dp[w - x] != INF:
                    dp[w] = max(dp[w], dp[w - x] + 1)
        return dp[target] if dp[target] > 0 else -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 使用0/1背包的变种：dp[w] = 和为 w 的最大子序列长度。初始化 dp[0] = 0，其余为负无穷。
# 对每个数字 x，从 target 倒序遍历到 x，dp[w] = max(dp[w], dp[w-x] + 1)。
# 最后如果 dp[target] > 0 则返回该值，否则返回 -1。
#
# 时间复杂度: O(n * target)
# 空间复杂度: O(target)
#
# 关键点:
# - 经典01背包求最大物品数，价值为1（每个元素计数+1）
# - 倒序遍历确保每个元素只使用一次
# - dp 初始化为负无穷，只有 dp[0]=0
