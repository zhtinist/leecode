"""
LeetCode #3011 - Find if Array Can Be Sorted
判断一个数组是否可以变为有序
https://leetcode.cn/problems/find-if-array-can-be-sorted/

给你一个下标从 0 开始且全是 正 整数的数组 `nums` 。
一次 操作 中，如果两个 相邻 元素在二进制下 设置位 的数目 相同 ，那么你可以将这两个元素交换。你可以执行这个操作 任意次 （也可以 0 次）。
如果你可以使数组变为非降序，请你返回 `true` ，否则返回 `false` 。

示例 1：
输入：nums = [8,4,2,30,15] 输出：true 解释：我们先观察每个元素的二进制表示。 2 ，4 和 8 分别都只有一个数位为 1 ，分别为 "10" ，"100" 和 "1000" 。15 和 30 分别有 4 个数位为 1 ："1111" 和 "11110" 。 我们可以通过 4 个操作使数组非降序： - 交换 nums[0] 和 nums[1] 。8 和 4 分别只有 1 个数位为 1 。数组变为 [4,8,2,30,15] 。 - 交换 nums[1] 和 nums[2] 。8 和 2 分别只有 1 个数位为 1 。数组变为 [4,2,8,30,15] 。 - 交换 nums[0] 和 nums[1] 。4 和 2 分别只有 1 个数位为 1 。数组变为 [2,4,8,30,15] 。 - 交换 nums[3] 和 nums[4] 。30 和 15 分别有 4 个数位为 1 ，数组变为 [2,4,8,15,30] 。 数组变成有序的，所以我们返回 true 。 注意我们还可以通过其他的操作序列使数组变得有序。
示例 2：
输入：nums = [1,2,3,4,5] 输出：true 解释：数组已经是非降序的，所以我们返回 true 。
示例 3：
输入：nums = [3,16,8,4,2] 输出：false 解释：无法通过操作使数组变为非降序。

提示：
`1 <= nums.length <= 100`
`1 <= nums[i] <= 2^8`
"""

from typing import List, Optional


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        """
        Elements with same number of set bits can be freely sorted within
        their contiguous group. Check that each group's min >= previous
        group's max for the array to be sortable.
        """
        n = len(nums)
        prev_max = 0
        i = 0

        while i < n:
            j = i
            cur_min = nums[i]
            cur_max = nums[i]
            while j < n and nums[j].bit_count() == nums[i].bit_count():
                cur_min = min(cur_min, nums[j])
                cur_max = max(cur_max, nums[j])
                j += 1

            # Current group's min must be >= previous group's max
            if cur_min < prev_max:
                return False
            prev_max = cur_max
            i = j

        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Sorting
#
# 解题思路:
# 相邻元素的交换仅限于二进制中置位数相同的元素。这意味着相同置位数的连续段内部可以任意排序，
# 但不同段之间无法交换元素。因此只需检查：将每段内部排序后，全局是否有序。
# 等价于：对于每段，计算其最小值和最大值，确保当前段的最小值 >= 上一段的最大值。
#
# 时间复杂度: O(n)，一次遍历扫描所有分段
# 空间复杂度: O(1)，仅使用常数空间
#
# 关键点:
# - 相同 popcount 的连续元素形成一个可自由排序的组
# - 不同组之间不能交换，因此组的相对顺序不变
# - 只需检查相邻组的边界条件：前组的最大值 <= 后组的最小值
