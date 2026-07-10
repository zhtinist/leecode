"""
LeetCode #198 - House Robber
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically contact the
police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

from typing import List, Optional


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]               # dp[i-2]
        prev1 = max(nums[0], nums[1]) # dp[i-1]

        for i in range(2, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr

        return prev1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。定义 dp[i] 为偷到第 i 间房子时能获得的最大金额。
# 对于第 i 间房子，有两个选择：
# 1. 不偷第 i 间：dp[i] = dp[i-1]
# 2. 偷第 i 间：dp[i] = dp[i-2] + nums[i]（不能偷相邻的第 i-1 间）
#
# 状态转移方程：dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#
# 使用两个变量 prev2 (dp[i-2]) 和 prev1 (dp[i-1]) 滚动更新，空间优化为 O(1)。
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(1) — 只用两个变量
#
# 关键点:
# - 核心是状态转移：偷或不偷当前房子
# - 不能偷相邻的房子
# - 空数组和单元素数组的边界处理
