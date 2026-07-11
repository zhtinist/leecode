"""
LeetCode #1958 - Check if Move is Legal
检查操作是否合法
https://leetcode.cn/problems/check-if-move-is-legal/

给你一个下标从 0 开始的 `8 x 8` 网格 `board` ，其中 `board[r][c]` 表示游戏棋盘上的格子 `(r, c)` 。棋盘上空格用 `'.'` 表示，白色格子用 `'W'` 表示，黑色格子用 `'B'` 表示。
游戏中每次操作步骤为：选择一个空格子，将它变成你正在执行的颜色（要么白色，要么黑色）。但是，合法 操作必须满足：涂色后这个格子是 好线段的一个端点 （好线段可以是水平的，竖直的或者是对角线）。
好线段 指的是一个包含 三个或者更多格子（包含端点格子）的线段，线段两个端点格子为 同一种颜色 ，且中间剩余格子的颜色都为 另一种颜色 （线段上不能有任何空格子）。你可以在下图找到好线段的例子：
给你两个整数 `rMove` 和 `cMove` 以及一个字符 `color` ，表示你正在执行操作的颜色（白或者黑），如果将格子 `(rMove, cMove)` 变成颜色 `color` 后，是一个 合法 操作，那么返回 `true` ，如果不是合法操作返回 `false` 。

示例 1：

输入：board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B" 输出：true 解释：'.'，'W' 和 'B' 分别用颜色蓝色，白色和黑色表示。格子 (rMove, cMove) 用 'X' 标记。 以选中格子为端点的两个好线段在上图中用红色矩形标注出来了。
示例 2：

输入：board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W" 输出：false 解释：虽然选中格子涂色后，棋盘上产生了好线段，但选中格子是作为中间格子，没有产生以选中格子为端点的好线段。

提示：
`board.length == board[r].length == 8`
`0 <= rMove, cMove < 8`
`board[rMove][cMove] == '.'`
`color` 要么是 `'B'` 要么是 `'W'` 。
"""

from typing import List, Optional


class Solution:
    def checkMove(
        self, board: List[List[str]], rMove: int, cMove: int, color: str
    ) -> bool:
        """
        Check all 8 directions. In each direction, look for:
        an opposite color piece adjacent, then a same color piece further out.
        """
        n = 8
        opponent = "B" if color == "W" else "W"
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]

        for dr, dc in directions:
            r, c = rMove + dr, cMove + dc
            # First step must exist, be opponent's color
            if not (0 <= r < n and 0 <= c < n) or board[r][c] != opponent:
                continue
            # Walk further in this direction
            r += dr
            c += dc
            while 0 <= r < n and 0 <= c < n:
                if board[r][c] == ".":
                    break
                if board[r][c] == color:
                    return True
                r += dr
                c += dc

        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Enumeration, Matrix
#
# 解题思路:
# 检查 8 个方向。对于每个方向：
# 1. 相邻格子必须是对手的颜色
# 2. 沿着该方向继续走，如果遇到空格子则无效
# 3. 如果遇到自己颜色的格子，则形成好线段，返回 True
# 4. 如果遇到越界则无效
# 形象理解：放下的棋子作为端点，中间夹着对手的连续棋子，
# 另一端必须也是自己的颜色。
#
# 时间复杂度: O(1)，棋盘固定 8x8
# 空间复杂度: O(1)
#
# 关键点:
# - 好线段的定义：两个端点同色，中间全是另一颜色
# - 8 个方向都要检查
# - 相邻第一格必须是对手颜色
