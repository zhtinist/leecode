"""
LeetCode #452 - Minimum Number of Arrows to Burst Balloons
中文题名：用最少数量的箭引爆气球
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

There are a number of spherical balloons spread in two-dimensional space. For each balloon,
provided input is the start and end coordinates of the horizontal diameter. Since it's
horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of
the diameter suffice. Start is always smaller than end. There will be at most 104
balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon
with xstart and xend bursts by an arrow shot at x if xstart
<= x <= xend. There is no limit to the number of arrows that can be shot. An
arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of
arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

【中文翻译】
在二维空间中有许多球形的气球。对于每个气球，输入是气球水平直径的起始和结束坐标。
因为是水平的，y 坐标无关紧要，只需 x_start 和 x_end。start 始终小于 end。最多有 10^4 个气球。

一支箭可以从 x 轴的不同点垂直向上射出。如果 x_start <= x <= x_end，则气球会被在 x 处射出的箭引爆。
射出的箭没有数量限制。箭一旦射出，会一直向上无限飞行。求引爆所有气球所需的最少箭数。

示例：
输入：[[10,16], [2,8], [1,6], [7,12]]
输出：2
解释：一种方式是在 x=6 处射一箭（引爆 [2,8] 和 [1,6]），在 x=11 处再射一箭（引爆另外两个气球）。
"""

from typing import List, Optional


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort balloons by end coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        # Position the first arrow at the end of the first balloon
        arrow_pos = points[0][1]

        for start, end in points[1:]:
            # If current balloon starts after the arrow position,
            # we need a new arrow
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法：按气球的结束坐标排序。在第一个气球的结束位置射第一支箭，可以引爆所有与该位置重叠的气球。
# 当遇到一个开始坐标大于当前箭位置的气球时，需要新的一支箭，将其射在该气球的结束位置。
# 这等价于经典的"区间调度/无重叠区间"问题的变体。
#
# 时间复杂度: O(N log N) — 排序开销
# 空间复杂度: O(1) — 排序可能 O(N) 取决于排序算法实现，但一般忽略不计
#
# 关键点:
# - 按结束坐标而非开始坐标排序是关键（贪心选择：最早结束的区间）
# - 每次射箭位置选择当前气球区间的右端点
# - 与 #435 Non-overlapping Intervals 思路相似
