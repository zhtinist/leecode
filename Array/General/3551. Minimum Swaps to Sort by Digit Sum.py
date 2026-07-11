"""
LeetCode #3551 - Minimum Swaps to Sort by Digit Sum
数位和排序需要的最小交换次数
https://leetcode.cn/problems/minimum-swaps-to-sort-by-digit-sum/

给你一个由 互不相同 的正整数组成的数组 `nums`，需要根据每个数字的数位和（即每一位数字相加求和）按 升序 对数组进行排序。如果两个数字的数位和相等，则较小的数字排在前面。
返回将 `nums` 排列为上述排序顺序所需的 最小 交换次数。
一次 交换 定义为交换数组中两个不同位置的值。

示例 1：

输入: nums = [37,100]
输出: 1
解释:
计算每个整数的数位和：`[3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]`
根据数位和排序：`[100, 37]`。将 `37` 与 `100` 交换，得到排序后的数组。
因此，将 `nums` 排列为排序顺序所需的最小交换次数为 1。
示例 2：

输入: nums = [22,14,33,7]
输出: 0
解释:
计算每个整数的数位和：`[2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]`
根据数位和排序：`[22, 14, 33, 7]`。数组已经是排序好的。
因此，将 `nums` 排列为排序顺序所需的最小交换次数为 0。
示例 3：

输入: nums = [18,43,34,16]
输出: 2
解释:
计算每个整数的数位和：`[1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]`
根据数位和排序：`[16, 34, 43, 18]`。将 `18` 与 `16` 交换，再将 `43` 与 `34` 交换，得到排序后的数组。
因此，将 `nums` 排列为排序顺序所需的最小交换次数为 2。

提示:
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`nums` 由 互不相同 的正整数组成。
"""

from typing import List, Optional


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        # Create the target sorted array
        target = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map value -> target index
        pos = {val: idx for idx, val in enumerate(target)}

        n = len(nums)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue
            # Find the cycle size
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1
            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sorting
#
# 解题思路:
# 首先定义排序规则：按数位和升序，数位和相同时按数值升序。生成目标排序数组 target。
# 然后将问题转化为：通过交换将原数组变成 target 数组的最小交换次数。
# 这是一个经典问题 — 最小交换次数 = n - 置换环的数量。
# 将原数组每个位置的元素映射到它在 target 中的目标位置，形成置换。
# 遍历每个位置，如果未访问且不在正确位置上，追踪整个环，环长为 L 则需要 L-1 次交换将环内元素归位。
# 最终答案为所有环的 (L-1) 之和。
#
# 时间复杂度: O(n log n)，主要时间花在排序上；追踪置换环为 O(n)。
# 空间复杂度: O(n)，需要存储 target 数组、位置映射和 visited 数组。
#
# 关键点:
# - 排序键为 (digit_sum(x), x)，先按数位和再按值本身。
# - 置换环分解：最小交换次数 = 元素总数 - 环的数量。
# - 每个长度为 L 的环恰好需要 L-1 次交换即可将环内所有元素归位。
