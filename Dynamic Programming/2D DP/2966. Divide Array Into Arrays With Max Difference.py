"""
LeetCode #2966 - Divide Array Into Arrays With Max Difference
划分数组并满足最大差限制
https://leetcode.cn/problems/divide-array-into-arrays-with-max-difference/

给你一个长度为 `n` 的整数数组 `nums`，以及一个正整数 `k` 。
将这个数组划分为 `n / 3` 个长度为 `3` 的子数组，并满足以下条件：
子数组中 任意 两个元素的差必须 小于或等于 `k` 。
返回一个 二维数组 ，包含所有的子数组。如果不可能满足条件，就返回一个空数组。如果有多个答案，返回 任意一个 即可。

示例 1：

输入：nums = [1,3,4,8,7,9,3,5,1], k = 2
输出：[[1,1,3],[3,4,5],[7,8,9]]
解释：
每个数组中任何两个元素之间的差小于或等于 2。
示例 2：

输入：nums = [2,4,2,2,5,2], k = 2
输出：[]
解释：
将 `nums` 划分为 2 个长度为 3 的数组的不同方式有：
[[2,2,2],[2,4,5]] （及其排列）
[[2,2,4],[2,2,5]] （及其排列）
因为有四个 2，所以无论我们如何划分，都会有一个包含元素 2 和 5 的数组。因为 `5 - 2 = 3 > k`，条件无法被满足，所以没有合法的划分。
示例 3：

输入：nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14
输出：[[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]
解释：
每个数组中任何两个元素之间的差小于或等于 14。

提示：
`n == nums.length`
`1 <= n <= 10^5`
`n` 是 `3` 的倍数
`1 <= nums[i] <= 10^5`
`1 <= k <= 10^5`
"""

from typing import List, Optional


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """
        Sort the array and greedily group every 3 consecutive elements.
        For each group of 3, check if max - min <= k.
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(0, n, 3):
            # Group nums[i], nums[i+1], nums[i+2]
            if nums[i + 2] - nums[i] > k:
                return []
            result.append([nums[i], nums[i + 1], nums[i + 2]])

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 贪心策略：对数组排序后，每 3 个连续元素为一组。排序后相邻元素的差最小，
# 如果排序后某组首尾元素之差超过 k，则无法满足条件返回空数组；否则该分组方案有效。
#
# 时间复杂度: O(n log n)，主要开销在排序
# 空间复杂度: O(1)，排序为原地排序，结果数组不算额外空间（或 O(n) 若考虑结果）
#
# 关键点:
# - 排序是核心思路：将相近的元素放在一起，最小化组内差值
# - 每组只需检查最小和最大元素的差（排序后即首尾元素）
# - 贪心正确性：排序后的分组是最优的，如果排序后都无法满足，则不存在合法方案
