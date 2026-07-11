"""
LeetCode #2909 - Minimum Sum of Mountain Triplets II
元素和最小的山形三元组 II
https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-ii/

给你一个下标从 0 开始的整数数组 `nums` 。
如果下标三元组 `(i, j, k)` 满足下述全部条件，则认为它是一个 山形三元组 ：
`i < j < k`
`nums[i] < nums[j]` 且 `nums[k] < nums[j]`
请你找出 `nums` 中 元素和最小 的山形三元组，并返回其 元素和 。如果不存在满足条件的三元组，返回 `-1` 。

示例 1：
输入：nums = [8,6,1,5,3] 输出：9 解释：三元组 (2, 3, 4) 是一个元素和等于 9 的山形三元组，因为：  - 2 < 3 < 4 - nums[2] < nums[3] 且 nums[4] < nums[3] 这个三元组的元素和等于 nums[2] + nums[3] + nums[4] = 9 。可以证明不存在元素和小于 9 的山形三元组。
示例 2：
输入：nums = [5,4,8,7,10,2] 输出：13 解释：三元组 (1, 3, 5) 是一个元素和等于 13 的山形三元组，因为：  - 1 < 3 < 5  - nums[1] < nums[3] 且 nums[5] < nums[3] 这个三元组的元素和等于 nums[1] + nums[3] + nums[5] = 13 。可以证明不存在元素和小于 13 的山形三元组。
示例 3：
输入：nums = [6,5,4,3,4,5] 输出：-1 解释：可以证明 nums 中不存在山形三元组。

提示：
`3 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^8`
"""

from typing import List, Optional


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float('inf')

        # left_min[i] = minimum value < nums[i] from left, or INF
        left_min = [INF] * n
        cur_min = INF
        for i in range(n):
            if cur_min < nums[i]:
                left_min[i] = cur_min
            cur_min = min(cur_min, nums[i])

        # right_min[i] = minimum value < nums[i] from right, or INF
        right_min = [INF] * n
        cur_min = INF
        for i in range(n - 1, -1, -1):
            if cur_min < nums[i]:
                right_min[i] = cur_min
            cur_min = min(cur_min, nums[i])

        ans = INF
        for i in range(n):
            if left_min[i] != INF and right_min[i] != INF:
                ans = min(ans, left_min[i] + nums[i] + right_min[i])

        return -1 if ans == INF else ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array
#
# 解题思路:
# 预处理两个数组：left_min[j] = 左侧小于 nums[j] 的最小值，right_min[j] = 右侧小于 nums[j] 的最小值。
# 由于只是要求小于 nums[j] 的最小值，若左侧全局最小值 < nums[j] 则为该值，否则不存在。
# 然后遍历所有可能的中间位置 j，计算 left_min[j] + nums[j] + right_min[j] 的最小值。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 左侧最小值若小于 nums[j]，即为最有选择（使和最小）
# - 左右侧的最小值是独立选择的，不需要配对
# - 不存在左侧或右侧满足条件的 j 直接跳过
