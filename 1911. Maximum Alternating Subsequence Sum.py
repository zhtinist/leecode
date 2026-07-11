"""
LeetCode #1911 - Maximum Alternating Subsequence Sum
最大交替子序列和
https://leetcode.cn/problems/maximum-alternating-subsequence-sum/

一个下标从 0 开始的数组的 交替和 定义为 偶数 下标处元素之 和 减去 奇数 下标处元素之 和 。
比方说，数组 `[4,2,5,3]` 的交替和为 `(4 + 5) - (2 + 3) = 4` 。
给你一个数组 `nums` ，请你返回 `nums` 中任意子序列的 最大交替和 （子序列的下标 重新 从 0 开始编号）。
一个数组的 子序列 是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说，`[2,7,4]` 是 `[4,2,3,7,2,1,4]` 的一个子序列（加粗元素），但是 `[2,4,2]` 不是。

示例 1：
输入：nums = [4,2,5,3] 输出：7 解释：最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。
示例 2：
输入：nums = [5,6,7,8] 输出：8 解释：最优子序列为 [8] ，交替和为 8 。
示例 3：
输入：nums = [6,2,1,2,4,5] 输出：10 解释：最优子序列为 [6,1,5] ，交替和为 (6 + 5) - 1 = 10 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # dp_even: max alternating sum ending at even index (0-based in subsequence)
        # dp_odd: max alternating sum ending at odd index
        dp_even = 0  # empty subsequence has sum 0
        dp_odd = float('-inf')  # invalid initially

        for num in nums:
            # For each number, we can either skip it or include it
            # Include as even index: previous must be odd, add num
            new_even = max(dp_even, dp_odd + num)
            # Include as odd index: previous must be even, subtract num
            new_odd = max(dp_odd, dp_even - num)
            dp_even, dp_odd = new_even, new_odd

        return dp_even



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 动态规划：维护两个状态。
# - dp_even：以偶数下标结尾的子序列的最大交替和
# - dp_odd：以奇数下标结尾的子序列的最大交替和
#
# 对于每个元素 num：
# - 作为偶数下标：前一个必须是奇数下标，交替和 = dp_odd + num
# - 作为奇数下标：前一个必须是偶数下标，交替和 = dp_even - num
# - 也可以选择不选当前元素，保持原值。
#
# 最终答案为 dp_even（子序列总是以偶数下标开始，也必须以偶数下标结束
# 才能得到最大交替和，因为最后一项是加）。
#
# 时间复杂度: O(n) — 遍历数组一次
# 空间复杂度: O(1) — 只维护两个状态变量
#
# 关键点:
# - 子序列的下标重新从0开始编号
# - 交替和 = 偶数下标和 - 奇数下标和
# - 空子序列不算，但 dp_even 初始为 0 可以处理
# - 类似于股票买卖问题（最佳买卖时机）
