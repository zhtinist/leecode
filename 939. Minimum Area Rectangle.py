"""
LeetCode #939 - Minimum Area Rectangle
中文题名：最小面积矩形
https://leetcode.com/problems/minimum-area-rectangle/

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from
these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Note:

`1 <= points.length <= 500`

`0 <= points[i][0] <= 40000`

`0 <= points[i][1] <= 40000`

All points are distinct.

【中文翻译】
给定平面上一组点，确定由这些点形成的矩形的最小面积，
矩形的边平行于 x 轴和 y 轴。

如果不存在任何矩形，则返回 0。

"""

from typing import List, Optional


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple, points))
        min_area = float('inf')
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # Points must form a diagonal (different x and different y)
                if x1 != x2 and y1 != y2:
                    # Check if the other two corners exist
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        min_area = min(min_area, area)

        return 0 if min_area == float('inf') else min_area



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 构建点集：将所有点存入哈希集合，以便 O(1) 查询某个坐标是否存在。
# 2. 枚举对角线：遍历所有点对 (x1,y1), (x2,y2)，如果 x1 != x2 且 y1 != y2
#    （形成一个对角线的两端），则检查另外两个角 (x1,y2) 和 (x2,y1) 是否存在。
# 3. 计算面积：如果四个角都存在，则该矩形有效，计算面积并更新最小值。
# 4. 返回结果：如果未找到任何矩形则返回 0，否则返回最小面积。
#
# 时间复杂度: O(N^2) — 枚举所有点对，其中 N 是点的数量（最多 500）。
# 空间复杂度: O(N) — 存储点集的哈希表。
#
# 关键点:
# - 矩形的边平行于坐标轴，因此矩形由对角两点唯一确定
# - 使用哈希集 O(1) 查询另外两个角是否存在
# - 对角线必须满足 x1 != x2 且 y1 != y2（否则退化为线段）
