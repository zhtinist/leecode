"""
LeetCode #1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
中文题名：切割后面积最大的蛋糕
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

Given a rectangular cake with height `h` and width `w`, and
two arrays of integers `horizontalCuts` and `verticalCuts` where
`horizontalCuts[i]` is the distance from the top of the rectangular cake to
the `ith` horizontal cut and similarly, `verticalCuts[j]` is
the distance from the left of the rectangular cake to the `jth` vertical
cut.

Return the maximum area of a piece of cake after you cut at each horizontal and
vertical position provided in the arrays `horizontalCuts` and `verticalCuts`. Since
the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

Example 2:

Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.

Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9

Constraints:

`2 <= h, w <= 10^9`

`1 <= horizontalCuts.length < min(h, 10^5)`

`1 <= verticalCuts.length < min(w, 10^5)`

`1 <= horizontalCuts[i] < h`

`1 <= verticalCuts[i] < w`

It is guaranteed that all elements in `horizontalCuts` are
distinct.

It is guaranteed that all elements in `verticalCuts` are
distinct.

【中文翻译】
给定一个高度为 `h`、宽度为 `w` 的矩形蛋糕，以及两个整数数组 `horizontalCuts` 和 `verticalCuts`，
其中 `horizontalCuts[i]` 是矩形蛋糕顶部到第 `i` 个水平切口的距离，
类似地，`verticalCuts[j]` 是矩形蛋糕左侧到第 `j` 个垂直切口的距离。

在数组 `horizontalCuts` 和 `verticalCuts` 中提供的每个水平和垂直位置进行切割后，
返回蛋糕的最大面积。由于答案可能是一个很大的数字，请将其对 10^9 + 7 取模后返回。

示例 1：

输入：h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
输出：4
解释：上图表示了给定的矩形蛋糕。红线是水平和垂直切割线。切割后，绿色的蛋糕块具有最大面积。

示例 2：

输入：h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
输出：6
解释：上图表示了给定的矩形蛋糕。红线是水平和垂直切割线。切割后，绿色和黄色的蛋糕块具有最大面积。

示例 3：

输入：h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
输出：9

约束条件：

`2 <= h, w <= 10^9`

`1 <= horizontalCuts.length < min(h, 10^5)`

`1 <= verticalCuts.length < min(w, 10^5)`

`1 <= horizontalCuts[i] < h`

`1 <= verticalCuts[i] < w`

保证 `horizontalCuts` 中的所有元素都是不同的。

保证 `verticalCuts` 中的所有元素都是不同的。
"""

from typing import List, Optional


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()

        max_h_gap = max(horizontalCuts[0] - 0, h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_h_gap = max(max_h_gap, horizontalCuts[i] - horizontalCuts[i - 1])

        max_v_gap = max(verticalCuts[0] - 0, w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_v_gap = max(max_v_gap, verticalCuts[i] - verticalCuts[i - 1])

        return (max_h_gap * max_v_gap) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 最大面积 = 最大的水平间隔 * 最大的垂直间隔。
# 分别对 horizontalCuts 和 verticalCuts 排序。
# 计算相邻切割之间的最大间隔（同时考虑边界：第一条切割到 0 的距离，以及 h/w 到最后一条切割的距离）。
# 最大高度间隔和最大宽度间隔相乘，并对 10^9+7 取模。
#
# 时间复杂度: O(N log N + M log M)  -- N 为水平切割数，M 为垂直切割数，排序占主导
# 空间复杂度: O(1)  -- 不计输入，排序可以原地进行
#
# 关键点:
# - 最大面积由各自方向的最大间隔决定，不需要排列组合所有矩形
# - 边界情况：从 0 到第一条切割、从最后一条切割到 h/w
# - 使用 (a * b) % MOD 防止整数溢出（Python 整数无溢出，但题目要求取模）









