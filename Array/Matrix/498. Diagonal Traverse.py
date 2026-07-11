"""
LeetCode #498 - Diagonal Traverse
中文题名：对角线遍历
https://leetcode.com/problems/diagonal-traverse/

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in
diagonal order as shown in the below image.

Example:

Input:
[
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

Note:

The total number of elements of the given matrix will not exceed 10,000.

【中文翻译】
给定一个包含 M x N 个元素的矩阵（M 行，N 列），请按照对角线遍历的顺序返回矩阵中的所有元素。

示例：
    输入：
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    输出：[1,2,4,7,5,3,6,8,9]

解释：
    遍历顺序为：从左上角开始，先向上走对角线，碰到边界后转向向下走对角线，交替进行。
    对角线方向：
    第 0 条对角线（向上）：[1]
    第 1 条对角线（向下）：[2, 4]
    第 2 条对角线（向上）：[7, 5, 3]
    第 3 条对角线（向下）：[6, 8]
    第 4 条对角线（向上）：[9]

注意：
    矩阵中的元素总数不超过 10,000。
"""

from typing import List, Optional


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        # 共有 m + n - 1 条对角线
        for diag in range(m + n - 1):
            if diag % 2 == 0:
                # 向上走：从下到上
                r = min(diag, m - 1)
                c = diag - r
                while r >= 0 and c < n:
                    result.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                # 向下走：从上到下
                c = min(diag, n - 1)
                r = diag - c
                while c >= 0 and r < m:
                    result.append(mat[r][c])
                    r += 1
                    c -= 1

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 对角线上所有元素的 (i + j) 之和相同，共有 m + n - 1 条对角线（编号 0 到 m+n-2）。
# 遍历每条对角线：偶数编号对角线方向向上（从下到上），奇数编号方向向下（从上到下）。
# 通过确定每条对角线的起始位置（行和列），按照方向依次收集元素加入结果。
# 关键公式：
# - 偶数对角线起始行 = min(diag, m-1)，起始列 = diag - 起始行
# - 奇数对角线起始列 = min(diag, n-1)，起始行 = diag - 起始列
#
# 时间复杂度: O(M * N) — 每个元素访问一次
# 空间复杂度: O(1) — 不计输出数组（若计入则为 O(M*N)）
#
# 关键点:
# - 对角线编号 = i + j，范围 [0, m+n-2]
# - 偶数对角线方向向上（行递减、列递增），奇数对角线方向向下（行递增、列递减）
# - 注意边界处理：起始位置不能超出矩阵范围
