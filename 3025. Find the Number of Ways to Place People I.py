"""
LeetCode #3025 - Find the Number of Ways to Place People I
人员站位的方案数 I
https://leetcode.cn/problems/find-the-number-of-ways-to-place-people-i/

给你一个  `n x 2` 的二维数组 `points` ，它表示二维平面上的一些点坐标，其中 `points[i] = [x_i, y_i]` 。

计算点对 `(A, B)` 的数量，其中
`A` 在 `B` 的左上角，并且
它们形成的长方形中（或直线上）没有其它点（包括边界），除了点 `A` 和点 `B`。
返回数量。

示例 1：

输入：points = [[1,1],[2,2],[3,3]]
输出：0
解释：

没有办法选择 `A` 和 `B`，使得 `A` 在 `B` 的左上角。
示例 2：

输入：points = [[6,2],[4,4],[2,6]]
输出：2
解释：

左边的是点对 `(points[1], points[0])`，其中 `points[1]` 在 `points[0]` 的左上角，并且形成的长方形内部是空的。
中间的是点对 `(points[2], points[1])`，和左边的一样是合法的点对。
右边的是点对 `(points[2], points[0])`，其中 `points[2]` 在 `points[0]` 的左上角，但 `points[1]` 在长方形内部，所以不是一个合法的点对。
示例 3：

输入：points = [[3,1],[1,3],[1,1]]
输出：2
解释：

左边的是点对 `(points[2], points[0])`，其中 `points[2]` 在 `points[0]` 的左上角并且在它们形成的直线上没有其它点。注意两个点形成一条线的情况是合法的。
中间的是点对 `(points[1], points[2])`，和左边一样也是合法的点对。
右边的是点对 `(points[1], points[0])`，它不是合法的点对，因为 `points[2]` 在长方形的边上。

提示：
`2 <= n <= 50`
`points[i].length == 2`
`0 <= points[i][0], points[i][1] <= 50`
`points[i]` 点对两两不同。
"""

from typing import List, Optional


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        A is top-left of B if A.x <= B.x and A.y >= B.y.
        Count pairs where the rectangle (including boundary) between
        A and B contains no other points.
        n <= 50, so O(n^3) is fine.
        """
        n = len(points)
        ans = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                ax, ay = points[i]
                bx, by = points[j]

                # A must be top-left of B: A.x <= B.x and A.y >= B.y
                if not (ax <= bx and ay >= by):
                    continue

                # Check if any other point is inside the rectangle
                ok = True
                for k in range(n):
                    if k == i or k == j:
                        continue
                    kx, ky = points[k]
                    # Inside or on boundary of rectangle
                    if ax <= kx <= bx and by <= ky <= ay:
                        ok = False
                        break

                if ok:
                    ans += 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Geometry, Array, Math, Enumeration, Sorting
#
# 解题思路:
# n <= 50，直接三重循环枚举。A 在 B 的左上角定义为 A.x <= B.x 且 A.y >= B.y。
# 对每对 (A, B)，检查是否有其他点位于矩形 [A.x, B.x] × [B.y, A.y] 的内部或边界上。
# 矩形为空（包括只有 A 和 B）才算合法。
#
# 时间复杂度: O(n^3)，n <= 50
# 空间复杂度: O(1)
#
# 关键点:
# - 矩形边界上的点也算作"内部"，不能有第三个点
# - A 和 B 在同一条水平线或垂直线上也是合法的（矩形退化为线段）
# - A.x <= B.x 且 A.y >= B.y 定义左上角关系（坐标系中 y 向上）
