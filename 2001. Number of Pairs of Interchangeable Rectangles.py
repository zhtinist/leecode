"""
LeetCode #2001 - Number of Pairs of Interchangeable Rectangles
可互换矩形的组数
https://leetcode.cn/problems/number-of-pairs-of-interchangeable-rectangles/

用一个下标从 0 开始的二维整数数组 `rectangles` 来表示 `n` 个矩形，其中 `rectangles[i] = [width_i, height_i]` 表示第 `i` 个矩形的宽度和高度。
如果两个矩形 `i` 和 `j`（`i < j`）的宽高比相同，则认为这两个矩形 可互换 。更规范的说法是，两个矩形满足 `width_i/height_i == width_j/height_j`（使用实数除法而非整数除法），则认为这两个矩形 可互换 。
计算并返回 `rectangles` 中有多少对 可互换 矩形。

示例 1：
输入：rectangles = [[4,8],[3,6],[10,20],[15,30]] 输出：6 解释：下面按下标（从 0 开始）列出可互换矩形的配对情况： - 矩形 0 和矩形 1 ：4/8 == 3/6 - 矩形 0 和矩形 2 ：4/8 == 10/20 - 矩形 0 和矩形 3 ：4/8 == 15/30 - 矩形 1 和矩形 2 ：3/6 == 10/20 - 矩形 1 和矩形 3 ：3/6 == 15/30 - 矩形 2 和矩形 3 ：10/20 == 15/30
示例 2：
输入：rectangles = [[4,5],[7,8]] 输出：0 解释：不存在成对的可互换矩形。

提示：
`n == rectangles.length`
`1 <= n <= 10^5`
`rectangles[i].length == 2`
`1 <= width_i, height_i <= 10^5`
"""

from typing import List, Optional


class Solution:
    def interchangeableRectangles(
        self, rectangles: List[List[int]]
    ) -> int:
        """
        Count pairs with same width/height ratio.
        Use reduced fraction (w//gcd, h//gcd) as key to avoid float issues.
        For a ratio with count c, number of pairs = c * (c - 1) // 2.
        """
        from collections import defaultdict
        import math

        ratio_count = defaultdict(int)

        for w, h in rectangles:
            g = math.gcd(w, h)
            ratio = (w // g, h // g)
            ratio_count[ratio] += 1

        ans = 0
        for c in ratio_count.values():
            ans += c * (c - 1) // 2

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Math, Counting, Number Theory
#
# 解题思路:
# 统计每个宽高比的矩形数量。使用约分后的分数 (w/gcd, h/gcd) 作为键，
# 避免浮点数精度问题。对于每个比例有 c 个矩形，从中任选 2 个组成一对，
# 组合数为 C(c, 2) = c*(c-1)/2。累加所有比例的组合数即为答案。
#
# 时间复杂度: O(N * log M)，N 为矩形数，log M 为 GCD 计算
# 空间复杂度: O(N)，哈希表存储
#
# 关键点:
# - 用最简分数作为键，避免浮点误差
# - 使用 math.gcd 约分
# - 组合数公式: c*(c-1)//2
