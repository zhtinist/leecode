"""
LeetCode #3453 - Separate Squares I
分割正方形 I
https://leetcode.cn/problems/separate-squares-i/

给你一个二维整数数组 `squares` ，其中 `squares[i] = [x_i, y_i, l_i]` 表示一个与 x 轴平行的正方形的左下角坐标和正方形的边长。
找到一个最小的 y 坐标，它对应一条水平线，该线需要满足它以上正方形的总面积 等于 该线以下正方形的总面积。
答案如果与实际答案的误差在 `10^-5` 以内，将视为正确答案。
注意：正方形 可能会 重叠。重叠区域应该被 多次计数 。

示例 1：

输入： squares = [[0,0,1],[2,2,1]]
输出： 1.00000
解释：

任何在 `y = 1` 和 `y = 2` 之间的水平线都会有 1 平方单位的面积在其上方，1 平方单位的面积在其下方。最小的 y 坐标是 1。
示例 2：

输入： squares = [[0,0,2],[1,1,1]]
输出： 1.16667
解释：

面积如下：
线下的面积：`7/6 * 2 (红色) + 1/6 (蓝色) = 15/6 = 2.5`。
线上的面积：`5/6 * 2 (红色) + 5/6 (蓝色) = 15/6 = 2.5`。
由于线以上和线以下的面积相等，输出为 `7/6 = 1.16667`。

提示：
`1 <= squares.length <= 5 * 10^4`
`squares[i] = [x_i, y_i, l_i]`
`squares[i].length == 3`
`0 <= x_i, y_i <= 10^9`
`1 <= l_i <= 10^9`
所有正方形的总面积不超过 `10^12`。
"""

from typing import List, Optional


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2.0

        lo, hi = 0.0, 2e9  # max y + max l <= 2*10^9
        for _ in range(80):  # enough for 1e-5 precision
            mid = (lo + hi) / 2.0
            above = 0.0
            for x, y, l in squares:
                if mid >= y + l:
                    continue
                elif mid <= y:
                    above += l * l
                else:
                    above += l * (y + l - mid)
            if above > target:
                lo = mid
            else:
                hi = mid
        return lo



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search
#
# 解题思路:
# 1. 计算所有正方形的总面积 total_area，目标是线上的面积 = 线下的面积 = total_area / 2
# 2. 面积 above(mid) 随 mid 增大而单调递减：
#    - mid >= y + l: 正方形完全在线下，above = 0
#    - mid <= y: 正方形完全在线上，above = l^2
#    - y < mid < y + l: 切割，above = l * (y + l - mid)
# 3. 二分查找最小的 y 使得 above(y) <= total_area / 2
# 4. 题目要求返回最小的 y 坐标，所以当 above == target 时使 hi = mid 收缩
#
# 时间复杂度: O(n * log(range/precision)) ≈ O(80n)
# 空间复杂度: O(1)
#
# 关键点:
# - 重叠正方形要分别计数（多次计数重叠面积）
# - 二分 80 次保证精度达到 1e-5
# - 单调性：线越高，上方面积越小
