"""
LeetCode #2874 - Maximum Value of an Ordered Triplet II
有序三元组中的最大值 II
https://leetcode.cn/problems/maximum-value-of-an-ordered-triplet-ii/

给你一个下标从 0 开始的整数数组 `nums` 。
请你从所有满足 `i < j < k` 的下标三元组 `(i, j, k)` 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 `0` 。
下标三元组 `(i, j, k)` 的值等于 `(nums[i] - nums[j]) * nums[k]` 。

示例 1：
输入：nums = [12,6,1,2,7] 输出：77 解释：下标三元组 (0, 2, 4) 的值是 (nums[0] - nums[2]) * nums[4] = 77 。 可以证明不存在值大于 77 的有序下标三元组。
示例 2：
输入：nums = [1,10,3,4,19] 输出：133 解释：下标三元组 (1, 2, 4) 的值是 (nums[1] - nums[2]) * nums[4] = 133 。 可以证明不存在值大于 133 的有序下标三元组。
示例 3：
输入：nums = [1,2,3] 输出：0 解释：唯一的下标三元组 (0, 1, 2) 的值是一个负数，(nums[0] - nums[1]) * nums[2] = -3 。因此，答案是 0 。

提示：
`3 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_i = nums[0]      # maximum nums[i] seen so far
        max_ij = float('-inf')  # maximum (nums[i] - nums[j]) seen so far
        ans = 0
        for k in range(2, n):
            # Update max_ij using nums[k-1] as j
            max_ij = max(max_ij, max_i - nums[k - 1])
            max_i = max(max_i, nums[k - 1])
            # Use nums[k] as k
            ans = max(ans, max_ij * nums[k])
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array
#
# 解题思路:
# 维护两个变量：max_i（当前见过的最大 nums[i]）和 max_ij（当前见过的最大 (nums[i]-nums[j])）。
# 遍历 nums，对于位置 k>=2，用 nums[k] 作为第三个数，同时用 nums[k-1] 更新 max_ij（作为新的 j）和 max_i（作为新的 i）。
# ans = max(ans, max_ij * nums[k])，最终若 ans < 0 则返回 0。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 一次遍历，动态维护 max_i 和 max_ij
# - 对于每个 k，先更新 max_ij = max(max_ij, max_i - nums[k-1])
# - 答案为负时返回0（题意要求）
