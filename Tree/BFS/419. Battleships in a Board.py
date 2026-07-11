"""
LeetCode #419 - Battleships in a Board
中文题名：甲板上的战舰
https://leetcode.com/problems/battleships-in-a-board/

Given an 2D board, count how many battleships are in it. The battleships are represented with
`'X'`s, empty slots are represented with `'.'`s. You may assume the
following rules:

You receive a valid board, made of only battleships or empty slots.

Battleships can only be placed horizontally or vertically. In other words, they can only
be made of the shape `1xN` (1 row, N columns) or `Nx1` (N rows, 1
column), where N can be of any size.

At least one horizontal or vertical cell separates between two battleships - there are
no adjacent battleships.

Example:

X..X
...X
...X

In the above board there are 2 battleships.

Invalid Example:

...X
XXXX
...X

This is an invalid board that you will not receive - as battleships will always have a cell
separating between them.

Follow up:
Could you do it in one-pass, using only O(1) extra memory
and without modifying the value of the board?

【中文翻译】
给定一个二维甲板，计算有多少艘战舰。战舰用 'X' 表示，空位用 '.' 表示。需遵守以下规则：
    你会收到一个有效的甲板，仅由战舰或空位组成。
    战舰只能水平或垂直放置，即形状为 1×N（1行N列）或 N×1（N行1列），N可为任意大小。
    两艘战舰之间至少有一个水平或垂直的空格隔开——不存在相邻的战舰。

示例：
    X..X
    ...X
    ...X
    上面的甲板中有 2 艘战舰。

无效示例（你不会收到）：
    ...X
    XXXX
    ...X
    因为战舰之间始终有空位隔开。

进阶：能否用 O(1) 额外内存、一遍扫描、且不修改甲板值来完成？
"""

from typing import List, Optional


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0

        rows, cols = len(board), len(board[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    # Only count if it's the first cell of a battleship
                    # (no X above and no X to the left)
                    if (r == 0 or board[r - 1][c] != "X") and \
                       (c == 0 or board[r][c - 1] != "X"):
                        count += 1

        return count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 因为战舰只能水平或垂直放置（1×N 或 N×1），且两艘战舰不能相邻，
# 所以每艘战舰的"左上角"（即第一个 X）是唯一可识别的：
#   - 它的上方不是 X（要么是第一行，要么上方是 '.'）
#   - 它的左方不是 X（要么是第一列，要么左方是 '.'）
#
# 遍历整个甲板，对于每个 X，检查它的上方和左方：
#   如果都不是 X，说明这是艘新战舰的起点，计数 +1。
#
# 这满足进阶要求：
# - 一遍扫描 O(M*N)
# - O(1) 额外空间
# - 不修改原数组
#
# 时间复杂度: O(M * N) — 遍历所有单元格
# 空间复杂度: O(1) — 只使用常数变量
#
# 关键点:
# - 只统计每艘战舰的"左上角"起始单元格
# - 利用战舰只能水平或垂直放置且不重叠的约束
# - 不需要 DFS/BFS 或修改数组
