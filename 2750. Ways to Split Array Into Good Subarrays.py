"""
LeetCode #2750 - Ways to Split Array Into Good Subarrays
将数组划分成若干好子数组的方式
https://leetcode.cn/problems/ways-to-split-array-into-good-subarrays/

给你一个二元数组 `nums` 。
如果数组中的某个子数组 恰好 只存在 一 个值为 `1` 的元素，则认为该子数组是一个 好子数组 。
请你统计将数组 `nums` 划分成若干 好子数组 的方法数，并以整数形式返回。由于数字可能很大，返回其对 `10^9 + 7` 取余 之后的结果。
子数组是数组中的一个连续 非空 元素序列。

示例 1：
输入：nums = [0,1,0,0,1] 输出：3 解释：存在 3 种可以将 nums 划分成若干好子数组的方式： - [0,1] [0,0,1] - [0,1,0] [0,1] - [0,1,0,0] [1]
示例 2：
输入：nums = [0,1,0] 输出：1 解释：存在 1 种可以将 nums 划分成若干好子数组的方式： - [0,1,0]

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 1`
"""

from typing import List, Optional


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ones = [i for i, v in enumerate(nums) if v == 1]
        if not ones:
            return 0
        ans = 1
        for i in range(1, len(ones)):
            ans = ans * (ones[i] - ones[i - 1]) % MOD
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Dynamic Programming
#
# 解题思路:
# 好子数组要求恰好包含一个 1。因此划分只能在相邻的两个 1 之间进行。
# 找出所有 1 的位置，相邻两个 1 之间有 gap = ones[i] - ones[i-1] 个位置可以切分。
# 每个 gap 都是独立的，总方案数 = 所有 gap 的乘积。如果没有 1 则无法划分，返回 0。
#
# 时间复杂度: O(n)
# 空间复杂度: O(k) 其中 k 是 1 的个数，可优化到 O(1)
#
# 关键点:
# - 好子数组 = 恰好一个 1，所以切割必须在两个 1 之间的任意位置
# - 两个相邻 1 之间的距离就是可选的切割位置数
# - 乘法原理：各段切割方案相乘
