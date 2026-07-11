"""
LeetCode #1329 - Sort the Matrix Diagonally
中文题名：将矩阵按对角线排序
https://leetcode.com/problems/sort-the-matrix-diagonally/

Given a `m * n` matrix `mat` of integers, sort it
diagonally in ascending order from the top-left to the bottom-right then return the
sorted array.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Constraints:

`m == mat.length`

`n == mat[i].length`

`1 <= m, n <= 100`

`1 <= mat[i][j] <= 100`

【中文翻译】
给定一个 `m x n` 的整数矩阵 `mat`，将矩阵中的每条对角线（从左上到右下方向）
按升序排序，然后返回排序后的矩阵。

示例 1：

输入: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
输出: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
解释：
原矩阵的对角线为：
(0,0)→(1,1)→(2,2): [3,2,1] → 排序为 [1,2,3]
(0,1)→(1,2)→(2,3): [3,2,2] → 排序为 [2,2,3]
(0,2)→(1,3): [1,1] → 排序为 [1,1]
(0,3): [1] → 排序为 [1]

约束条件：

`m == mat.length`

`n == mat[i].length`

`1 <= m, n <= 100`

`1 <= mat[i][j] <= 100`
"""

from typing import List, Optional


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diagonals = {}

        # 将同一对角线上的元素分组（对角线由 i - j 唯一标识）
        for i in range(m):
            for j in range(n):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(mat[i][j])

        # 对每条对角线进行排序
        for key in diagonals:
            diagonals[key].sort(reverse=True)  # 用栈的方式从大到小，方便 pop

        # 将排序后的值写回矩阵
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop()

        return mat



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 关键观察：在同一条从左上到右下的对角线上，所有元素的 (行索引 - 列索引) 值相等。
#    即对角线由 i - j 的值唯一标识。
# 2. 使用字典将矩阵中的每个元素按照其 (i - j) 分组到对应的对角线列表中。
# 3. 对每条对角线的元素列表进行排序（降序排序以便使用 pop() 从末尾取最小值）。
# 4. 再次遍历矩阵，将排序后的元素按顺序写回原来的位置。
#
# 时间复杂度: O(M*N*log(min(M,N))) — 最长的对角线长度为 min(M,N)，排序复杂度为对数级别
# 空间复杂度: O(M*N) — 字典存储所有矩阵元素
#
# 关键点:
# - 同一对角线上的元素满足 i - j 为常数
# - 使用降序排序配合 pop() 可以在 O(1) 时间内取出最小值
# - 也可以用 collections.defaultdict(list) 简化字典操作










