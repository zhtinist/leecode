"""
LeetCode #1785 - Minimum Elements to Add to Form a Given Sum
中文题名：构成特定和需要添加的最少元素
https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/

You are given an integer array `nums` and two integers `limit` and `goal`. The array `nums` has an interesting property that `abs(nums[i]) <= limit`.

Return the minimum number of elements you need to add to make the sum of the array equal to `goal`. The array must maintain its property that `abs(nums[i]) <= limit`.

Note that `abs(x)` equals `x` if `x >= 0`, and `-x` otherwise.

Example 1:

Input: nums = [1,-1,1], limit = 3, goal = -4
Output: 2
Explanation: You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.

Example 2:

Input: nums = [1,-10,9,1], limit = 100, goal = 0
Output: 1

Constraints:

`1 <= nums.length <= 105`

`1 <= limit <= 106`

`-limit <= nums[i] <= limit`

`-109 <= goal <= 109`

【中文翻译】
给定整数数组 nums 和两个整数 limit 和 goal。可以向数组中添加任意数量的整数元素，
每个添加的元素绝对值不超过 limit。求使数组元素之和等于 goal 所需添加的最少元素数量。

示例 1：
输入: nums = [1,-1,1], limit = 3, goal = -4
输出: 2
解释: 当前和为 1。需要添加使总和 = -4。添加 -3 和 -2：1+(-3)+(-2)=-4。
"""

from typing import List, Optional


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(goal - sum(nums))
        # 每个元素最大贡献 limit，需 ceil(diff / limit) 个元素
        return (diff + limit - 1) // limit
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 计算当前和与目标之间的差值 diff = abs(goal - sum(nums))。
# 每个添加的元素最多贡献 limit（向目标方向），所以需要 ceil(diff / limit) 个元素。
# 向上取整公式：(diff + limit - 1) // limit。
#
# 时间复杂度: O(N) — 计算 sum(nums)
# 空间复杂度: O(1)
#
# 关键点:
# - 贪心：每个元素贡献尽可能大的值（limit）
# - 向上取整用 (a + b - 1) // b 实现
# - 元素可以为负，类似双向调整
