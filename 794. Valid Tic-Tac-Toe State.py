"""
LeetCode #794 - Valid Tic-Tac-Toe State
中文题名：有效的井字游戏状态
https://leetcode.com/problems/valid-tic-tac-toe-state/

A Tic-Tac-Toe board is given as a string array `board`. Return True if and only if
it is possible to reach this board position during the course of a valid tic-tac-toe game.

The `board` is a 3 x 3 array, and consists of characters `"
"`, `"X"`, and `"O"`.  The "
" character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").

The first player always places "X" characters, while the second player always
places "O" characters.

"X" and "O" characters are always placed into empty squares, never
filled ones.

The game ends when there are 3 of the same (non-empty) character filling any row,
column, or diagonal.

The game also ends if all squares are non-empty.

No more moves can be played if the game is over.

Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true

Note:

`board` is a length-3 array of strings, where each string
`board[i]` has length 3.

Each `board[i][j]` is a character in the set `{" ", "X",
"O"}`.

【中文翻译】
一个井字游戏棋盘由字符串数组 `board` 表示。如果该棋盘是在有效的井字游戏过程中可能达到的状态，则返回 True，否则返回 False。

`board` 是一个 3 x 3 的数组，由字符 `" "`、`"X"` 和 `"O"` 组成。`" "` 字符代表一个空位。

井字游戏的规则如下：
- 玩家轮流将字符放入空位（" "）。
- 第一个玩家始终放置 "X" 字符，第二个玩家始终放置 "O" 字符。
- "X" 和 "O" 只能放入空位，不能放入已填的格子。
- 当有 3 个相同（非空）字符填满任一行、列或对角线时，游戏结束。
- 当所有格子都被填满时，游戏也会结束。
- 游戏结束后不能再进行任何移动。

示例 1：
输入：board = ["O  ", "   ", "   "]
输出：false
解释：第一个玩家始终放置 "X"。

示例 2：
输入：board = ["XOX", " X ", "   "]
输出：false
解释：玩家轮流进行移动。

示例 3：
输入：board = ["XXX", "   ", "OOO"]
输出：false

示例 4：
输入：board = ["XOX", "O O", "XOX"]
输出：true

注意：
`board` 是长度为 3 的字符串数组，其中每个字符串 `board[i]` 的长度为 3。
每个 `board[i][j]` 是集合 `{" ", "X", "O"}` 中的一个字符。
"""

from typing import List, Optional


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)

        # X goes first, so X count must equal O count or be O count + 1
        if x_count not in (o_count, o_count + 1):
            return False

        def win(player: str) -> bool:
            # Check rows
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
            # Check columns
            for j in range(3):
                if all(board[i][j] == player for i in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False

        x_wins = win('X')
        o_wins = win('O')

        # If X wins, X must have one more move than O
        if x_wins and x_count != o_count + 1:
            return False
        # If O wins, counts must be equal
        if o_wins and x_count != o_count:
            return False

        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 棋盘状态有效的必要条件：
# 1. X 先手，所以 X 的数量要么等于 O 的数量（O 刚下完），
#    要么比 O 多 1（X 刚下完）。
# 2. 如果 X 赢了，那么 X 必须比 O 多 1（X 下最后一步获胜）。
# 3. 如果 O 赢了，那么 X 必须等于 O（O 下最后一步获胜）。
# 4. X 和 O 不可能同时赢（游戏结束后不会继续）。
#
# 通过遍历棋盘统计 X 和 O 的数量，然后检查所有行、列、
# 对角线是否有三连。根据胜负情况和数量关系判断是否有效。
#
# 时间复杂度: O(1) - 棋盘大小固定为 3x3
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - X 必须等于 O 或等于 O + 1
# - 获胜方必须对应正确的先手/后手数量关系
# - 两方不能同时获胜
