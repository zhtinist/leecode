"""
LeetCode #3380 - Maximum Area Rectangle With Point Constraints I
用点构造面积最大的矩形 I
https://leetcode.cn/problems/maximum-area-rectangle-with-point-constraints-i/

给你一个数组 `points`，其中 `points[i] = [x_i, y_i]` 表示无限平面上一点的坐标。
你的任务是找出满足以下条件的矩形可能的 最大 面积：
矩形的四个顶点必须是数组中的 四个 点。
矩形的内部或边界上 不能 包含任何其他点。
矩形的边与坐标轴 平行 。
返回可以获得的 最大面积 ，如果无法形成这样的矩形，则返回 -1。

示例 1：

输入： points = [[1,1],[1,3],[3,1],[3,3]]
输出：4
解释：

我们可以用这 4 个点作为顶点构成一个矩形，并且矩形内部或边界上没有其他点。因此，最大面积为 4 。
示例 2：

输入： points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
输出：-1
解释：

唯一一组可能构成矩形的点为 `[1,1], [1,3], [3,1]` 和 `[3,3]`，但点 `[2,2]` 总是位于矩形内部。因此，返回 -1 。
示例 3：

输入： points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]
输出：2
解释：

点 `[1,3], [1,2], [3,2], [3,3]` 可以构成面积最大的矩形，面积为 2。此外，点 `[1,1], [1,2], [3,1], [3,2]` 也可以构成一个符合题目要求的矩形，面积相同。

提示：
`1 <= points.length <= 10`
`points[i].length == 2`
`0 <= x_i, y_i <= 100`
给定的所有点都是 唯一 的。
"""

from typing import List, Optional


class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        pt_set = set(tuple(p) for p in points)
        ans = -1

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x3, y3 = points[j]
                if x1 == x3 or y1 == y3:
                    continue
                x2, y2 = x3, y1
                x4, y4 = x1, y3
                if (x2, y2) not in pt_set or (x4, y4) not in pt_set:
                    continue
                x_min = min(x1, x3)
                x_max = max(x1, x3)
                y_min = min(y1, y3)
                y_max = max(y1, y3)
                valid = True
                for px, py in points:
                    if (px == x1 and py == y1) or (px == x2 and py == y2) or (px == x3 and py == y3) or (px == x4 and py == y4):
                        continue
                    if x_min <= px <= x_max and y_min <= py <= y_max:
                        valid = False
                        break
                if valid:
                    ans = max(ans, (x_max - x_min) * (y_max - y_min))
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Binary Indexed Tree, Segment Tree, Geometry, Array, Math, Enumeration, Sorting
#
# 解题思路:
# points数量<=10，直接枚举所有4个点的组合。对于每组4个点，检查是否构成轴对齐矩形
# （x坐标成对出现，y坐标成对出现），然后检查矩形内部和边界上没有其他点。
# 在所有合法矩形中取最大面积。
#
# 时间复杂度: O(C(n,4) * n)，n<=10
# 空间复杂度: O(1)
#
# 关键点:
# - 轴对齐矩形的四个顶点必须有两对相同的x坐标和两对相同的y坐标
# - 检查内部和边界上是否有其他点
