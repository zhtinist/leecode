"""
LeetCode #2270 - Number of Ways to Split Array
分割数组的方案数
https://leetcode.cn/problems/number-of-ways-to-split-array/

给你一个下标从 0 开始长度为 `n` 的整数数组 `nums` 。
如果以下描述为真，那么 `nums` 在下标 `i` 处有一个 合法的分割 ：
前 `i + 1` 个元素的和 大于等于 剩下的 `n - i - 1` 个元素的和。
下标 `i` 的右边 至少有一个 元素，也就是说下标 `i` 满足 `0 <= i < n - 1` 。
请你返回 `nums` 中的 合法分割 方案数。

示例 1：
输入：nums = [10,4,-8,7] 输出：2 解释： 总共有 3 种不同的方案可以将 nums 分割成两个非空的部分： - 在下标 0 处分割 nums 。那么第一部分为 [10] ，和为 10 。第二部分为 [4,-8,7] ，和为 3 。因为 10 >= 3 ，所以 i = 0 是一个合法的分割。 - 在下标 1 处分割 nums 。那么第一部分为 [10,4] ，和为 14 。第二部分为 [-8,7] ，和为 -1 。因为 14 >= -1 ，所以 i = 1 是一个合法的分割。 - 在下标 2 处分割 nums 。那么第一部分为 [10,4,-8] ，和为 6 。第二部分为 [7] ，和为 7 。因为 6 < 7 ，所以 i = 2 不是一个合法的分割。 所以 nums 中总共合法分割方案受为 2 。
示例 2：
输入：nums = [2,3,1,0] 输出：2 解释： 总共有 2 种 nums 的合法分割： - 在下标 1 处分割 nums 。那么第一部分为 [2,3] ，和为 5 。第二部分为 [1,0] ，和为 1 。因为 5 >= 1 ，所以 i = 1 是一个合法的分割。 - 在下标 2 处分割 nums 。那么第一部分为 [2,3,1] ，和为 6 。第二部分为 [0] ，和为 0 。因为 6 >= 0 ，所以 i = 2 是一个合法的分割。

提示：
`2 <= nums.length <= 10^5`
`-10^5 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        Count the number of valid split indices i (0 <= i < n-1) where
        sum of first i+1 elements >= sum of remaining elements.
        Use prefix sum vs. total sum approach: at index i, left = prefix_sum,
        right = total_sum - left. Valid if left >= right.
        """
        total_sum = sum(nums)
        prefix_sum = 0
        count = 0

        # Iterate through valid split indices: 0 to n-2 (right side needs at least 1 element)
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]
            right_sum = total_sum - prefix_sum
            if prefix_sum >= right_sum:
                count += 1

        return count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum
#
# 解题思路:
# 首先计算整个数组的总和 total_sum。然后遍历 i 从 0 到 n-2（因为分割点右侧必须至少有一个元素），
# 维护前缀和 prefix_sum（即前 i+1 个元素的和）。右侧和为 total_sum - prefix_sum。
# 当 prefix_sum >= right_sum 时，该分割点合法，计数加一。
# 这种一次遍历的方法避免了为每个分割点重复计算左右和。
#
# 时间复杂度: O(n)，其中 n 是数组长度。计算总和 O(n)，一次遍历 O(n)。
# 空间复杂度: O(1)，仅使用常数额外空间。
#
# 关键点:
# - 先计算总和，遍历时维护前缀和即可 O(1) 得到右侧和
# - 分割点 i 的范围是 [0, n-2]，确保右侧非空
# - 注意元素可能为负数（-10^5 到 10^5），使用 Python int 无需担心溢出
