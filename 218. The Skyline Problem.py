"""
LeetCode #218 - The Skyline Problem
中文题名：天际线问题
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

【中文翻译】
城市的 skyline 是从远处观看该城市所有建筑物形成的轮廓的外轮廓。现在假设你得到了一个城市的建筑物位置和高度，如图 A 所示，编写一个程序来输出这些建筑物共同形成的天际线，如图 B 所示。

*   *

每个建筑物的几何信息由一组三元组 `[Li, Ri, Hi]` 表示，其中 `Li` 和 `Ri` 分别是第 i 个建筑物左边缘和右边缘的 x 坐标，`Hi` 是其高度。保证 `0 <= Li, Ri <= INT_MAX`，`0 < Hi <= INT_MAX`，且 `Ri - Li > 0`。你可以假设所有建筑物都是在高度为 0 的绝对平坦表面上的完美矩形。

例如，图 A 中所有建筑物的尺寸记录为：`[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]`。

输出是一个「关键点」列表（图 B 中的红点），格式为 `[ [x1,y1], [x2, y2], [x3, y3], ... ]`，它唯一地定义了天际线。关键点是水平线段的左端点。请注意，最后一个关键点（最右侧建筑物的结束点）仅用于标记天际线的终止，其高度始终为零。此外，任何两个相邻建筑物之间的地面也应被视为天际线轮廓的一部分。

例如，图 B 中的天际线应表示为：`[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]`。

说明：

任何输入列表中的建筑物数量保证在 `[0, 10000]` 范围内。

输入列表已按左 x 坐标 `Li` 升序排序。

输出列表必须按 x 坐标排序。

输出天际线中不得有连续相同高度的水平线。例如，`[...[2 3], [4 5], [7 5], [11 5], [12 7]...]` 是不可接受的；高度为 5 的三条线应在最终输出中合并为一条，例如：`[...[2 3], [4 5], [12 7], ...]`
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
