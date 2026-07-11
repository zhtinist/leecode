"""
LeetCode #3484 - Design Spreadsheet
设计电子表格
https://leetcode.cn/problems/design-spreadsheet/

电子表格是一个网格，它有 26 列（从 `'A'` 到 `'Z'`）和指定数量的 `rows`。每个单元格可以存储一个 0 到 10^5 之间的整数值。
请你实现一个 `Spreadsheet` 类：
`Spreadsheet(int rows)` 初始化一个具有 26 列（从 `'A'` 到 `'Z'`）和指定行数的电子表格。所有单元格最初的值都为 0 。
`void setCell(String cell, int value)` 设置指定单元格的值。单元格引用以 `"AX"` 的格式提供（例如，`"A1"`，`"B10"`），其中字母表示列（从 `'A'` 到 `'Z'`），数字表示从 1 开始的行号。
`void resetCell(String cell)` 重置指定单元格的值为 0 。
`int getValue(String formula)` 计算一个公式的值，格式为 `"=X+Y"`，其中 `X` 和 `Y` 要么 是单元格引用，要么非负整数，返回计算的和。
注意： 如果 `getValue` 引用一个未通过 `setCell` 明确设置的单元格，则该单元格的值默认为 0 。

示例 1：

输入：
["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
[[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]
输出：
[null, 12, null, 16, null, 25, null, 15]
解释 Spreadsheet spreadsheet = new Spreadsheet(3); // 初始化一个具有 3 行和 26 列的电子表格
spreadsheet.getValue("=5+7"); // 返回 12 (5+7)
spreadsheet.setCell("A1", 10); // 设置 A1 为 10
spreadsheet.getValue("=A1+6"); // 返回 16 (10+6)
spreadsheet.setCell("B2", 15); // 设置 B2 为 15
spreadsheet.getValue("=A1+B2"); // 返回 25 (10+15)
spreadsheet.resetCell("A1"); // 重置 A1 为 0
spreadsheet.getValue("=A1+B2"); // 返回 15 (0+15)

提示：
`1 <= rows <= 10^3`
`0 <= value <= 10^5`
公式保证采用 `"=X+Y"` 格式，其中 `X` 和 `Y` 要么是有效的单元格引用，要么是小于等于 `10^5` 的 非负 整数。
每个单元格引用由一个大写字母 `'A'` 到 `'Z'` 和一个介于 `1` 和 `rows` 之间的行号组成。
总共 最多会对 `setCell`、`resetCell` 和 `getValue` 调用 `10^4` 次。
"""

from typing import List, Optional


class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.grid = [[0] * 26 for _ in range(rows)]

    def _parseCell(self, cell: str):
        """Parse 'A1' -> (row_idx, col_idx)"""
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        r, c = self._parseCell(cell)
        self.grid[r][c] = value

    def resetCell(self, cell: str) -> None:
        r, c = self._parseCell(cell)
        self.grid[r][c] = 0

    def _resolve(self, token: str) -> int:
        """Resolve a token: either a cell reference or an integer"""
        if token[0].isalpha():
            r, c = self._parseCell(token)
            return self.grid[r][c]
        return int(token)

    def getValue(self, formula: str) -> int:
        # formula format: "=X+Y"
        parts = formula[1:].split('+')
        return self._resolve(parts[0]) + self._resolve(parts[1])



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Array, Hash Table, String, Matrix
#
# 解题思路:
# 1. 使用二维数组 grid[rows][26] 存储单元格值
# 2. setCell: 解析单元格字符串（如 "A1" -> 行 0, 列 0），设置值
# 3. resetCell: 将指定单元格值设为 0
# 4. getValue: 解析公式 "=X+Y"，将 X 和 Y 解析为单元格值或整数，返回和
# 5. 辅助方法 _parseCell 将 "A1" 格式转为行列索引
#    _resolve 将 token 解析为数值（单元格引用或直接数字）
#
# 时间复杂度: setCell/resetCell/getValue 均为 O(1)
# 空间复杂度: O(26 * rows) = O(rows)
#
# 关键点:
# - 列字母到索引的转换：ord(col) - ord('A')
# - 行号从 1 开始：int(cell[1:]) - 1
# - 公式始终是 "=X+Y" 格式，用 '+' 分割即可
