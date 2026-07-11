"""
LeetCode #2865 - Beautiful Towers I
美丽塔 I
https://leetcode.cn/problems/beautiful-towers-i/

给定一个包含 `n` 个整数的数组 `heights` 表示 `n` 座连续的塔中砖块的数量。你的任务是移除一些砖块来形成一个 山脉状 的塔排列。在这种布置中，塔高度先是非递减，有一个或多个连续塔达到最大峰值，然后非递增排列。
返回满足山脉状塔排列的方案中，高度和的最大值 。

示例 1：
输入：maxHeights = [5,3,4,1,1] 输出：13 解释：我们移除一些砖块来形成 heights = [5,3,3,1,1]，峰值位于下标 0。
示例 2：
输入：maxHeights = [6,5,3,9,2,7] 输出：22 解释：我们移除一些砖块来形成 heights = [3,3,3,9,2,2]，峰值位于下标 3。
示例 3：
输入：maxHeights = [3,2,5,5,2,3] 输出：18 解释：我们移除一些砖块来形成 heights = [2,2,5,5,2,2]，峰值位于下标 2 或 3。

提示：
`1 <= n == heights.length <= 10^3`
`1 <= heights[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        for peak in range(n):
            heights = [0] * n
            heights[peak] = maxHeights[peak]
            # Left side: non-decreasing from left to peak
            for j in range(peak - 1, -1, -1):
                heights[j] = min(heights[j + 1], maxHeights[j])
            # Right side: non-increasing from peak to right
            for j in range(peak + 1, n):
                heights[j] = min(heights[j - 1], maxHeights[j])
            ans = max(ans, sum(heights))
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Array, Monotonic Stack
#
# 解题思路:
# 枚举每个位置作为山峰（峰值），从峰值向左，每个位置高度不能超过 maxHeights[j] 且不能超过右边已确定的高度；
# 从峰值向右同理。由于 n <= 1000，O(n^2) 可接受。计算每种情况的总高度，取最大值。
#
# 时间复杂度: O(n^2)
# 空间复杂度: O(n)
#
# 关键点:
# - 山峰定义：从左到右非递减，从峰到右非递增
# - 每个位置的最终高度取 min(maxHeights[j], 相邻已确定高度)
# - 枚举所有可能的峰值位置，计算最大总和
