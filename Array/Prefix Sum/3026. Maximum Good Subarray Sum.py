"""
LeetCode #3026 - Maximum Good Subarray Sum
最大好子数组和
https://leetcode.cn/problems/maximum-good-subarray-sum/

给你一个长度为 `n` 的数组 `nums` 和一个 正 整数 `k` 。
如果 `nums` 的一个子数组中，第一个元素和最后一个元素 差的绝对值恰好 为 `k` ，我们称这个子数组为 好 的。换句话说，如果子数组 `nums[i..j]` 满足 `|nums[i] - nums[j]| == k` ，那么它是一个好子数组。
请你返回 `nums` 中 好 子数组的 最大 和，如果没有好子数组，返回 `0` 。

示例 1：
输入：nums = [1,2,3,4,5,6], k = 1 输出：11 解释：好子数组中第一个元素和最后一个元素的差的绝对值必须为 1 。好子数组有 [1,2] ，[2,3] ，[3,4] ，[4,5] 和 [5,6] 。最大子数组和为 11 ，对应的子数组为 [5,6] 。
示例 2：
输入：nums = [-1,3,2,4,5], k = 3 输出：11 解释：好子数组中第一个元素和最后一个元素的差的绝对值必须为 3 。好子数组有 [-1,3,2] 和 [2,4,5] 。最大子数组和为 11 ，对应的子数组为 [2,4,5] 。
示例 3：
输入：nums = [-1,-2,-3,-4], k = 2 输出：-6 解释：好子数组中第一个元素和最后一个元素的差的绝对值必须为 2 。好子数组有 [-1,-2,-3] 和 [-2,-3,-4] 。最大子数组和为 -6 ，对应的子数组为 [-1,-2,-3] 。

提示：
`2 <= nums.length <= 10^5`
`-10^9 <= nums[i] <= 10^9`
`1 <= k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        For each ending position j, find a starting position i where
        |nums[i] - nums[j]| == k. Maintain the minimum prefix sum before
        each value to maximize subarray sum.
        """
        ans = -10**18  # very small
        prefix = 0  # sum of nums[0..j-1]
        # min_prefix_before[value] = minimum prefix sum before any occurrence of value
        min_prefix = {}

        for j, num in enumerate(nums):
            # Check if there's a valid start with value num + k or num - k
            target1 = num + k
            target2 = num - k

            if target1 in min_prefix:
                cur_sum = (prefix + num) - min_prefix[target1]
                if cur_sum > ans:
                    ans = cur_sum

            if target2 in min_prefix:
                cur_sum = (prefix + num) - min_prefix[target2]
                if cur_sum > ans:
                    ans = cur_sum

            # Update min_prefix for current num (as potential future start)
            if num in min_prefix:
                if prefix < min_prefix[num]:
                    min_prefix[num] = prefix
            else:
                min_prefix[num] = prefix

            prefix += num

        return ans if ans > -10**17 else 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Prefix Sum
#
# 解题思路:
# 好子数组条件是 |nums[i] - nums[j]| == k。对于每个终点 j，需要找到满足 nums[i] = nums[j] ± k 的起点 i。
# 子数组和为 prefix[j] - prefix[i-1]，要最大化此值即需要最小化 prefix[i-1]。
# 使用哈希表记录每个值出现之前的"最小前缀和"，遍历过程中更新答案。
#
# 时间复杂度: O(n)，一次遍历数组
# 空间复杂度: O(n)，最坏情况下每个元素值都不同
#
# 关键点:
# - 将问题转化为：对每个 j，查找 nums[j] ± k 对应的最小前缀和
# - 前缀和技巧：子数组和 = 右端点前缀和 - 左端点前一个位置的前缀和
# - 贪心维护最小值：对于同一值的多个起始位置，只保留前缀和最小的那个
