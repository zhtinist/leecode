"""
LeetCode #1253 - Reconstruct a 2-Row Binary Matrix
中文题名：重构 2 行二进制矩阵
https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

Given the following details of a matrix with `n` columns and `2` rows :

The matrix is a binary matrix, which means each element in the matrix can be
`0` or `1`.

The sum of elements of the 0-th(upper) row is given as `upper`.

The sum of elements of the 1-st(lower) row is given as `lower`.

The sum of elements in the i-th column(0-indexed) is `colsum[i]`, where
`colsum` is given as an integer array with length `n`.

Your task is to reconstruct the matrix with `upper`, `lower` and `colsum`.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.

Example 1:

Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.

Example 2:

Input: upper = 2, lower = 3, colsum = [2,2,1,1]
Output: []

Example 3:

Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]

Constraints:

`1 <= colsum.length <= 10^5`

`0 <= upper, lower <= colsum.length`

`0 <= colsum[i] <= 2`

【中文翻译】
给定一个具有 `n` 列和 `2` 行的矩阵的以下信息：

- 矩阵是二进制矩阵，这意味着矩阵中的每个元素可以是 `0` 或 `1`。
- 第 0 行（上方行）的元素之和为 `upper`。
- 第 1 行（下方行）的元素之和为 `lower`。
- 第 i 列（0 索引）的元素之和为 `colsum[i]`，其中 `colsum` 是一个长度为 `n` 的整数数组。

你的任务是用 `upper`、`lower` 和 `colsum` 来重构该矩阵。

以二维整数数组的形式返回它。

如果有多个有效解，任何一个都会被接受。

如果不存在有效解，返回一个空的二维数组。

示例 1：

输入：upper = 2, lower = 1, colsum = [1,1,1]
输出：[[1,1,0],[0,0,1]]
解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。

示例 2：

输入：upper = 2, lower = 3, colsum = [2,2,1,1]
输出：[]

示例 3：

输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]

约束条件：

`1 <= colsum.length <= 10^5`

`0 <= upper, lower <= colsum.length`

`0 <= colsum[i] <= 2`
"""

from typing import List, Optional


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)

        # Quick check: total sum must match
        if upper + lower != sum(colsum):
            return []

        upper_row = [0] * n
        lower_row = [0] * n

        for i in range(n):
            if colsum[i] == 2:
                upper_row[i] = 1
                lower_row[i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper >= lower:
                    upper_row[i] = 1
                    upper -= 1
                else:
                    lower_row[i] = 1
                    lower -= 1

        if upper != 0 or lower != 0:
            return []

        return [upper_row, lower_row]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法。
# 1. 首先验证：所有列和的总和必须等于 upper + lower，否则无解。
# 2. 遍历每一列 i：
#    - colsum[i] == 2：两行都必须放 1，upper 和 lower 各减 1。
#    - colsum[i] == 1：需要在上下两行中选择一行放 1。贪心策略：优先分配给剩余需求较大的一行
#      （if upper >= lower: 放上行，else: 放下行），这样可以最大化可行解的几率。
#    - colsum[i] == 0：两行都放 0，不做任何操作。
# 3. 遍历结束后，如果 upper == 0 且 lower == 0，返回结果矩阵；否则返回空数组。
# 为什么贪心有效：只要总量匹配，逐列优先满足需求量较大的一行一定能构造出解（前提是没有矛盾）。
#
# 时间复杂度: O(N)，一次遍历
# 空间复杂度: O(N)，存储结果矩阵
#
# 关键点:
# - 先处理 colsum[i] == 2 的列（两行都必须为 1）
# - 对于 colsum[i] == 1，优先分配给 upper 和 lower 中较大的那个
# - 贪心策略保证：只要总和要求匹配，就一定不会在中途导致某一行超过上限
# - 最终验证 upper == lower == 0，防止中途某行被减成负数
