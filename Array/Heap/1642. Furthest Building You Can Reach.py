"""
LeetCode #1642 - Furthest Building You Can Reach
中文题名：可以到达的最远建筑
https://leetcode.com/problems/furthest-building-you-can-reach/

You are given an integer array `heights` representing the heights of
buildings, some `bricks`, and some `ladders`.

You start your journey from building `0` and move to the next building by
possibly using bricks or ladders.

While moving from building `i` to building `i+1` (0-indexed),

If the current building's height is greater than or equal to
the next building's height, you do not need a ladder or bricks.

If the current building's height is less than the next building's height,
you can either use one ladder or `(h[i+1] - h[i])`
bricks.

Return the furthest building index (0-indexed) you can reach if you use the given
ladders and bricks optimally.

Example 1:

Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3

Constraints:

`1 <= heights.length <= 105`

`1 <= heights[i] <= 106`

`0 <= bricks <= 109`

`0 <= ladders <= heights.length`

【中文翻译】
给定一个整数数组 heights 表示建筑物的高度，以及一些砖块 bricks 和梯子 ladders。
从建筑 0 出发，向建筑 n-1 移动。从建筑 i 到 i+1 时：
- 如果 heights[i+1] <= heights[i]，不需要任何道具
- 如果 heights[i+1] > heights[i]，可以使用一个梯子 或 (heights[i+1] - heights[i]) 个砖块
求能到达的最远建筑索引（从0开始）。

示例 1：
输入: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
输出: 4
解释: 从0到1不用道具。到2需攀爬5，用梯子。到3下坡。到4攀爬3，用砖块。无法到达建筑5。
"""

from typing import List, Optional
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            heapq.heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i

        return n - 1
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心 + 最小堆。策略：最大的 ladders 个高度差用梯子，其余的用砖块。
# 最小堆存储当前被砖块支付的高度差。当堆大小超过 ladders 时，弹出最小的用砖块支付。
# 如果砖块不够（bricks < 0），返回当前索引。
#
# 时间复杂度: O(N log L) — L 为梯子数量
# 空间复杂度: O(L) — 堆的大小
#
# 关键点:
# - 始终用梯子替换最大的 diff，砖块支付最小的 diff
# - 最小堆配合贪心策略灵活高效
