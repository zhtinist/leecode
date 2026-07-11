"""
LeetCode #2831 - Find the Longest Equal Subarray
找出最长等值子数组
https://leetcode.cn/problems/find-the-longest-equal-subarray/

给你一个下标从 0 开始的整数数组 `nums` 和一个整数 `k` 。
如果子数组中所有元素都相等，则认为子数组是一个 等值子数组 。注意，空数组是 等值子数组 。
从 `nums` 中删除最多 `k` 个元素后，返回可能的最长等值子数组的长度。
子数组 是数组中一个连续且可能为空的元素序列。

示例 1：
输入：nums = [1,3,2,3,1,3], k = 3 输出：3 解释：最优的方案是删除下标 2 和下标 4 的元素。 删除后，nums 等于 [1, 3, 3, 3] 。 最长等值子数组从 i = 1 开始到 j = 3 结束，长度等于 3 。 可以证明无法创建更长的等值子数组。
示例 2：
输入：nums = [1,1,2,2,1,1], k = 2 输出：4 解释：最优的方案是删除下标 2 和下标 3 的元素。  删除后，nums 等于 [1, 1, 1, 1] 。  数组自身就是等值子数组，长度等于 4 。  可以证明无法创建更长的等值子数组。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= nums.length`
`0 <= k <= nums.length`
"""

from typing import List, Optional


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        ans = 0
        for idx_list in pos.values():
            left = 0
            for right in range(len(idx_list)):
                while (idx_list[right] - idx_list[left] + 1) - (right - left + 1) > k:
                    left += 1
                ans = max(ans, right - left + 1)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Binary Search, Sliding Window
#
# 解题思路:
# 按值分组，记录每个值在原数组中的所有位置。对于每个值的所有位置，使用滑动窗口找到最长的一段，
# 使得删除窗口内非该值的元素数量 <= k。窗口跨度 = idx[right] - idx[left] + 1，
# 其中该值的元素 = right - left + 1，需要删除的其他元素 = 窗口跨度 - 该值元素数。
# 当需要删除的元素 > k 时收缩左边界。
#
# 时间复杂度: O(n) 每个元素最多被处理两次
# 空间复杂度: O(n) 存储位置列表
#
# 关键点:
# - 分组处理：对每个值独立做滑动窗口
# - 窗口内该值的元素数 = right - left + 1
# - 需要删除的元素 = 窗口总跨度 - 该值元素数 = (idx[right]-idx[left]+1) - (right-left+1)
# - 条件 <= k 时可以扩大窗口
