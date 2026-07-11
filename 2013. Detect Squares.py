"""
LeetCode #2013 - Detect Squares
检测正方形
https://leetcode.cn/problems/detect-squares/

给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：
添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。
给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。
轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。
实现 `DetectSquares` 类：
`DetectSquares()` 使用空数据结构初始化对象
`void add(int[] point)` 向数据结构添加一个新的点 `point = [x, y]`
`int count(int[] point)` 统计按上述方式与点 `point = [x, y]` 共同构造 轴对齐正方形 的方案数。

示例：
输入： ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"] [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]] 输出： [null, null, null, null, 1, 0, null, 2]  解释： DetectSquares detectSquares = new DetectSquares(); detectSquares.add([3, 10]); detectSquares.add([11, 2]); detectSquares.add([3, 2]); detectSquares.count([11, 10]); // 返回 1 。你可以选择：                                //   - 第一个，第二个，和第三个点 detectSquares.count([14, 8]);  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。 detectSquares.add([11, 2]);    // 允许添加重复的点。 detectSquares.count([11, 10]); // 返回 2 。你可以选择：                                //   - 第一个，第二个，和第三个点                                //   - 第一个，第三个，和第四个点

提示：
`point.length == 2`
`0 <= x, y <= 1000`
调用 `add` 和 `count` 的 总次数 最多为 `5000`
"""

from typing import List, Optional


class DetectSquares:
    def __init__(self):
        """
        Store point counts: count[(x, y)] = frequency of that point.
        """
        from collections import defaultdict
        self.points_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points_count[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        """
        For the query point (qx, qy), find another point (x, y) with same x
        (vertical alignment), compute side length = |qy - y|, then check
        the other two corners of the axis-aligned square.
        """
        qx, qy = point
        ans = 0

        for (x, y), freq in self.points_count.items():
            # Must share x-coordinate and have different y (positive area)
            if x != qx or y == qy:
                continue

            side = abs(qy - y)

            # Two possible squares: to the right or left of the query point
            # Corner 1: (qx + side, qy), (qx + side, y)
            ans += (
                freq
                * self.points_count[(qx + side, qy)]
                * self.points_count[(qx + side, y)]
            )
            # Corner 2: (qx - side, qy), (qx - side, y)
            ans += (
                freq
                * self.points_count[(qx - side, qy)]
                * self.points_count[(qx - side, y)]
            )

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Array, Hash Table, Counting, Data Stream
#
# 解题思路:
# 使用哈希表存储每个点的出现次数。
# add: O(1) 添加点并增加计数。
# count: 枚举与查询点 (qx, qy) x 坐标相同的已有点 (x, y)（即垂直对齐）。
# 这样的点作为正方形的一条边。边长 side = |qy - y|。
# 正方形的另外两个角有两种可能：在右侧 (qx+side, qy) 和 (qx+side, y)，
# 或在左侧 (qx-side, qy) 和 (qx-side, y)。
# 每种情况下，方案数是三个点的频次乘积。累加所有可能。
#
# 时间复杂度: add O(1), count O(N) 其中 N 为已添加的不同点数 (最多 5000)
# 空间复杂度: O(N)
#
# 关键点:
# - 正方形轴对齐，所以需要垂直对齐的点作为边
# - 正方面积必须为正 (y != qy)
# - 两个方向（左和右）分别计算
