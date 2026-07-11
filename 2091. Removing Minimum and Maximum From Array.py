"""
LeetCode #2091 - Removing Minimum and Maximum From Array
从数组中移除最大值和最小值
https://leetcode.cn/problems/removing-minimum-and-maximum-from-array/

给你一个下标从 0 开始的数组 `nums` ，数组由若干 互不相同 的整数组成。
`nums` 中有一个值最小的元素和一个值最大的元素。分别称为 最小值 和 最大值 。你的目标是从数组中移除这两个元素。
一次 删除 操作定义为从数组的 前面 移除一个元素或从数组的 后面 移除一个元素。
返回将数组中最小值和最大值 都 移除需要的最小删除次数。

示例 1：
输入：nums = [2,10,7,5,4,1,8,6] 输出：5 解释： 数组中的最小元素是 nums[5] ，值为 1 。 数组中的最大元素是 nums[1] ，值为 10 。 将最大值和最小值都移除需要从数组前面移除 2 个元素，从数组后面移除 3 个元素。 结果是 2 + 3 = 5 ，这是所有可能情况中的最小删除次数。
示例 2：
输入：nums = [0,-4,19,1,8,-2,-3,5] 输出：3 解释： 数组中的最小元素是 nums[1] ，值为 -4 。 数组中的最大元素是 nums[2] ，值为 19 。 将最大值和最小值都移除需要从数组前面移除 3 个元素。 结果是 3 ，这是所有可能情况中的最小删除次数。
示例 3：
输入：nums = [101] 输出：1 解释： 数组中只有这一个元素，那么它既是数组中的最小值又是数组中的最大值。 移除它只需要 1 次删除操作。

提示：
`1 <= nums.length <= 10^5`
`-10^5 <= nums[i] <= 10^5`
`nums` 中的整数 互不相同
"""

from typing import List, Optional


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # Find indices of min and max
        min_idx = 0
        max_idx = 0
        for i in range(n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i

        # Make sure min_idx <= max_idx for easier calculation
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Three strategies:
        # 1) Delete both from left: right + 1
        # 2) Delete both from right: n - left
        # 3) Delete one from left, one from right: (left + 1) + (n - right)
        return min(right + 1, n - left, left + 1 + n - right)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 找到数组中最小值和最大值的索引。有三种删除策略：
# 1) 从左边删除到较远的那个元素（right+1次）
# 2) 从右边删除到较近的那个元素（n-left次）
# 3) 从左边删到较近的，从右边删到较远的（left+1 + n-right次）
# 取三种策略的最小值。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 找到min/max索引
# - 三种删除策略枚举
# - 两种元素可以分别从两端删除
