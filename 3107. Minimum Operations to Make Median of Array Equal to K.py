"""
LeetCode #3107 - Minimum Operations to Make Median of Array Equal to K
使数组中位数等于 K 的最少操作数
https://leetcode.cn/problems/minimum-operations-to-make-median-of-array-equal-to-k/

给你一个整数数组 `nums` 和一个 非负 整数 `k` 。一次操作中，你可以选择任一元素 加 `1` 或者减 `1` 。
请你返回将 `nums` 中位数 变为 `k` 所需要的 最少 操作次数。
一个数组的中位数指的是数组按非递减顺序排序后最中间的元素。如果数组长度为偶数，我们选择中间两个数的较大值为中位数。

示例 1：

输入：nums = [2,5,6,8,5], k = 4
输出：2
解释：我们将 `nums[1]` 和 `nums[4]` 减 `1` 得到 `[2, 4, 6, 8, 4]` 。现在数组的中位数等于 `k` 。
示例 2：

输入：nums = [2,5,6,8,5], k = 7
输出：3
解释：我们将 `nums[1]` 增加 1 两次，并且将 `nums[2]` 增加 1 一次，得到 `[2, 7, 7, 8, 5]` 。
示例 3：

输入：nums = [1,2,3,4,5,6], k = 4
输出：0
解释：数组中位数已经等于 `k` 了。

提示：
`1 <= nums.length <= 2 * 10^5`
`1 <= nums[i] <= 10^9`
`1 <= k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mid = n // 2

        if nums[mid] == k:
            return 0

        ans = 0
        if nums[mid] < k:
            # 中位数太小，增加右半部分（包括中位数）
            for i in range(mid, n):
                if nums[i] < k:
                    ans += k - nums[i]
        else:
            # 中位数太大，减少左半部分（包括中位数）
            for i in range(mid + 1):
                if nums[i] > k:
                    ans += nums[i] - k

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 排序后中位数位于索引n//2处。为使中位数等于k，如果中位数小于k，
# 则将中位数及右侧所有小于k的元素增加到k；如果中位数大于k，
# 则将中位数及左侧所有大于k的元素减少到k。修改这些元素即可保证排序后中位数为k。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(1)（不计排序空间）
#
# 关键点:
# - 中位数在排序数组中的索引为n//2
# - 只需修改一侧的元素（小于k改右半，大于k改左半）
# - 不需要考虑偶数长度的两个中间值，因为排序后索引n//2就是较大者
