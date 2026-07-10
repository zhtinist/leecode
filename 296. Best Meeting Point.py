"""
LeetCode #296 - Best Meeting Point
中文题名：最佳碰面地点
https://leetcode.com/problems/best-meeting-point/

A group of two or more people wants to meet and minimize the total travel distance. You are
given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The
distance is calculated using Manhattan Distance, where distance(p1,
p2) = `|p2.x - p1.x| + |p2.y - p1.y|`.

Example:

Input:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6

Explanation: Given three people living at `(0,0)`, `(0,4)`, and `(2,2)`:
The point `(0,2)` is an ideal meeting point, as the total travel distance
of 2+2+2=6 is minimal. So return 6.

【中文翻译】
给定一组二维网格，网格中的值 0 或 1 表示，其中每个 1 标记了组内某个人的家。距离使用曼哈顿距离计算，即 distance(p1, p2) = `|p2.x - p1.x| + |p2.y - p1.y|`。

示例：

输入：

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

输出：6

解释：给定三个人分别住在 `(0,0)`、`(0,4)` 和 `(2,2)`：
点 `(0,2)` 是理想的碰面地点，因为总旅行距离 2+2+2=6 最小。所以返回 6。
"""

from typing import List, Optional


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """Find the minimal total Manhattan distance to a meeting point.

        Key insight: The optimal meeting point in Manhattan distance is the
        MEDIAN of all points in each dimension independently.
        The problem decomposes into two 1D problems: find median of rows and cols.
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        rows = []
        cols = []

        # Collect all home coordinates
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        # rows is already sorted (we iterate row by row)
        # Sort cols
        cols.sort()

        # Find median
        median_row = rows[len(rows) // 2]
        median_col = cols[len(cols) // 2]

        # Calculate total distance
        total_dist = 0
        for r in rows:
            total_dist += abs(r - median_row)
        for c in cols:
            total_dist += abs(c - median_col)

        return total_dist


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: Yes
#
# 解题思路:
# 曼哈顿距离的二维问题可以分解为两个独立的一维问题。最佳会面点的坐标是
# 所有家的行坐标的中位数和列坐标的中位数（中位数使绝对距离和最小）。
# 1. 收集所有家的行坐标和列坐标
# 2. 行坐标已按遍历顺序排好，列坐标需要排序
# 3. 取中位数作为最佳会面点
# 4. 计算所有家到该点的曼哈顿距离之和
#
# 证明：对于一维绝对距离和 ∑|x - a_i|，当 x 为中位数时取得最小值。
# 曼哈顿距离 |x1-x2| + |y1-y2| 可以分解：min ∑(|r_i - r_med| + |c_i - c_med|)
# = min ∑|r_i - r_med| + min ∑|c_i - c_med|
#
# 时间复杂度: O(MN + K log K) 或 O(MN) - K 为家的数量，收集坐标 O(MN)
#   利用 rows 天然有序可以用快速选择 O(K)
# 空间复杂度: O(K) - 存储所有家的坐标
#
# 关键点:
# - 曼哈顿距离可分解为行和列的独立问题
# - 中位数使绝对距离和最小（不是平均值！）
# - rows 天然有序（按行遍历），不需要额外排序
# - 等价于两个一维的 Best Meeting Point 问题
