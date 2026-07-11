"""
LeetCode #2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
数组的最小相等和
https://leetcode.cn/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

给你两个由正整数和 `0` 组成的数组 `nums1` 和 `nums2` 。
你必须将两个数组中的 所有 `0` 替换为 严格 正整数，并且满足两个数组中所有元素的和 相等 。
返回 最小 相等和 ，如果无法使两数组相等，则返回 `-1` 。

示例 1：
输入：nums1 = [3,2,0,1,0], nums2 = [6,5,0] 输出：12 解释：可以按下述方式替换数组中的 0 ： - 用 2 和 4 替换 nums1 中的两个 0 。得到 nums1 = [3,2,2,1,4] 。 - 用 1 替换 nums2 中的一个 0 。得到 nums2 = [6,5,1] 。 两个数组的元素和相等，都等于 12 。可以证明这是可以获得的最小相等和。
示例 2：
输入：nums1 = [2,0,2,0], nums2 = [1,4] 输出：-1 解释：无法使两个数组的和相等。

提示：
`1 <= nums1.length, nums2.length <= 10^5`
`0 <= nums1[i], nums2[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(x for x in nums1 if x > 0)
        zero1 = nums1.count(0)
        sum2 = sum(x for x in nums2 if x > 0)
        zero2 = nums2.count(0)

        if zero1 == 0 and zero2 == 0:
            return sum1 if sum1 == sum2 else -1

        if zero1 == 0:
            # nums1 sum is fixed. nums2 must reach sum1
            if sum1 >= sum2 + zero2:
                return sum1
            return -1

        if zero2 == 0:
            if sum2 >= sum1 + zero1:
                return sum2
            return -1

        # Both have zeros
        return max(sum1 + zero1, sum2 + zero2)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 计算每个数组的非零元素和 sum_i 以及零的个数 zero_i。由于每个零至少替换为1，
# 所以每个数组的最小可能和为 sum_i + zero_i。若两数组都没有零，则必须 sum1 == sum2。
# 若一方无零，另一方的零必须填充到恰好补足差距，且差距 ≥ zero_i。若双方都有零，答案为两者最小可能和的最大值。
#
# 时间复杂度: O(n + m)
# 空间复杂度: O(1)
#
# 关键点:
# - 零替换成严格正整数，最小值为 1
# - 无零数组的和是固定的，有零数组可以调整
# - 双方都有零时，最小相等和为 max(sum1+zero1, sum2+zero2)
