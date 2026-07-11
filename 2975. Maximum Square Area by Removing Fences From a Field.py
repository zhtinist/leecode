"""
LeetCode #2975 - Maximum Square Area by Removing Fences From a Field
移除栅栏得到的正方形田地的最大面积
https://leetcode.cn/problems/maximum-square-area-by-removing-fences-from-a-field/

有一个大型的 `(m - 1) x (n - 1)` 矩形田地，其两个对角分别是 `(1, 1)` 和 `(m, n)` ，田地内部有一些水平栅栏和垂直栅栏，分别由数组 `hFences` 和 `vFences` 给出。
水平栅栏为坐标 `(hFences[i], 1)` 到 `(hFences[i], n)`，垂直栅栏为坐标 `(1, vFences[i])` 到 `(m, vFences[i])` 。
返回通过 移除 一些栅栏（可能不移除）所能形成的最大面积的 正方形 田地的面积，或者如果无法形成正方形田地则返回 `-1`。
由于答案可能很大，所以请返回结果对 `10^9 + 7` 取余 后的值。
注意：田地外围两个水平栅栏（坐标 `(1, 1)` 到 `(1, n)` 和坐标 `(m, 1)` 到 `(m, n)` ）以及两个垂直栅栏（坐标 `(1, 1)` 到 `(m, 1)` 和坐标 `(1, n)` 到 `(m, n)` ）所包围。这些栅栏 不能 被移除。

示例 1：

输入：m = 4, n = 3, hFences = [2,3], vFences = [2] 输出：4 解释：移除位于 2 的水平栅栏和位于 2 的垂直栅栏将得到一个面积为 4 的正方形田地。
示例 2：

输入：m = 6, n = 7, hFences = [2], vFences = [4] 输出：-1 解释：可以证明无法通过移除栅栏形成正方形田地。

提示：
`3 <= m, n <= 10^9`
`1 <= hFences.length, vFences.length <= 600`
`1 < hFences[i] < m`
`1 < vFences[i] < n`
`hFences` 和 `vFences` 中的元素是唯一的。
"""

from typing import List, Optional


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        """
        Collect all possible horizontal and vertical gaps (including boundaries),
        find the maximum common gap length g, then area = g * g.
        """
        MOD = 10**9 + 7

        # Add boundaries
        h_all = [1] + sorted(hFences) + [m]
        v_all = [1] + sorted(vFences) + [n]

        # Generate all possible gap lengths
        h_gaps = set()
        for i in range(len(h_all)):
            for j in range(i + 1, len(h_all)):
                h_gaps.add(h_all[j] - h_all[i])

        v_gaps = set()
        for i in range(len(v_all)):
            for j in range(i + 1, len(v_all)):
                v_gaps.add(v_all[j] - v_all[i])

        # Find max common gap
        max_side = 0
        for gap in h_gaps:
            if gap in v_gaps:
                max_side = max(max_side, gap)

        if max_side == 0:
            return -1

        return (max_side * max_side) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Enumeration
#
# 解题思路:
# 要形成正方形，需要水平方向和垂直方向有相同长度的间隔（边长）。
# 首先将边界（1 和 m, 1 和 n）加入栅栏集合，然后枚举所有可能的水平间隔长度和垂直间隔长度。
# 找到两者共有的最大间隔长度 g，面积即为 g^2 对 10^9+7 取模。
#
# 时间复杂度: O(H^2 + V^2)，其中 H=hFences长度+2，V=vFences长度+2，最多约600
# 空间复杂度: O(H^2 + V^2)，存储所有可能的间隔长度
#
# 关键点:
# - 边界栅栏不可移除，必须计入
# - 正方形要求水平间隔 = 垂直间隔 = 边长
# - 数据范围小（<=600），O(n^2) 枚举可行
