"""
LeetCode #2555 - Maximize Win From Two Segments
两个线段获得的最多奖品
https://leetcode.cn/problems/maximize-win-from-two-segments/

在 X轴 上有一些奖品。给你一个整数数组 `prizePositions` ，它按照 非递减 顺序排列，其中 `prizePositions[i]` 是第 `i` 件奖品的位置。数轴上一个位置可能会有多件奖品。再给你一个整数 `k` 。
你可以同时选择两个端点为整数的线段。每个线段的长度都必须是 `k` 。你可以获得位置在任一线段上的所有奖品（包括线段的两个端点）。注意，两个线段可能会有相交。
比方说 `k = 2` ，你可以选择线段 `[1, 3]` 和 `[2, 4]` ，你可以获得满足 `1 <= prizePositions[i] <= 3` 或者 `2 <= prizePositions[i] <= 4` 的所有奖品 i 。
请你返回在选择两个最优线段的前提下，可以获得的 最多 奖品数目。

示例 1：
输入：prizePositions = [1,1,2,2,3,3,5], k = 2 输出：7 解释：这个例子中，你可以选择线段 [1, 3] 和 [3, 5] ，获得 7 个奖品。
示例 2：
输入：prizePositions = [1,2,3,4], k = 0 输出：2 解释：这个例子中，一个选择是选择线段 `[3, 3]` 和 `[4, 4]` ，获得 2 个奖品。

提示：
`1 <= prizePositions.length <= 10^5`
`1 <= prizePositions[i] <= 10^9`
`0 <= k <= 10^9 `
`prizePositions` 有序非递减。
"""

from typing import List, Optional


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        # best[i] = max prizes covered by one segment within [0..i]
        best = [0] * n
        left = 0
        for right in range(n):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            cur = right - left + 1
            if right == 0:
                best[right] = cur
            else:
                best[right] = max(best[right - 1], cur)

        ans = 0
        left = 0
        for right in range(n):
            while prizePositions[right] - prizePositions[left] > k:
                left += 1
            cur = right - left + 1
            prev = best[left - 1] if left > 0 else 0
            ans = max(ans, cur + prev)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Sliding Window
#
# 解题思路:
# 先计算每个位置作为右端点时一个片段能覆盖的最多奖品数（滑动窗口）。
# 用best数组记录到每个位置为止单个片段的最大覆盖数。然后再次遍历，
# 对于每个右端点j的片段，找出左端点left，答案=max(当前片段覆盖数+best[left-1])，
# 即左右两个不重叠（或刚好接触）片段的最大覆盖数之和。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 滑动窗口计算以每个位置结尾的片段覆盖数
# - best数组用前缀最大值维护"第一个片段的最佳选择"
# - 两片段可以重叠，但用left-1保证不重复计算更能找到最优（重叠时总优于分开）
