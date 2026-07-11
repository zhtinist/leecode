"""
LeetCode #1401 - Circle and Rectangle Overlapping
中文题名：圆和矩形是否有重叠
https://leetcode.com/problems/circle-and-rectangle-overlapping/

Given a circle represented as (`radius`, `x_center`, `y_center`) and
an axis-aligned rectangle represented as (`x1`, `y1`,
`x2`, `y2`), where (`x1`, `y1`) are the
coordinates of the bottom-left corner, and (`x2`, `y2`) are the
coordinates of the top-right corner of the rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.

In other words, check if there are any point (xi, yi) such that
belongs to the circle and the rectangle at the same time.

Example 1:

Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0)

Example 2:

Input: radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true

Example 3:

Input: radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
Output: true

Example 4:

Input: radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false

Constraints:

`1 <= radius <= 2000`

`-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4`

`x1 < x2`

`y1 < y2`

【中文翻译】

给定一个圆 (radius, x_center, y_center) 和一个与坐标轴平行的矩形 (x1, y1, x2, y2)，其中 (x1, y1) 为左下角坐标，(x2, y2) 为右上角坐标。

如果圆和矩形有重叠部分返回 True，否则返回 False。

即，检查是否存在任何点 (xi, yi) 同时属于圆和矩形。

示例 1：
输入：radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
输出：true
解释：圆和矩形共享点 (1,0)

示例 2：
输入：radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
输出：true

示例 3：
输入：radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
输出：true

示例 4：
输入：radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
输出：false

约束条件：
1 <= radius <= 2000
-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
x1 < x2
y1 < y2
"""

from typing import List, Optional


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # 找到矩形上离圆心最近的点
        closest_x = max(x1, min(x_center, x2))
        closest_y = max(y1, min(y_center, y2))

        # 计算最近点到圆心的距离平方
        dx = closest_x - x_center
        dy = closest_y - y_center

        return dx * dx + dy * dy <= radius * radius



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 圆和矩形重叠的充要条件是：矩形上离圆心最近的点到圆心的距离 <= 半径。
# 1. 将圆心坐标分别钳制（clamp）到矩形的 x 范围和 y 范围内，
#    得到矩形上离圆心最近的点 (closest_x, closest_y)。
# 2. 计算该点到圆心的距离平方。
# 3. 如果距离平方 <= 半径平方，则重叠。
#
# 时间复杂度: O(1)  只需常数次计算
# 空间复杂度: O(1)
#
# 关键点:
# - 不需要考虑复杂的几何相交判断，只需找最近点
# - clamp 操作：closest_x = max(x1, min(x_center, x2))
# - 使用距离平方比较避免浮点数的 sqrt 运算
# - 如果圆心在矩形内部，最近点就是圆心本身，距离为 0，一定重叠










