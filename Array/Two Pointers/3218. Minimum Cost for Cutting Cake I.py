"""
LeetCode #3218 - Minimum Cost for Cutting Cake I
切蛋糕的最小总开销 I
https://leetcode.cn/problems/minimum-cost-for-cutting-cake-i/

有一个 `m x n` 大小的矩形蛋糕，需要切成 `1 x 1` 的小块。
给你整数 `m` ，`n` 和两个数组：
`horizontalCut` 的大小为 `m - 1` ，其中 `horizontalCut[i]` 表示沿着水平线 `i` 切蛋糕的开销。
`verticalCut` 的大小为 `n - 1` ，其中 `verticalCut[j]` 表示沿着垂直线 `j` 切蛋糕的开销。
一次操作中，你可以选择任意不是 `1 x 1` 大小的矩形蛋糕并执行以下操作之一：
沿着水平线 `i` 切开蛋糕，开销为 `horizontalCut[i]` 。
沿着垂直线 `j` 切开蛋糕，开销为 `verticalCut[j]` 。
每次操作后，这块蛋糕都被切成两个独立的小蛋糕。
每次操作的开销都为最开始对应切割线的开销，并且不会改变。
请你返回将蛋糕全部切成 `1 x 1` 的蛋糕块的 最小 总开销。

示例 1：

输入：m = 3, n = 2, horizontalCut = [1,3], verticalCut = [5]
输出：13
解释：

沿着垂直线 0 切开蛋糕，开销为 5 。
沿着水平线 0 切开 `3 x 1` 的蛋糕块，开销为 1 。
沿着水平线 0 切开 `3 x 1` 的蛋糕块，开销为 1 。
沿着水平线 1 切开 `2 x 1` 的蛋糕块，开销为 3 。
沿着水平线 1 切开 `2 x 1` 的蛋糕块，开销为 3 。
总开销为 `5 + 1 + 1 + 3 + 3 = 13` 。
示例 2：

输入：m = 2, n = 2, horizontalCut = [7], verticalCut = [4]
输出：15
解释：
沿着水平线 0 切开蛋糕，开销为 7 。
沿着垂直线 0 切开 `1 x 2` 的蛋糕块，开销为 4 。
沿着垂直线 0 切开 `1 x 2` 的蛋糕块，开销为 4 。
总开销为 `7 + 4 + 4 = 15` 。

提示：
`1 <= m, n <= 20`
`horizontalCut.length == m - 1`
`verticalCut.length == n - 1`
`1 <= horizontalCut[i], verticalCut[i] <= 10^3`
"""

from typing import List, Optional


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        h = v = 0  # 指针
        h_pieces = v_pieces = 1  # 当前水平/垂直块数
        cost = 0
        while h < len(horizontalCut) and v < len(verticalCut):
            if horizontalCut[h] >= verticalCut[v]:
                cost += horizontalCut[h] * v_pieces
                h_pieces += 1
                h += 1
            else:
                cost += verticalCut[v] * h_pieces
                v_pieces += 1
                v += 1
        while h < len(horizontalCut):
            cost += horizontalCut[h] * v_pieces
            h += 1
        while v < len(verticalCut):
            cost += verticalCut[v] * h_pieces
            v += 1
        return cost










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Two Pointers, Dynamic Programming, Sorting
#
# 解题思路:
# 贪心策略：代价越大的切割应该越早进行（因为后续切割会产生更多块，每块都要切）。
# 排序 horizontalCut 和 verticalCut 降序。
# 维护 h_pieces（当前水平方向块数）和 v_pieces（当前垂直方向块数）。
# 每次选择代价最大的切割线：
# - 切水平线：代价 * 当前垂直块数（每块垂直条都需要切一次）
# - 切垂直线：代价 * 当前水平块数
# 切割后对应方向的块数 +1。
#
# 时间复杂度: O((m+n) log(m+n))
# 空间复杂度: O(1)
#
# 关键点:
# - 类似巧克力切割问题，高代价切割应优先执行
# - 每次水平切割影响所有垂直块（v_pieces 倍），反之亦然
