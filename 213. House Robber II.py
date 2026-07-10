"""
LeetCode #213 - House Robber II
中文题名：打家劫舍 II
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have
security system connected and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the
police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.

Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

【中文翻译】
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1：

输入：[2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后再偷窃 3 号房屋（金额 = 2），因为它们相邻。

示例 2：

输入：[1,2,3,1]
输出：4
解释：先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
偷窃到的最高金额 = 1 + 3 = 4。
"""

from typing import List, Optional


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(arr):
            prev, curr = 0, 0
            for x in arr:
                prev, curr = curr, max(curr, prev + x)
            return curr

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 房屋环形排列意味着第一间和最后一间相邻，不能同时抢劫。
# 将问题分解为两个线性子问题：
# 1. 抢劫 nums[0..n-2]（不抢最后一间）
# 2. 抢劫 nums[1..n-1]（不抢第一间）
# 取两者最大值即为答案。
# 线性 House Robber 使用 DP 滚动变量优化：
#   prev 表示偷到 i-2 位置的最大值，curr 表示偷到 i-1 位置的最大值。
#   状态转移：new_curr = max(curr, prev + x)，即 max(不抢当前, 抢当前)。
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 环形问题的核心技巧：拆分为两个互斥的线性情况取最大值
# - 特殊情况 n == 1 时无法拆分，直接返回 nums[0]
# - 使用两个变量代替 DP 数组，空间优化至 O(1)
