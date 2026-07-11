"""
LeetCode #1901 - Find a Peak Element II
寻找峰值 II
https://leetcode.cn/problems/find-a-peak-element-ii/

一个 2D 网格中的 峰值 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。
给你一个 从 0 开始编号 的 `m x n` 矩阵 `mat` ，其中任意两个相邻格子的值都 不相同 。找出 任意一个 峰值 `mat[i][j]` 并 返回其位置 `[i,j]` 。
你可以假设整个矩阵周边环绕着一圈值为 `-1` 的格子。
要求必须写出时间复杂度为 `O(m log(n))` 或 `O(n log(m))` 的算法

示例 1:

输入: mat = [[1,4],[3,2]] 输出: [0,1] 解释: 3 和 4 都是峰值，所以[1,0]和[0,1]都是可接受的答案。
示例 2:

输入: mat = [[10,20,15],[21,30,14],[7,16,32]] 输出: [1,1] 解释: 30 和 32 都是峰值，所以[1,1]和[2,2]都是可接受的答案。

提示：
`m == mat.length`
`n == mat[i].length`
`1 <= m, n <= 500`
`1 <= mat[i][j] <= 10^5`
任意两个相邻元素均不相等.
"""

from typing import List, Optional


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        left, right = 0, n - 1

        while left <= right:
            mid_col = (left + right) // 2

            # Find row with max value in this column
            max_row = 0
            for row in range(m):
                if mat[row][mid_col] > mat[max_row][mid_col]:
                    max_row = row

            # Compare with left neighbor
            left_is_bigger = mid_col > 0 and mat[max_row][mid_col - 1] > mat[max_row][mid_col]
            # Compare with right neighbor
            right_is_bigger = mid_col < n - 1 and mat[max_row][mid_col + 1] > mat[max_row][mid_col]

            if not left_is_bigger and not right_is_bigger:
                return [max_row, mid_col]
            elif left_is_bigger:
                right = mid_col - 1
            else:
                left = mid_col + 1

        return [-1, -1]  # Should never reach here



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Matrix
#
# 解题思路:
# 二分查找列，O(m log n) 复杂度。
# 1. 在中间列找到最大值所在行 max_row。
# 2. 比较该位置与左右邻居：
#    - 如果大于左右邻居，则找到峰值。
#    - 如果左边邻居更大，说明左侧存在峰值，移动右边界。
#    - 如果右边邻居更大，说明右侧存在峰值，移动左边界。
# 3. 正确性保证：从中列最大值向更大方向移动，一定会遇到峰值
#    （因为边界外视为 -∞，且所有相邻元素不相等）。
#
# 时间复杂度: O(m log n)
# 空间复杂度: O(1)
#
# 关键点:
# - 利用二维矩阵的极值性质进行列二分
# - 每次找到当前列的最大值，比较左右邻居
# - 向更大的方向移动一定能找到峰值
# - 所有相邻元素不相等保证了没有"平台"
