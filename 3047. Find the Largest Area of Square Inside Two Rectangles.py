"""
LeetCode #3047 - Find the Largest Area of Square Inside Two Rectangles
求交集区域内的最大正方形面积
https://leetcode.cn/problems/find-the-largest-area-of-square-inside-two-rectangles/

在二维平面上存在 `n` 个矩形。给你两个下标从 0 开始的二维整数数组 `bottomLeft` 和 `topRight`，两个数组的大小都是 `n x 2` ，其中 `bottomLeft[i]` 和 `topRight[i]` 分别代表第 `i` 个矩形的 左下角 和 右上角 坐标。
我们定义 向右 的方向为 x 轴正半轴（x 坐标增加），向左 的方向为 x 轴负半轴（x 坐标减少）。同样地，定义 向上 的方向为 y 轴正半轴（y 坐标增加），向下 的方向为 y 轴负半轴（y 坐标减少）。
你可以选择一个区域，该区域由两个矩形的 交集 形成。你需要找出能够放入该区域 内 的 最大 正方形面积，并选择最优解。
返回能够放入交集区域的正方形的 最大 可能面积，如果矩形之间不存在任何交集区域，则返回 `0`。

示例 1：
输入：bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]] 输出：1 解释：边长为 1 的正方形可以放入矩形 0 和矩形 1 的交集区域，或矩形 1 和矩形 2 的交集区域。因此最大面积是边长 * 边长，即 1 * 1 = 1。 可以证明，边长更大的正方形无法放入任何交集区域。
示例 2：
输入：bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]] 输出：1 解释：边长为 1 的正方形可以放入矩形 0 和矩形 1，矩形 1 和矩形 2，或所有三个矩形的交集区域。因此最大面积是边长 * 边长，即 1 * 1 = 1。 可以证明，边长更大的正方形无法放入任何交集区域。 请注意，区域可以由多于两个矩形的交集构成。
示例 3：
输入：bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]] 输出：0 解释：不存在相交的矩形，因此，返回 0 。

提示：
`n == bottomLeft.length == topRight.length`
`2 <= n <= 10^3`
`bottomLeft[i].length == topRight[i].length == 2`
`1 <= bottomLeft[i][0], bottomLeft[i][1] <= 10^7`
`1 <= topRight[i][0], topRight[i][1] <= 10^7`
`bottomLeft[i][0] < topRight[i][0]`
`bottomLeft[i][1] < topRight[i][1]`
"""

from typing import List, Optional


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        """
        For each pair of rectangles, compute their intersection.
        The largest square that fits has side = min(width, height) of intersection.
        Return max(side^2) over all pairs.
        """
        n = len(bottomLeft)
        ans = 0

        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]
            for j in range(i + 1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                # Intersection
                left = max(x1, x3)
                right = min(x2, x4)
                bottom = max(y1, y3)
                top = min(y2, y4)

                if left < right and bottom < top:
                    side = min(right - left, top - bottom)
                    ans = max(ans, side * side)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Geometry, Array, Math
#
# 解题思路:
# 枚举所有矩形对，计算其交集区域。两个矩形的交集仍是矩形，坐标为：
# 左边界取两矩形左边界的最大值，右边界取右边界的最大值，上下边界同理。
# 交集矩形的最大内接正方形边长为 min(宽度, 高度)，面积即边长的平方。取所有对的最大值。
#
# 时间复杂度: O(n^2)，n <= 1000，最多约 50 万对
# 空间复杂度: O(1)
#
# 关键点:
# - 交集矩形：left=max(x1,x3), right=min(x2,x4), bottom=max(y1,y3), top=min(y2,y4)
# - 正方形边长受限于交集的较短边
# - 交集有效条件：left < right 且 bottom < top
