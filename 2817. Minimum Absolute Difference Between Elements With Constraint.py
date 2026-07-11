"""
LeetCode #2817 - Minimum Absolute Difference Between Elements With Constraint
限制条件下元素之间的最小绝对差
https://leetcode.cn/problems/minimum-absolute-difference-between-elements-with-constraint/

给你一个下标从 0 开始的整数数组 `nums` 和一个整数 `x` 。
请你找到数组中下标距离至少为 `x` 的两个元素的 差值绝对值 的 最小值 。
换言之，请你找到两个下标 `i` 和 `j` ，满足 `abs(i - j) >= x` 且 `abs(nums[i] - nums[j])` 的值最小。
请你返回一个整数，表示下标距离至少为 `x` 的两个元素之间的差值绝对值的 最小值 。

示例 1：
输入：nums = [4,3,2,4], x = 2 输出：0 解释：我们选择 nums[0] = 4 和 nums[3] = 4 。 它们下标距离满足至少为 2 ，差值绝对值为最小值 0 。 0 是最优解。
示例 2：
输入：nums = [5,3,2,10,15], x = 1 输出：1 解释：我们选择 nums[1] = 3 和 nums[2] = 2 。 它们下标距离满足至少为 1 ，差值绝对值为最小值 1 。 1 是最优解。
示例 3：
输入：nums = [1,2,3,4], x = 3 输出：3 解释：我们选择 nums[0] = 1 和 nums[3] = 4 。 它们下标距离满足至少为 3 ，差值绝对值为最小值 3 。 3 是最优解。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`0 <= x < nums.length`
"""

from typing import List, Optional


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        from sortedcontainers import SortedList
        sl = SortedList()
        n = len(nums)
        ans = float('inf')
        for i in range(x, n):
            sl.add(nums[i - x])
            idx = sl.bisect_left(nums[i])
            if idx < len(sl):
                ans = min(ans, abs(sl[idx] - nums[i]))
            if idx > 0:
                ans = min(ans, abs(sl[idx - 1] - nums[i]))
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Ordered Set
#
# 解题思路:
# 使用平衡树（SortedList）维护一个大小为 n-x 的滑动窗口。
# 对于每个 i (从 x 开始)，窗口包含 nums[0] ~ nums[i-x]（即与 nums[i] 下标距离 >= x 的元素）。
# 在有序窗口中二分查找 nums[i] 的位置，比较其前驱和后继，取最小差值。
# 遍历所有 i 更新全局最小答案。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - SortedList 支持 O(log n) 的插入和二分查找
# - 对于每个 nums[i]，只需比较窗口中距离它最近的两个元素（前驱和后继）
# - 因为窗口内元素排序后，最小差值一定在相邻元素之间
