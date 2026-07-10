"""
LeetCode #218 - The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/

A city's skyline is the outer contour of the silhouette formed by all the buildings in
that city when viewed from a distance. Now suppose you are given the locations and height
of all the buildings as shown on a cityscape photo (Figure A), write a program to
output the skyline formed by these buildings collectively (Figure B).

*   *

The geometric information of each building is represented by a triplet of integers `[Li,
Ri, Hi]`, where `Li` and `Ri` are the x coordinates of the left
and right edge of the ith building, respectively, and `Hi` is its height. It is
guaranteed that `0 <= Li, Ri <= INT_MAX`, `0 < Hi <= INT_MAX`,
and `Ri - Li > 0`. You may assume all buildings are perfect rectangles
grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: `[ [2 9 10],
[3 7 15], [5 12 12], [15 20 10], [19 24 8] ] `.

The output is a list of "key points" (red dots in Figure B) in the format of
`[ [x1,y1], [x2, y2], [x3, y3], ... ]` that uniquely defines a skyline. A key
point is the left endpoint of a horizontal line segment. Note that the last key
point, where the rightmost building ends, is merely used to mark the termination of the
skyline, and always has zero height. Also, the ground in between any two adjacent buildings
should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:`[ [2 10], [3 15], [7
12], [12 0], [15 10], [20 8], [24, 0] ]`.

Notes:

The number of buildings in any input list is guaranteed to be in the range `[0,
10000]`.

The input list is already sorted in ascending order by the left x position
`Li`.

The output list must be sorted by the x position.

There must be no consecutive horizontal lines of equal height in the output skyline. For
instance, `[...[2 3], [4 5], [7 5], [11 5], [12 7]...]` is not acceptable;
the three lines of height 5 should be merged into one in the final output as such:
`[...[2 3], [4 5], [12 7], ...]`
"""

from typing import List, Optional


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq

        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        result: List[List[int]] = []
        heap = [(0, float('inf'))]  # (negated height, right_x)

        for x, neg_h, r in events:
            if neg_h < 0:
                heapq.heappush(heap, (neg_h, r))

            while heap[0][1] <= x:
                heapq.heappop(heap)

            cur_height = -heap[0][0]
            if not result or result[-1][1] != cur_height:
                result.append([x, cur_height])

        return result












# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 扫描线(Line Sweep) + 最大堆(Max-Heap)方法。
# 1. 将每栋建筑拆解为两个事件点：左端点(开始，高度为负值)和右端点(结束，高度为 0)。
#    使用负高度确保开始事件在处理时的高楼优先，同时也方便最大堆操作。
# 2. 对事件按 x 坐标排序。
# 3. 维护一个最大堆，存储当前活跃建筑的 (负高度, 右边界)。堆顶即为当前最高建筑。
# 4. 遍历每个事件点：
#    - 遇到开始事件：将 (负高度, 右边界) 入堆。
#    - 惰性删除：若堆顶建筑的右边界 <= 当前 x 坐标，说明该建筑已结束，弹出堆顶。
#    - 获取当前最高高度，若与上一个关键点高度不同，则添加新关键点 [x, 当前最高]。
#
# 时间复杂度: O(n log n) - 每个事件点最多一次堆操作，排序 O(n log n)
# 空间复杂度: O(n) - 事件列表和堆各存储 O(n) 个元素
#
# 关键点:
# - 将建筑拆为开始和结束两个事件，统一按 x 排序处理
# - 用负高度实现最大堆(Python 的 heapq 是最小堆)
# - 惰性删除：不主动移除结束的建筑，只在堆顶过期时弹出
# - 关键点只在最高高度发生变化时记录
