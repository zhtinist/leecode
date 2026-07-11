"""
LeetCode #497 - Random Point in Non-overlapping Rectangles
中文题名：非重叠矩形中的随机点
https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

Given a list of non-overlapping axis-aligned rectangles
`rects`, write a function `pick` which randomly and uniformily picks
an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates.

A point on the perimeter of a rectangle is included in
the space covered by the rectangles.

`i`th rectangle = `rects[i]` = `[x1,y1,x2,y2]`,
where `[x1, y1]` are the integer coordinates of the bottom-left corner,
and `[x2, y2]` are the integer coordinates of the top-right corner.

length and width of each rectangle does not exceed `2000`.

`1 <= rects.length <= 100`

`pick` return a point as an array of integer coordinates `[p_x,
p_y]`

`pick` is called at most `10000` times.

Example 1:

Input:
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output:
[null,[4,1],[4,1],[3,3]]

Example 2:

Input:
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output:
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]

【中文翻译】
给定一个非重叠轴对齐矩形列表 rects，编写一个函数 pick 在矩形覆盖的空间中
随机均匀地选择一个整数点。

注意：
    整数点是指具有整数坐标的点。
    矩形边界上的点包含在矩形覆盖的空间中。
    第 i 个矩形 rects[i] = [x1, y1, x2, y2]，其中 [x1, y1] 是左下角的整数坐标，
    [x2, y2] 是右上角的整数坐标。
    每个矩形的长度和宽度不超过 2000。
    1 <= rects.length <= 100。
    pick 函数返回一个整数坐标数组 [p_x, p_y]。
    pick 最多被调用 10000 次。

示例 1：
    输入：
    ["Solution","pick","pick","pick"]
    [[[[1,1,5,5]]],[],[],[]]
    输出：
    [null,[4,1],[4,1],[3,3]]

示例 2：
    输入：
    ["Solution","pick","pick","pick","pick","pick"]
    [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
    输出：
    [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
"""

import random
import bisect
from typing import List, Optional


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total_points = 0
        for x1, y1, x2, y2 in rects:
            # 整数点数 = (宽度+1) * (高度+1)，包含边界
            points = (x2 - x1 + 1) * (y2 - y1 + 1)
            total_points += points
            self.prefix.append(total_points)
        self.total_points = total_points

    def pick(self) -> List[int]:
        # 按面积加权随机选择一个矩形
        rand_area = random.randint(1, self.total_points)
        idx = bisect.bisect_left(self.prefix, rand_area)
        x1, y1, x2, y2 = self.rects[idx]
        # 在选中的矩形内随机选择一个整数点
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 先计算每个矩形包含的整数点数 = (x2 - x1 + 1) * (y2 - y1 + 1)（包含边界）。
# 构建前缀和数组 prefix，prefix[i] 表示前 i 个矩形的累计点数。
# pick 时：生成 [1, total_points] 内的随机数，通过二分查找确定该点落在哪个矩形内，
# 再在该矩形内随机选取一个整数坐标 (x, y)。
# 由于每个矩形被选中的概率与其面积（点数）成正比，实现了均匀随机。
#
# 时间复杂度: 初始化 O(N)，pick O(log N)，N 为矩形个数
# 空间复杂度: O(N) — 存储前缀和数组
#
# 关键点:
# - 整数点数量公式：(x2 - x1 + 1) * (y2 - y1 + 1)，注意 +1 包含边界
# - 前缀和 + 二分查找实现加权随机选择
# - 矩形之间非重叠，点不会重复，保证均匀分布
# - 使用 random.randint 生成均匀随机坐标
