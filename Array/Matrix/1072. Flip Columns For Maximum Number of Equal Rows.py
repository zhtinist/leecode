"""
LeetCode #1072 - Flip Columns For Maximum Number of Equal Rows
中文题名：按列翻转得到最大值相等的行数
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

Given a `matrix` consisting of 0s and 1s, we may choose any number of columns in
the matrix and flip every cell in that column.  Flipping a cell
changes the value of that cell from 0 to 1 or from 1 to 0.

Return the maximum number of rows that have all values equal after some number of flips.

Example 1:

Input: [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:

Input: [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:

Input: [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.

Note:

`1 <= matrix.length <= 300`

`1 <= matrix[i].length <= 300`

All `matrix[i].length`'s are equal

`matrix[i][j]` is `0` or `1`

【中文翻译】
给定由若干 0 和 1 组成的矩阵 matrix，从中选出任意数量的列并翻转其上的每个单元格。翻转后，单元格的值从 0 变成 1，或者从 1 变成 0。

返回经过一些翻转后，行内所有值都相等的最大行数。

示例 1：

输入：[[0,1],[1,1]]
输出：1
解释：不进行翻转，有 1 行所有值都相等。

示例 2：

输入：[[0,1],[1,0]]
输出：2
解释：翻转第一列的值之后，这两行都具有相等的值。

示例 3：

输入：[[0,0,0],[0,0,1],[1,1,0]]
输出：2
解释：翻转前两列的值之后，后两行具有相等的值。

注意：

1 <= matrix.length <= 300
1 <= matrix[i].length <= 300
所有 matrix[i].length 都相等
matrix[i][j] 为 0 或 1

"""

from typing import List, Optional


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import Counter

        patterns = Counter()
        for row in matrix:
            if row[0] == 1:
                normalized = tuple(1 - x for x in row)
            else:
                normalized = tuple(row)
            patterns[normalized] += 1

        return max(patterns.values())










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键洞察：两行能在相同的列翻转后变为全相等行，当且仅当它们具有相同的模式或互为正反（即一行是另一行的完全翻转）。
# 例如 [0,0,1] 和 [1,1,0] 互为正反——翻转前两列后都变成 [1,1,0]。
# 因此，我们可以将每一行标准化：如果第一个元素是 1，则翻转整行；否则保持不变。
# 这样标准化后，所有能通过相同列翻转变成全等行的行都会变成相同的模式。
# 使用 Counter 统计每种标准化模式出现的次数，返回最大值。
#
# 时间复杂度: O(m * n) - m 为行数，n 为列数
# 空间复杂度: O(m * n) - 存储所有行的标准化模式
#
# 关键点:
# - 按第一个元素标准化：首元素为 1 则翻转整行
# - 翻转整行等价于对每列取反 (1 - x)
# - 互为正反的两行在标准化后变为相同模式
# - 统计出现次数最多的模式即为答案
