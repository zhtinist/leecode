"""
LeetCode #2453 - Destroy Sequential Targets
摧毁一系列目标
https://leetcode.cn/problems/destroy-sequential-targets/

给你一个下标从 0 开始的数组 `nums` ，它包含若干正整数，表示数轴上你需要摧毁的目标所在的位置。同时给你一个整数 `space` 。
你有一台机器可以摧毁目标。给机器 输入 `nums[i]` ，这台机器会摧毁所有位置在 `nums[i] + c * space` 的目标，其中 `c` 是任意非负整数。你想摧毁 `nums` 中 尽可能多 的目标。
请你返回在摧毁数目最多的前提下，`nums[i]` 的 最小值 。

示例 1：
输入：nums = [3,7,8,1,1,5], space = 2 输出：1 解释：如果我们输入 nums[3] ，我们可以摧毁位于 1,3,5,7,9,... 这些位置的目标。 这种情况下， 我们总共可以摧毁 5 个目标（除了 nums[2]）。 没有办法摧毁多于 5 个目标，所以我们返回 nums[3] 。
示例 2：
输入：nums = [1,3,5,2,4,6], space = 2 输出：1 解释：输入 nums[0] 或者 nums[3] 都会摧毁 3 个目标。 没有办法摧毁多于 3 个目标。 由于 nums[0] 是最小的可以摧毁 3 个目标的整数，所以我们返回 1 。
示例 3：
输入：nums = [6,2,5], space = 100 输出：2 解释：无论我们输入哪个数字，都只能摧毁 1 个目标。输入的最小整数是 nums[1] 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`1 <= space <= 10^9`
"""

from typing import List, Optional


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # Group nums by remainder modulo space
        # For each remainder, track: (count, min_value)
        groups = {}
        for x in nums:
            r = x % space
            if r not in groups:
                groups[r] = [1, x]  # [count, min_value]
            else:
                groups[r][0] += 1
                if x < groups[r][1]:
                    groups[r][1] = x

        # Find the group with max count; tie-break by smaller min_value
        max_count = 0
        best_min = float('inf')
        for count, min_val in groups.values():
            if count > max_count or (count == max_count and min_val < best_min):
                max_count = count
                best_min = min_val

        return best_min


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Counting
#
# 解题思路:
# 核心洞察：两个数字 nums[i] 和 nums[j] 摧毁相同的目标集合，当且仅当它们模 space 的余数相同。
# 因为 nums[i] + c*space 的所有目标与 nums[i] 同余数模 space。
# 因此，按 nums[i] % space 分组。对于每个余数组，记录组内元素数量和最小值。
# 找到数量最大的组；如果平局，选择最小值更小的组。返回该组的 minimum value。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 同余分组：nums[i] % space 相同的数字能摧毁相同集合的目标
# - 哈希表分组：使用字典按余数分组，同时维护每组的 count 和 min_value
# - 平局处理：多组 count 相同时，选择 min_value 最小的
