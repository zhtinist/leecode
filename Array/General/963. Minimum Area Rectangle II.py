"""
LeetCode #963 - Minimum Area Rectangle II
中文题名：最小面积矩形 II
https://leetcode.com/problems/minimum-area-rectangle-ii/

Given a set of points in the xy-plane, determine the minimum area of any
rectangle formed from these points, with sides not necessarily parallel to
the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

Example 2:

Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.

Example 3:

Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.

Example 4:

Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.

【中文翻译】
给定 xy 平面上的一组点，确定由这些点组成的任意矩形的最小面积，
其中矩形的边不一定平行于 x 轴和 y 轴。
如果没有矩形则返回 0。

"""

from typing import List, Optional
from collections import defaultdict
import math


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        point_set = set(tuple(p) for p in points)
        min_area = float('inf')

        for i in range(n):
            p1 = points[i]
            for j in range(i + 1, n):
                p2 = points[j]
                for k in range(j + 1, n):
                    p3 = points[k]
                    # 检查 p1, p2, p3 是否构成直角（以 p1 为顶点）
                    # 向量 p1->p2 和 p1->p3 点积为 0
                    v1 = (p2[0] - p1[0], p2[1] - p1[1])
                    v2 = (p3[0] - p1[0], p3[1] - p1[1])

                    if v1[0] * v2[0] + v1[1] * v2[1] == 0:
                        # 第四个点 p4 = p2 + p3 - p1
                        p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
                        if p4 in point_set:
                            area = math.sqrt(v1[0]**2 + v1[1]**2) * math.sqrt(v2[0]**2 + v2[1]**2)
                            min_area = min(min_area, area)

        return min_area if min_area != float('inf') else 0.0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 枚举三个点，检查它们是否构成直角（点积为 0）。
# 如果 p1, p2, p3 构成直角（以 p1 为直角顶点），则第四个点可以通过向量加法得到：
# p4 = p2 + p3 - p1。
# 检查 p4 是否存在于点集中，若存在则构成矩形，计算面积。
# 矩形面积 = |p1->p2| * |p1->p3|（两直角边的乘积）。
# 需要考虑三种直角顶点的情况（p1, p2, p3 分别作为直角顶点），
# 但由于我们枚举了所有三个点的组合，每种直角情况都会被覆盖。
#
# 时间复杂度: O(N^3) — 三重循环枚举三个点
# 空间复杂度: O(N) — 点集哈希表
#
# 关键点:
# - 矩形的充要条件：三个点构成直角 + 第四点存在
# - 向量点积为零判断直角
# - 由三个点推算第四个点：p4 = p2 + p3 - p1（平行四边形对角线性质）
# - 面积等于两直角边长度的乘积
