"""
LeetCode #593 - Valid Square
中文题名：有效的正方形
https://leetcode.com/problems/valid-square/

Given the coordinates of four points in 2D space, return whether the four points could
construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:

All the input integers are in the range [-10000, 10000].

A valid square has four equal sides with positive length and four equal angles
(90-degree angles).

Input points have no order.

【中文翻译】
给定二维空间中四个点的坐标，判断这四个点是否能构成一个正方形。

点的坐标 (x, y) 用一个包含两个整数的整数数组表示。

示例：
    输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    输出：True

注意：
    所有输入的整数在 [-10000, 10000] 范围内。
    一个有效的正方形有四条等长的正数边长和四个相等的角（90 度角）。
    输入的点没有顺序。
"""

from typing import List, Optional


class Solution:
    def validSquare(
        self,
        p1: List[int],
        p2: List[int],
        p3: List[int],
        p4: List[int],
    ) -> bool:
        """
        Compute all 6 pairwise squared distances.
        A valid square has 4 equal side lengths and 2 equal diagonal lengths,
        with side length > 0 and diagonal = 2 * side (by Pythagorean theorem
        applied to squared distances: diag^2 = 2 * side^2).
        """

        def dist_sq(a: List[int], b: List[int]) -> int:
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        points = [p1, p2, p3, p4]
        distances = []

        for i in range(4):
            for j in range(i + 1, 4):
                distances.append(dist_sq(points[i], points[j]))

        distances.sort()

        # The smallest 4 should be equal (sides), the largest 2 equal (diagonals)
        side = distances[0]
        diag = distances[-1]

        return (
            side > 0
            and distances[1] == side
            and distances[2] == side
            and distances[3] == side
            and distances[4] == diag
            and distances[5] == diag
            and diag == 2 * side
        )



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 计算四个点之间全部 6 条边的平方距离并排序。一个合法的正方形满足：4 条边（即排序后
# 的前 4 个距离）长度相等且大于 0；2 条对角线（即排序后的后 2 个距离）长度相等；
# 并且对角线平方 = 2 * 边长平方（勾股定理）。同时满足这些条件即可判定为正方形。
#
# 时间复杂度: O(1) — 只有 4 个点，6 条边，排序也是 O(1)
# 空间复杂度: O(1) — 存储 6 个距离
#
# 关键点:
# - 使用平方距离避免浮点数精度问题
# - 正方形判定条件：4 条边等长 + 2 条对角线等长 + 对角线的平方 = 2 * 边长平方
# - 边长必须大于 0（四个点不能重合）
