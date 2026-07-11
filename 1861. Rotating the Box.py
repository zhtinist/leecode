"""
LeetCode #1861 - Rotating the Box
旋转盒子
https://leetcode.cn/problems/rotating-the-box/

给你一个 `m x n` 的字符矩阵 `boxGrid` ，它表示一个箱子的侧视图。箱子的每一个格子可能为：
`'#'` 表示石头
`'*'` 表示固定的障碍物
`'.'` 表示空位置
这个箱子被 顺时针旋转 90 度 ，由于重力原因，部分石头的位置会发生改变。每个石头会垂直掉落，直到它遇到障碍物，另一个石头或者箱子的底部。重力 不会 影响障碍物的位置，同时箱子旋转不会产生惯性 ，也就是说石头的水平位置不会发生改变。
题目保证初始时 `boxGrid` 中的石头要么在一个障碍物上，要么在另一个石头上，要么在箱子的底部。
请你返回一个 `n x m` 的矩阵，表示按照上述旋转后，箱子内的结果。

示例 1：

输入：box = [["#",".","#"]] 输出：[["."],       ["#"],       ["#"]]
示例 2：

输入：box = [["#",".","*","."],             ["#","#","*","."]] 输出：[["#","."],       ["#","#"],       ["*","*"],       [".","."]]
示例 3：

输入：box = [["#","#","*",".","*","."],             ["#","#","#","*",".","."],             ["#","#","#",".","#","."]] 输出：[[".","#","#"],       [".","#","#"],       ["#","#","*"],       ["#","*","."],       ["#",".","*"],       ["#",".","."]]

提示：
`m == boxGrid.length`
`n == boxGrid[i].length`
`1 <= m, n <= 500`
`boxGrid[i][j]` 只可能是 `'#'` ，`'*'` 或者 `'.'` 。
"""

from typing import List, Optional


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # Step 1: Let stones fall to the right (gravity simulation)
        for row in boxGrid:
            # Two pointers: write_pos is where next stone should land
            write_pos = n - 1
            for col in range(n - 1, -1, -1):
                if row[col] == '*':
                    write_pos = col - 1
                elif row[col] == '#':
                    row[col] = '.'
                    row[write_pos] = '#'
                    write_pos -= 1

        # Step 2: Rotate 90 degrees clockwise
        # New matrix: n rows x m columns
        # result[r][c] = original[m-1-c][r]
        result = [[''] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                result[r][c] = boxGrid[m - 1 - c][r]

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, Matrix
#
# 解题思路:
# 分两步处理：
# 1. 重力模拟：对于每一行，从右向左扫描，使用双指针将石头'#'移动到
#    最右侧可用位置（被障碍物'*'阻挡时重置位置）。
# 2. 旋转矩阵：将 m x n 矩阵顺时针旋转90度得到 n x m 矩阵。
#    旋转公式：result[r][c] = original[m-1-c][r]
#
# 时间复杂度: O(m * n) — 遍历所有格子两次
# 空间复杂度: O(m * n) — 结果矩阵的空间
#
# 关键点:
# - 重力模拟时障碍物'*'会阻挡石头下落
# - 旋转公式：原矩阵的行变为新矩阵的列（从下到上）
# - 障碍物位置不受重力影响
