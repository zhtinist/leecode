"""
LeetCode #2250 - Count Number of Rectangles Containing Each Point
统计包含每个点的矩形数目
https://leetcode.cn/problems/count-number-of-rectangles-containing-each-point/

给你一个二维整数数组 `rectangles` ，其中 `rectangles[i] = [l_i, h_i]` 表示第 `i` 个矩形长为 `l_i` 高为 `h_i` 。给你一个二维整数数组 `points` ，其中 `points[j] = [x_j, y_j]` 是坐标为 `(x_j, y_j)` 的一个点。
第 `i` 个矩形的 左下角 在 `(0, 0)` 处，右上角 在 `(l_i, h_i)` 。
请你返回一个整数数组 `count` ，长度为 `points.length`，其中 `count[j]`是 包含 第 `j` 个点的矩形数目。
如果 `0 <= x_j <= l_i` 且 `0 <= y_j <= h_i` ，那么我们说第 `i` 个矩形包含第 `j` 个点。如果一个点刚好在矩形的 边上 ，这个点也被视为被矩形包含。

示例 1：

输入：rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]] 输出：[2,1] 解释： 第一个矩形不包含任何点。 第二个矩形只包含一个点 (2, 1) 。 第三个矩形包含点 (2, 1) 和 (1, 4) 。 包含点 (2, 1) 的矩形数目为 2 。 包含点 (1, 4) 的矩形数目为 1 。 所以，我们返回 [2, 1] 。
示例 2：

输入：rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]] 输出：[1,3] 解释： 第一个矩形只包含点 (1, 1) 。 第二个矩形只包含点 (1, 1) 。 第三个矩形包含点 (1, 3) 和 (1, 1) 。 包含点 (1, 3) 的矩形数目为 1 。 包含点 (1, 1) 的矩形数目为 3 。 所以，我们返回 [1, 3] 。

提示：
`1 <= rectangles.length, points.length <= 5 * 10^4`
`rectangles[i].length == points[j].length == 2`
`1 <= l_i, x_j <= 10^9`
`1 <= h_i, y_j <= 100`
所有 `rectangles` 互不相同 。
所有 `points` 互不相同 。
"""

from typing import List, Optional


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # Sort rectangles by length descending
        rectangles.sort(key=lambda r: -r[0])

        # Pair each point with its original index, then sort by x descending
        n = len(points)
        sorted_points = sorted(
            [(x, y, i) for i, (x, y) in enumerate(points)],
            key=lambda p: -p[0]
        )

        ans = [0] * n
        height_freq = [0] * 101  # frequency of each height among rectangles with l >= current x
        ri = 0  # pointer for rectangles

        for x, y, idx in sorted_points:
            # Add all rectangles whose length >= current point's x
            while ri < len(rectangles) and rectangles[ri][0] >= x:
                h = rectangles[ri][1]
                height_freq[h] += 1
                ri += 1

            # Count rectangles with height >= y among those already added
            cnt = 0
            for h in range(y, 101):
                cnt += height_freq[h]
            ans[idx] = cnt

        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Binary Indexed Tree, Array, Hash Table, Binary Search, Sorting
#
# 解题思路:
# 矩形的高 h_i 范围很小（1 到 100），这是解题的关键突破口。
# 使用离线处理 + 双指针技巧避免对每个点重复扫描所有矩形。
#
# 算法：
# 1. 按长度 l 降序排列所有矩形。
# 2. 按 x 坐标降序排列所有查询点（保留原始下标）。
# 3. 维护一个高度频率数组 height_freq[101]，表示"当前已处理的矩形中"
#    各高度的出现次数。
# 4. 双指针遍历：对于每个查询点 (x, y)，将所有满足 l >= x 的矩形加入
#    height_freq（这些矩形的长度条件已满足），只需统计其中 h >= y 的数量。
# 5. 由于高度范围只有 101，遍历 height_freq 的 [y..100] 区间累加即可。
#
# 时间复杂度: O(N*logN + M*logM + N + M*100)
#   其中 N=矩形数, M=点数, 100 为高度范围（常数）
# 空间复杂度: O(N + M) — 排序存储 + 高度频率数组(101)
#
# 关键点:
# - 高度 ≤ 100 使得 O(100) 遍历高度维可行
# - 离线处理：将矩形和点都按 x 降序排列，双指针一次扫描
# - 矩形左下角在 (0,0)，所以只需检查 l >= x 且 h >= y
# - 高度频率数组替代二分查找，避免每次查询的 O(log N) 开销
