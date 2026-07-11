"""
LeetCode #3623 - Count Number of Trapezoids I
统计梯形的数目 I
https://leetcode.cn/problems/count-number-of-trapezoids-i/

给你一个二维整数数组 `points`，其中 `points[i] = [x_i, y_i]` 表示第 `i` 个点在笛卡尔平面上的坐标。
水平梯形 是一种凸四边形，具有 至少一对 水平边（即平行于 x 轴的边）。两条直线平行当且仅当它们的斜率相同。
返回可以从 `points` 中任意选择四个不同点组成的 水平梯形 数量。
由于答案可能非常大，请返回结果对 `10^9 + 7` 取余数后的值。

示例 1：

输入： points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
输出： 3
解释：

有三种不同方式选择四个点组成一个水平梯形：
使用点 `[1,0]`、`[2,0]`、`[3,2]` 和 `[2,2]`。
使用点 `[2,0]`、`[3,0]`、`[3,2]` 和 `[2,2]`。
使用点 `[1,0]`、`[3,0]`、`[3,2]` 和 `[2,2]`。
示例 2：

输入： points = [[0,0],[1,0],[0,1],[2,1]]
输出： 1
解释：

只有一种方式可以组成一个水平梯形。

提示：
`4 <= points.length <= 10^5`
`–10^8 <= x_i, y_i <= 10^8`
所有点两两不同。
"""

from typing import List, Optional


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import Counter

        MOD = 10 ** 9 + 7

        # Count points at each y-coordinate
        y_counts = Counter(y for x, y in points)

        # For each y-level with cnt points, there are C(cnt, 2) ways
        # to choose 2 points as one horizontal base
        total = 0  # sum of C(cnt, 2) over all y
        sum_sq = 0  # sum of [C(cnt, 2)]^2 over all y

        for cnt in y_counts.values():
            c2 = cnt * (cnt - 1) // 2  # C(cnt, 2)
            total = (total + c2) % MOD
            sum_sq = (sum_sq + c2 * c2) % MOD

        # For each pair of distinct y-levels, the number of trapezoids
        # is C(cnt1, 2) * C(cnt2, 2)
        # Sum over all y1 != y2: (total^2 - sum_sq) / 2
        result = (total * total - sum_sq) % MOD
        result = result * pow(2, MOD - 2, MOD) % MOD  # divide by 2

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Geometry, Array, Hash Table, Math
#
# 解题思路:
# 水平梯形的定义：凸四边形中有一对平行且水平的边。这意味着在两个不同的 y 坐标上
# 各有一对点组成两条水平线段（梯形的上底和下底）。
#
# 因此，问题转化为：
# 1. 按 y 坐标将所有点分组
# 2. 对于 y 坐标 yi 有 cnt 个点，从中选 2 个作为一条水平边，共有 C(cnt, 2) 种选法
# 3. 选择两个不同的 y 坐标 y1 和 y2，从上选 2 点、从下选 2 点，组成一个梯形
#    数量为 C(cnt1, 2) * C(cnt2, 2)
# 4. 所有 y1 < y2 的组合求和
#
# 优化计算：令 a_i = C(cnt_i, 2)
# sum_{i<j} a_i * a_j = ((sum a_i)^2 - sum a_i^2) / 2
# 使用模逆除以 2 在模 MOD 下实现。
#
# 时间复杂度: O(N) — N 为点的数量，仅需一次遍历统计和两次聚合计算
# 空间复杂度: O(N) — Counter 存储不同 y 坐标的计数, 最坏 O(N)
#
# 关键点:
# - 识别梯形仅由两组水平点对定义（每对位于同一 y 坐标）
# - 组合计数 C(cnt, 2) = cnt * (cnt - 1) / 2
# - 用平方和公式避免 O(K^2) 的两两配对计算
# - 模除法：用费马小定理乘以 2^(MOD-2) 实现除以 2
