"""
LeetCode #223 - Rectangle Area
中文题名：矩形面积
https://leetcode.com/problems/rectangle-area/

Find the total area covered by two rectilinear rectangles in a
2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the
figure.

*

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45

Note:

Assume that the total area is never beyond the maximum possible value of int.

【中文翻译】
在二维平面上计算两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。

*

示例：

输入：A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
输出：45

注意：

假设总面积不会超过 int 的最大可能值。
"""

from typing import List, Optional


class Solution:
    def computeArea(
        self,
        ax1: int, ay1: int, ax2: int, ay2: int,
        bx1: int, by1: int, bx2: int, by2: int,
    ) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        overlap_x = min(ax2, bx2) - max(ax1, bx1)
        overlap_y = min(ay2, by2) - max(ay1, by1)
        overlap = max(0, overlap_x) * max(0, overlap_y)

        return area1 + area2 - overlap












# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 总面积 = 矩形1面积 + 矩形2面积 - 重叠部分面积。
# 1. 计算两个矩形各自的面积：
#    area1 = (ax2 - ax1) * (ay2 - ay1)
#    area2 = (bx2 - bx1) * (by2 - by1)
# 2. 计算重叠部分(交集的宽和高)：
#    overlap_x = min(ax2, bx2) - max(ax1, bx1)  — 右边界的最小值 - 左边界的最大值
#    overlap_y = min(ay2, by2) - max(ay1, by1)  — 上边界的最小值 - 下边界的最大值
# 3. 若 overlap_x <= 0 或 overlap_y <= 0，说明无重叠，用 max(0, ...) 处理。
#    overlap = overlap_x * overlap_y (如果重叠存在)
# 4. 返回 area1 + area2 - overlap。
#
# 时间复杂度: O(1) - 纯数学计算
# 空间复杂度: O(1) - 只使用常数变量
#
# 关键点:
# - 重叠宽度的计算：右边界取 min，左边界取 max，差值即为重叠宽度
# - 用 max(0, ...) 处理无重叠的情况(差值为负时重叠面积为 0)
# - 无需判断两个矩形的相对位置，公式自动处理所有情况
