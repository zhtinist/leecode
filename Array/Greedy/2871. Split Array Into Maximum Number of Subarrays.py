"""
LeetCode #2871 - Split Array Into Maximum Number of Subarrays
将数组分割成最多数目的子数组
https://leetcode.cn/problems/split-array-into-maximum-number-of-subarrays/

给你一个只包含 非负 整数的数组 `nums` 。
我们定义满足 `l <= r` 的子数组 `nums[l..r]` 的分数为 `nums[l] AND nums[l + 1] AND ... AND nums[r]` ，其中 AND 是按位与运算。
请你将数组分割成一个或者更多子数组，满足：
每个 元素都 只 属于一个子数组。
子数组分数之和尽可能 小 。
请你在满足以上要求的条件下，返回 最多 可以得到多少个子数组。
一个 子数组 是一个数组中一段连续的元素。

示例 1：
输入：nums = [1,0,2,0,1,2] 输出：3 解释：我们可以将数组分割成以下子数组： - [1,0] 。子数组分数为 1 AND 0 = 0 。 - [2,0] 。子数组分数为 2 AND 0 = 0 。 - [1,2] 。子数组分数为 1 AND 2 = 0 。 分数之和为 0 + 0 + 0 = 0 ，是我们可以得到的最小分数之和。 在分数之和为 0 的前提下，最多可以将数组分割成 3 个子数组。所以返回 3 。
示例 2：
输入：nums = [5,7,1,3] 输出：1 解释：我们可以将数组分割成一个子数组：[5,7,1,3] ，分数为 1 ，这是可以得到的最小总分数。 在总分数为 1 的前提下，最多可以将数组分割成 1 个子数组。所以返回 1 。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        total_and = nums[0]
        for x in nums:
            total_and &= x
        if total_and != 0:
            return 1
        # Greedily split whenever running AND becomes 0
        ans = 0
        cur_and = (1 << 31) - 1  # all bits set (or use nums[0])
        for x in nums:
            cur_and &= x
            if cur_and == 0:
                ans += 1
                cur_and = (1 << 31) - 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Bit Manipulation, Array
#
# 解题思路:
# 首先计算整个数组的AND值。AND运算只会使值减小或不变，因此最小可能的子数组分数和就是整个数组的AND值。
# 如果总AND不为0，无法分割（分割会增加分数和），返回1。如果总AND为0，贪心地从左到右扫描，
# 每当当前AND变为0就形成一个子数组并重置，这样能得到最多的子数组。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 所有子数组分数之和的最小值 = 整个数组的AND值
# - 若总AND > 0，任何分割都会增加总和，因此不分割
# - 若总AND = 0，贪心分割：遇到0就切，重置AND
