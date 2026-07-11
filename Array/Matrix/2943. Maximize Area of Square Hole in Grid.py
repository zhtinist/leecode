"""
LeetCode #2943 - Maximize Area of Square Hole in Grid
最大化网格图中正方形空洞的面积
https://leetcode.cn/problems/maximize-area-of-square-hole-in-grid/

给你两个整数 `n` 和 `m`，以及两个整数数组 `hBars` 和 `vBars`。网格由 `n + 2` 条水平线和 `m + 2` 条竖直线组成，形成 1x1 的单元格。网格中的线条从 `1` 开始编号。
你可以从 `hBars` 中 删除 一些水平线条，并从 `vBars` 中删除一些竖直线条。注意，其他线条是固定的，无法删除。
返回一个整数表示移除一些线条（可以不移除任何线条）后，网格中 正方形空洞的最大面积 。

示例 1：

输入: n = 2, m = 1, hBars = [2,3], vBars = [2]
输出: 4
解释:
左侧图片展示了网格的初始状态。水平线是 `[1,2,3,4]`，竖直线是 `[1,2,3]`。
构造最大正方形空洞的一种方法是移除水平线 2 和竖直线 2。
示例 2：

输入: n = 1, m = 1, hBars = [2], vBars = [2]
输出: 4
解释:
移除水平线 2 和竖直线 2，可以得到最大正方形空洞。
示例 3：

输入: n = 2, m = 3, hBars = [2,3], vBars = [2,4]
输出: 4
解释:
构造最大正方形空洞的一种方法是移除水平线 3 和竖直线 4。

提示：
`1 <= n <= 10^9`
`1 <= m <= 10^9`
`1 <= hBars.length <= 100`
`2 <= hBars[i] <= n + 1`
`1 <= vBars.length <= 100`
`2 <= vBars[i] <= m + 1`
`hBars` 中所有值互不相同。
`vBars` 中所有值互不相同。
"""

from typing import List, Optional


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int],
                                 vBars: List[int]) -> int:
        def max_consecutive(arr):
            arr.sort()
            best = 1
            cur = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cur += 1
                    best = max(best, cur)
                else:
                    cur = 1
            return best

        h_gap = max_consecutive(hBars) + 1 if hBars else 1
        v_gap = max_consecutive(vBars) + 1 if vBars else 1
        side = min(h_gap, v_gap)
        return side * side



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sorting
#
# 解题思路:
# 移除连续的水平线或竖直线可合并多个单元格形成空洞。正方形空洞的边长 = 水平方向最大连续空洞大小和垂直方向最大连续空洞大小的最小值。
# 对 hBars 和 vBars 分别排序，求最长连续递增子序列的长度，空洞大小 = 连续长度 + 1。
# 面积 = min(水平最大空洞, 垂直最大空洞)^2。
#
# 时间复杂度: O(H log H + V log V) 其中 H = len(hBars), V = len(vBars)
# 空间复杂度: O(1)
#
# 关键点:
# - 连续移除相邻线条才能扩大空洞（非连续的移除合并不了）
# - 寻找最长连续递增序列长度
# - 正方形边长受限于水平和垂直两个方向的较小值
