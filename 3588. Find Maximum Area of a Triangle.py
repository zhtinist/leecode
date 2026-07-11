"""
LeetCode #3588 - Find Maximum Area of a Triangle
找到最大三角形面积
https://leetcode.cn/problems/find-maximum-area-of-a-triangle/

给你一个二维数组 `coords`，大小为 `n x 2`，表示一个无限笛卡尔平面上 `n` 个点的坐标。
找出一个 最大 三角形的 两倍 面积，其中三角形的三个顶点来自 `coords` 中的任意三个点，并且该三角形至少有一条边与 x 轴或 y 轴平行。严格地说，如果该三角形的最大面积为 `A`，则返回 `2 * A`。
如果不存在这样的三角形，返回 -1。
注意，三角形的面积 不能 为零。

示例 1：

输入： coords = [[1,1],[1,2],[3,2],[3,3]]
输出： 2
解释：

图中的三角形的底边为 1，高为 2。因此，它的面积为 `1/2 * 底边 * 高 = 1`。
示例 2：

输入： coords = [[1,1],[2,2],[3,3]]
输出： -1
解释：
唯一可能的三角形的顶点是 `(1, 1)`、`(2, 2)` 和 `(3, 3)`。它的任意边都不与 x 轴或 y 轴平行。

提示：
`1 <= n == coords.length <= 10^5`
`1 <= coords[i][0], coords[i][1] <= 10^6`
所有 `coords[i]` 都是 唯一 的。
"""

from typing import List, Optional


class Solution:
    def maxTriangleArea(self, coords: List[List[int]]) -> int:
        """Return 2 * max area of triangle with at least one side
        parallel to x-axis or y-axis, or -1 if none exists."""
        from collections import defaultdict

        # Group points by x-coordinate and y-coordinate
        by_x = defaultdict(list)  # x -> list of y values
        by_y = defaultdict(list)  # y -> list of x values

        for x, y in coords:
            by_x[x].append(y)
            by_y[y].append(x)

        # Sorted unique x and y values for computing max distance to DIFFERENT coordinate
        unique_x = sorted(by_x.keys())
        unique_y = sorted(by_y.keys())

        ans = -1

        # Case 1: side parallel to x-axis (two points share same y)
        for y, xs in by_y.items():
            if len(xs) < 2:
                continue
            base = max(xs) - min(xs)
            if base == 0:
                continue
            # Height: max vertical distance to a DIFFERENT y
            height = 0
            if unique_y[0] != y:
                height = max(height, y - unique_y[0])
            if unique_y[-1] != y:
                height = max(height, unique_y[-1] - y)
            if height <= 0:
                continue
            area2 = base * height
            if area2 > ans:
                ans = area2

        # Case 2: side parallel to y-axis (two points share same x)
        for x, ys in by_x.items():
            if len(ys) < 2:
                continue
            base = max(ys) - min(ys)
            if base == 0:
                continue
            # Height: max horizontal distance to a DIFFERENT x
            height = 0
            if unique_x[0] != x:
                height = max(height, x - unique_x[0])
            if unique_x[-1] != x:
                height = max(height, unique_x[-1] - x)
            if height <= 0:
                continue
            area2 = base * height
            if area2 > ans:
                ans = area2

        return ans











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Geometry, Array, Hash Table, Math, Enumeration
#
# 解题思路:
# 题目要求三角形的至少一条边与 x 轴或 y 轴平行（即水平或垂直），求最大面积的两倍。
#
# 情况1：底边平行于 x 轴（水平边）
#   - 两个顶点有相同的 y 坐标，底边长度 = |x1 - x2|
#   - 第三个顶点不能在相同的水平线上（否则面积为0）
#   - 高 = 第三个顶点的 y 坐标与底边 y 坐标之差的绝对值
#   - 对每个 y 坐标，底边取该 y 上 x 坐标的最大差值（最远两点），
#     高取该 y 到其他不同 y 坐标的最大距离
#
# 情况2：底边平行于 y 轴（垂直边）
#   - 类似的思路，按 x 坐标分组
#
# 最后取两种情况的最大值。如果没有任何有效三角形，返回 -1。
#
# 时间复杂度: O(N log N)，对坐标去重并排序（unique_x/unique_y），每个点恰好被处理一次
# 空间复杂度: O(N)，存储按 x 和 y 分组的哈希表
#
# 关键点:
# - 底边由共享同一个 x 或 y 的两个点构成，取该坐标上的最远两点得到最大底边长度
# - 高必须来自不同 x/y 的第三个点，否则三点共线面积为0
# - 返回 2 * 面积（整数），避免浮点数精度问题
