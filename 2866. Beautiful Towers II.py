"""
LeetCode #2866 - Beautiful Towers II
美丽塔 II
https://leetcode.cn/problems/beautiful-towers-ii/

给你一个长度为 `n` 下标从 0 开始的整数数组 `maxHeights` 。
你的任务是在坐标轴上建 `n` 座塔。第 `i` 座塔的下标为 `i` ，高度为 `heights[i]` 。
如果以下条件满足，我们称这些塔是 美丽 的：
`1 <= heights[i] <= maxHeights[i]`
`heights` 是一个 山脉 数组。
如果存在下标 `i` 满足以下条件，那么我们称数组 `heights` 是一个 山脉 数组：
对于所有 `0 < j <= i` ，都有 `heights[j - 1] <= heights[j]`
对于所有 `i <= k < n - 1` ，都有 `heights[k + 1] <= heights[k]`
请你返回满足 美丽塔 要求的方案中，高度和的最大值 。

示例 1：
输入：maxHeights = [5,3,4,1,1] 输出：13 解释：和最大的美丽塔方案为 heights = [5,3,3,1,1] ，这是一个美丽塔方案，因为： - 1 <= heights[i] <= maxHeights[i]   - heights 是个山脉数组，峰值在 i = 0 处。 13 是所有美丽塔方案中的最大高度和。
示例 2：
输入：maxHeights = [6,5,3,9,2,7] 输出：22 解释： 和最大的美丽塔方案为 heights = [3,3,3,9,2,2] ，这是一个美丽塔方案，因为： - 1 <= heights[i] <= maxHeights[i] - heights 是个山脉数组，峰值在 i = 3 处。 22 是所有美丽塔方案中的最大高度和。
示例 3：
输入：maxHeights = [3,2,5,5,2,3] 输出：18 解释：和最大的美丽塔方案为 heights = [2,2,5,5,2,2] ，这是一个美丽塔方案，因为： - 1 <= heights[i] <= maxHeights[i] - heights 是个山脉数组，最大值在 i = 2 处。 注意，在这个方案中，i = 3 也是一个峰值。 18 是所有美丽塔方案中的最大高度和。

提示：
`1 <= n == maxHeights <= 10^5`
`1 <= maxHeights[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        # Left-to-right: non-decreasing
        left = [0] * n
        stack = []
        cur = 0
        for i in range(n):
            h = maxHeights[i]
            width = 1
            while stack and stack[-1][1] >= h:
                prev_w, prev_h = stack.pop()
                cur -= prev_w * prev_h
                width += prev_w
            stack.append((width, h))
            cur += width * h
            left[i] = cur

        # Right-to-left: non-increasing
        right = [0] * n
        stack = []
        cur = 0
        for i in range(n - 1, -1, -1):
            h = maxHeights[i]
            width = 1
            while stack and stack[-1][1] >= h:
                prev_w, prev_h = stack.pop()
                cur -= prev_w * prev_h
                width += prev_w
            stack.append((width, h))
            cur += width * h
            right[i] = cur

        ans = 0
        for i in range(n):
            ans = max(ans, left[i] + right[i] - maxHeights[i])
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Array, Monotonic Stack
#
# 解题思路:
# 使用单调栈分别预处理每个位置左侧非递减部分的最大高度和，以及右侧非递增部分的最大高度和。
# 单调栈中存储 (宽度, 高度)，遇到更低的高度时弹出栈中高度更大的元素，合并宽度。
# 最终答案为 left[i] + right[i] - maxHeights[i] 的最大值（峰值被计算两次，需减去一次）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 单调栈维护非递减/非递增序列，合并被压平的区间
# - left[i] = 以 i 为终点的非递减序列最大和
# - right[i] = 以 i 为起点的非递增序列最大和
# - 总高度 = left[i] + right[i] - maxHeights[i]
