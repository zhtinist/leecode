"""
LeetCode #2249 - Count Lattice Points Inside a Circle
统计圆内格点数目
https://leetcode.cn/problems/count-lattice-points-inside-a-circle/

给你一个二维整数数组 `circles` ，其中 `circles[i] = [x_i, y_i, r_i]` 表示网格上圆心为 `(x_i, y_i)` 且半径为 `r_i` 的第 `i` 个圆，返回出现在 至少一个 圆内的 格点数目 。
注意：
格点 是指整数坐标对应的点。
圆周上的点 也被视为出现在圆内的点。

示例 1：

输入：circles = [[2,2,1]] 输出：5 解释： 给定的圆如上图所示。 出现在圆内的格点为 (1, 2)、(2, 1)、(2, 2)、(2, 3) 和 (3, 2)，在图中用绿色标识。 像 (1, 1) 和 (1, 3) 这样用红色标识的点，并未出现在圆内。 因此，出现在至少一个圆内的格点数目是 5 。
示例 2：

输入：circles = [[2,2,2],[3,4,1]] 输出：16 解释： 给定的圆如上图所示。 共有 16 个格点出现在至少一个圆内。 其中部分点的坐标是 (0, 2)、(2, 0)、(2, 4)、(3, 2) 和 (4, 4) 。

提示：
`1 <= circles.length <= 200`
`circles[i].length == 3`
`1 <= x_i, y_i <= 100`
`1 <= r_i <= min(x_i, y_i)`
"""

from typing import List, Optional


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()

        for x, y, r in circles:
            r2 = r * r
            # Iterate over the bounding square of the circle
            for i in range(x - r, x + r + 1):
                dx = i - x
                dx2 = dx * dx
                for j in range(y - r, y + r + 1):
                    dy = j - y
                    if dx2 + dy * dy <= r2:
                        points.add((i, j))

        return len(points)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Geometry, Array, Hash Table, Math, Enumeration
#
# 解题思路:
# 对于每个圆，枚举其外接正方形内的所有整数格点，检查是否在圆内（含边界）。
# 使用集合去重，确保每个格点只被计数一次。
#
# 由于圆的坐标范围很小（圆心 ≤ 100，半径 ≤ 100），每个圆的外接正方形最多
# 约 (2r+1)^2 ≤ 40401 个格点。200 个圆最多约 800 万次检查，完全可行。
#
# 判断点在圆内的条件：(x - xi)^2 + (y - yi)^2 <= ri^2
#
# 时间复杂度: O(C * R^2) — C 为圆的数量，R 为最大半径（100）
# 空间复杂度: O(P) — P 为所有圆覆盖的格点总数（去重后）
#
# 关键点:
# - 枚举每个圆的边界框内的所有整数点，而非整个坐标平面
# - 使用 set 自动去重，确保同一个格点不被重复计数
# - 圆周上的点也视为在圆内（用 <= 判断）
