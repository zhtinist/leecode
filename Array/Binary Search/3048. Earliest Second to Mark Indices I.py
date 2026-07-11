"""
LeetCode #3048 - Earliest Second to Mark Indices I
标记所有下标的最早秒数 I
https://leetcode.cn/problems/earliest-second-to-mark-indices-i/

给你两个下标从 1 开始的整数数组 `nums` 和 `changeIndices` ，数组的长度分别为 `n` 和 `m` 。
一开始，`nums` 中所有下标都是未标记的，你的任务是标记 `nums` 中 所有 下标。
从第 `1` 秒到第 `m` 秒（包括 第 `m` 秒），对于每一秒 `s` ，你可以执行以下操作 之一 ：
选择范围 `[1, n]` 中的一个下标 `i` ，并且将 `nums[i]` 减少 `1` 。
如果 `nums[changeIndices[s]]` 等于 `0` ，标记 下标 `changeIndices[s]` 。
什么也不做。
请你返回范围 `[1, m]` 中的一个整数，表示最优操作下，标记 `nums` 中 所有 下标的 最早秒数 ，如果无法标记所有下标，返回 `-1` 。

示例 1：
输入：nums = [2,2,0], changeIndices = [2,2,2,2,3,2,2,1] 输出：8 解释：这个例子中，我们总共有 8 秒。按照以下操作标记所有下标： 第 1 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [1,2,0] 。 第 2 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [0,2,0] 。 第 3 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [0,1,0] 。 第 4 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [0,0,0] 。 第 5 秒，标​​​​​记 changeIndices[5] ，也就是标记下标 3 ，因为 nums[3] 等于 0 。 第 6 秒，标​​​​​记 changeIndices[6] ，也就是标记下标 2 ，因为 nums[2] 等于 0 。 第 7 秒，什么也不做。 第 8 秒，标记 changeIndices[8] ，也就是标记下标 1 ，因为 nums[1] 等于 0 。 现在所有下标已被标记。 最早可以在第 8 秒标记所有下标。 所以答案是 8 。
示例 2：
输入：nums = [1,3], changeIndices = [1,1,1,2,1,1,1] 输出：6 解释：这个例子中，我们总共有 7 秒。按照以下操作标记所有下标： 第 1 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,2] 。 第 2 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,1] 。 第 3 秒：选择下标 2 ，将 nums[2] 减少 1 。nums 变为 [1,0] 。 第 4 秒：标​​​​​记 changeIndices[4] ，也就是标记下标 2 ，因为 nums[2] 等于 0 。 第 5 秒：选择下标 1 ，将 nums[1] 减少 1 。nums 变为 [0,0] 。 第 6 秒：标​​​​​记 changeIndices[6] ，也就是标记下标 1 ，因为 nums[1] 等于 0 。 现在所有下标已被标记。 最早可以在第 6 秒标记所有下标。 所以答案是 6 。
示例 3：
Input: nums = [0,1], changeIndices = [2,2,2] Output: -1 Explanation: 这个例子中，无法标记所有下标，因为下标 1 不在 changeIndices 中。 所以答案是 -1 。

提示：
`1 <= n == nums.length <= 2000`
`0 <= nums[i] <= 10^9`
`1 <= m == changeIndices.length <= 2000`
`1 <= changeIndices[i] <= n`
"""

from typing import List, Optional


class Solution:
    def earliestSecondToMarkIndices(
        self, nums: List[int], changeIndices: List[int]
    ) -> int:
        """
        Binary search the earliest second. For a given t, check if
        all indices can be marked. Greedy: mark each index at its
        last occurrence within [0, t), do decrements before deadlines.
        """
        n = len(nums)
        m = len(changeIndices)

        def can_mark_all(t: int) -> bool:
            """Check if all indices can be marked within first t seconds."""
            # Last second (0-indexed) each index appears
            last = [-1] * n
            for s in range(t):
                idx = changeIndices[s] - 1  # 0-indexed
                last[idx] = s

            # Every index must appear at least once
            for i in range(n):
                if last[i] == -1:
                    return False

            # Sort indices by their deadline (last occurrence)
            indices = sorted(range(n), key=lambda i: last[i])

            total_ops = 0  # total decrement + mark operations so far
            for i in indices:
                # Need nums[i] decrements + 1 mark operation
                total_ops += nums[i] + 1
                # Must fit within deadline (last[i] seconds have passed, 0-indexed)
                if total_ops > last[i] + 1:
                    return False

            return True

        lo, hi = 1, m
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_mark_all(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search
#
# 解题思路:
# 二分搜索最早秒数 t。对于给定的 t，判断前 t 秒内是否能标记所有下标。
# 贪心策略：每个下标在其最后一次出现的秒数被标记（因为越晚标记，前面的时间可以用于减操作）。
# 对于每个下标 i，需要 nums[i] 次减操作 + 1 次标记操作。
# 按最后出现时间排序，依次检查累计所需操作数是否超过对应时间限制。
#
# 时间复杂度: O(m * log m)，每次检查 O(n + m)
# 空间复杂度: O(n)
#
# 关键点:
# - 二分查找 + 贪心验证：单调性（时间越长越容易完成）
# - 每个下标在最后出现位置标记最优（留有最多减操作时间）
# - 累计操作数 = 已处理下标的减操作总数 + 已处理下标数，必须 <= 当前截止时间
