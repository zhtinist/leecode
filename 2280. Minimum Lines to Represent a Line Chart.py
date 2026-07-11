"""
LeetCode #2280 - Minimum Lines to Represent a Line Chart
表示一个折线图的最少线段数
https://leetcode.cn/problems/minimum-lines-to-represent-a-line-chart/

给你一个二维整数数组 `stockPrices` ，其中 `stockPrices[i] = [day_i, price_i]` 表示股票在 `day_i` 的价格为 `price_i` 。折线图 是一个二维平面上的若干个点组成的图，横坐标表示日期，纵坐标表示价格，折线图由相邻的点连接而成。比方说下图是一个例子：
请你返回要表示一个折线图所需要的 最少线段数 。

示例 1：

输入：stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]] 输出：3 解释： 上图为输入对应的图，横坐标表示日期，纵坐标表示价格。 以下 3 个线段可以表示折线图： - 线段 1 （红色）从 (1,7) 到 (4,4) ，经过 (1,7) ，(2,6) ，(3,5) 和 (4,4) 。 - 线段 2 （蓝色）从 (4,4) 到 (5,4) 。 - 线段 3 （绿色）从 (5,4) 到 (8,1) ，经过 (5,4) ，(6,3) ，(7,2) 和 (8,1) 。 可以证明，无法用少于 3 条线段表示这个折线图。
示例 2：

输入：stockPrices = [[3,4],[1,2],[7,8],[2,3]] 输出：1 解释： 如上图所示，折线图可以用一条线段表示。

提示：
`1 <= stockPrices.length <= 10^5`
`stockPrices[i].length == 2`
`1 <= day_i, price_i <= 10^9`
所有 `day_i` 互不相同 。
"""

from typing import List, Optional


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        """
        Return the minimum number of line segments to represent the line chart.

        Key insight: Three points are collinear if the slopes between consecutive
        pairs are equal. To avoid floating-point precision issues, compare using
        cross-multiplication:
            (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
        """
        n = len(stockPrices)
        if n <= 2:
            return n - 1  # 0 or 1 line needed

        stockPrices.sort(key=lambda x: x[0])

        lines = 1  # at least one line segment
        for i in range(2, n):
            x1, y1 = stockPrices[i - 2]
            x2, y2 = stockPrices[i - 1]
            x3, y3 = stockPrices[i]

            # Check if slopes are equal: (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)
            # Cross-multiply to avoid division and floating-point issues
            dy1 = y2 - y1
            dx1 = x2 - x1
            dy2 = y3 - y2
            dx2 = x3 - x2

            if dy1 * dx2 != dy2 * dx1:
                lines += 1

        return lines


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Geometry, Array, Math, Number Theory, Sorting
#
# 解题思路:
# 最少线段数等于"方向发生变化的次数 + 1"。三个连续的点在同一条直线上当且仅当
# 连接相邻点的两条线段斜率相等：(y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)。
# 为避免浮点数精度问题，使用叉乘比较：dy1 * dx2 == dy2 * dx1。
# 首先按日期（横坐标）排序所有点，然后遍历每三个连续点，检查它们是否共线。
# 如果不共线（斜率改变），则需要一条新线段，lines 加一。
#
# 时间复杂度: O(N log N)，N 为 stockPrices 长度。排序 O(N log N)，
# 遍历 O(N)。
# 空间复杂度: O(1)，仅使用常数额外空间（排序可能使用 O(log N) 递归栈空间）。
#
# 关键点:
# - 三个连续点是否共线：用叉乘比较斜率，避免浮点数除法精度问题
# - 先按横坐标排序，因为点不一定按日期顺序给出
# - n <= 2 时的边界情况：0 个点需要 0 条线，1 个点需要 0 条线，2 个点需要 1 条线
# - 初始 lines = 1：至少需要一条线段连接所有点
# - 每次检测到斜率改变时 lines 加一
