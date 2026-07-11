"""
LeetCode #3346 - Maximum Frequency of an Element After Performing Operations I
执行操作后元素的最高频率 I
https://leetcode.cn/problems/maximum-frequency-of-an-element-after-performing-operations-i/

给你一个整数数组 `nums` 和两个整数 `k` 和 `numOperations` 。
你必须对 `nums` 执行 操作  `numOperations` 次。每次操作中，你可以：
选择一个下标 `i` ，它在之前的操作中 没有 被选择过。
将 `nums[i]` 增加范围 `[-k, k]` 中的一个整数。
在执行完所有操作以后，请你返回 `nums` 中出现 频率最高 元素的出现次数。
一个元素 `x` 的 频率 指的是它在数组中出现的次数。

示例 1：

输入：nums = [1,4,5], k = 1, numOperations = 2
输出：2
解释：
通过以下操作得到最高频率 2 ：
将 `nums[1]` 增加 0 ，`nums` 变为 `[1, 4, 5]` 。
将 `nums[2]` 增加 -1 ，`nums` 变为 `[1, 4, 4]` 。
示例 2：

输入：nums = [5,11,20,20], k = 5, numOperations = 1
输出：2
解释：
通过以下操作得到最高频率 2 ：
将 `nums[1]` 增加 0 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
`0 <= k <= 10^5`
`0 <= numOperations <= nums.length`
"""

from typing import List, Optional


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        max_val = max(nums) + k + 2
        diff = [0] * (max_val + 2)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1
            diff[max(0, x - k)] += 1
            diff[x + k + 1] -= 1

        cur = 0
        ans = 0
        for v in range(max_val + 1):
            cur += diff[v]
            f = freq[v] if v < len(freq) else 0
            can_reach = cur
            ans = max(ans, f + min(can_reach - f, numOperations))
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Prefix Sum, Sorting, Sliding Window
#
# 解题思路:
# 使用差分数组统计每个值可以被多少个元素覆盖（每个元素可变为[nums[i]-k, nums[i]+k]
# 内的值）。然后遍历所有可能的目标值，计算原有频率 + min(可达数量 - 原有频率,
# numOperations)。取最大值。
#
# 时间复杂度: O(M + n), M = max(nums) + k
# 空间复杂度: O(M)
#
# 关键点:
# - 差分数组统计可达范围
# - 每个元素最多用一次操作
# - 最多操作numOperations次
