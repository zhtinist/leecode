"""
LeetCode #1968 - Array With Elements Not Equal to Average of Neighbors
构造元素不等于两相邻元素平均值的数组
https://leetcode.cn/problems/array-with-elements-not-equal-to-average-of-neighbors/

给你一个 下标从 0 开始 的数组 `nums` ，数组由若干 互不相同的 整数组成。你打算重新排列数组中的元素以满足：重排后，数组中的每个元素都 不等于 其两侧相邻元素的 平均值 。
更公式化的说法是，重新排列的数组应当满足这一属性：对于范围 `1 <= i < nums.length - 1` 中的每个 `i` ，`(nums[i-1] + nums[i+1]) / 2` 不等于 `nums[i]` 均成立 。
返回满足题意的任一重排结果。

示例 1：
输入：nums = [1,2,3,4,5] 输出：[1,2,4,5,3] 解释： i=1, nums[i] = 2, 两相邻元素平均值为 (1+4) / 2 = 2.5 i=2, nums[i] = 4, 两相邻元素平均值为 (2+5) / 2 = 3.5 i=3, nums[i] = 5, 两相邻元素平均值为 (4+3) / 2 = 3.5
示例 2：
输入：nums = [6,2,0,9,7] 输出：[9,7,6,2,0] 解释： i=1, nums[i] = 7, 两相邻元素平均值为 (9+6) / 2 = 7.5 i=2, nums[i] = 6, 两相邻元素平均值为 (7+2) / 2 = 4.5 i=3, nums[i] = 2, 两相邻元素平均值为 (6+0) / 2 = 3

提示：
`3 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Sort and then interleave: put smaller half at even indices,
        larger half at odd indices. This guarantees each element is either
        larger than both neighbors or smaller than both neighbors.
        """
        nums.sort()
        n = len(nums)
        result = [0] * n
        # Place smaller half at even indices
        mid = (n + 1) // 2
        j = 0
        for i in range(0, n, 2):
            result[i] = nums[j]
            j += 1
        # Place larger half at odd indices
        for i in range(1, n, 2):
            result[i] = nums[j]
            j += 1

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 排序后"大小交替"排列。将较小的一半放在偶数索引，较大的一半放在奇数索引。
# 这样每个元素的两个邻居要么都大于它，要么都小于它，
# 因此其值不可能等于邻居的平均值。
# 例如 [1,2,3,4,5] 排序后交错得到 [1,3,2,5,4] 或 [1,4,2,5,3]。
# 核心保证：(nums[i-1] + nums[i+1]) / 2 != nums[i]。
#
# 时间复杂度: O(N log N)，排序主导
# 空间复杂度: O(N)，结果数组
#
# 关键点:
# - 将排序后的数组分成较小半和较大半交叉放置
# - 交错排列确保每个元素邻居的值要么都比它大，要么都比它小
# - 不存在"一个比它大一个比它小"的相邻组合
