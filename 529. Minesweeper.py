"""
LeetCode #529 - Minesweeper
中文题名：扫雷游戏
https://leetcode.com/problems/minesweeper/

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an
unrevealed mine, 'E' represents an unrevealed empty square, 'B'
represents a revealed blank square that has no adjacent (above, below, left, right,
and all 4 diagonals) mines, digit ('1' to '8') represents how many
mines are adjacent to this revealed square, and finally 'X' represents
a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed
squares ('M' or 'E'), return the board after revealing this position
according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to
'X'.

If an empty square ('E') with no adjacent mines is revealed, then change
it to revealed blank ('B') and all of its adjacent unrevealed squares
should be revealed recursively.

If an empty square ('E') with at least one adjacent mine is revealed,
then change it to a digit ('1' to '8') representing the number of
adjacent mines.

Return the board when no more squares will be revealed.

Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
['E', 'E', 'M', 'E', 'E'],
['E', 'E', 'E', 'E', 'E'],
['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
['B', '1', 'M', '1', 'B'],
['B', '1', '1', '1', 'B'],
['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
['B', '1', 'M', '1', 'B'],
['B', '1', '1', '1', 'B'],
['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
['B', '1', 'X', '1', 'B'],
['B', '1', '1', '1', 'B'],
['B', 'B', 'B', 'B', 'B']]

Explanation:

Note:

The range of the input matrix's height and width is [1,50].

The click position will only be an unrevealed square ('M' or 'E'), which
also means the input board contains at least one clickable square.

The input board won't be a stage when game is over (some mines have been
revealed).

For simplicity, not mentioned rules should be ignored in this problem. For example, you
don't need to reveal all the unrevealed mines when the game is over, consider
any cases that you will win the game or flag any squares.

【中文翻译】
让我们玩扫雷游戏！给定一个 2D 字符矩阵表示游戏面板：
- 'M'：未挖出的地雷
- 'E'：未挖出的空格
- 'B'：已挖出的空白格（周围 8 个方向没有相邻地雷）
- 数字 '1'~'8'：已挖出的格子，表示周围相邻的地雷数量
- 'X'：已挖出的地雷

给定点击位置（行列索引），根据以下规则揭露该位置后返回面板：
1. 如果揭开地雷 ('M')，游戏结束，将其改为 'X'
2. 如果揭开一个没有相邻地雷的空格 ('E')，将其改为 'B'，并递归揭露所有相邻未揭露格子
3. 如果揭开有至少一个相邻地雷的空格 ('E')，将其改为数字 ('1'~'8') 表示相邻地雷数

返回不再有新格子被揭露时的面板状态。

示例 1：
    点击：[3,0]
    输出参见上方 Output（揭露大片空白区域并显示边缘数字）

示例 2：
    点击：[1,2]（点击地雷位置）
    输出参见上方 Output（地雷变为 'X'，游戏结束）

说明：面板高度和宽度范围 [1, 50]。点击位置始终是未揭露的格子 ('M' 或 'E')。
"""

from typing import List, Optional


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click[0], click[1]
        rows, cols = len(board), len(board[0])

        # Rule 1: If a mine is revealed, game over
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        # 8-directional neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1),           (0, 1),
                       (1, -1),  (1, 0),  (1, 1)]

        def count_adjacent_mines(x: int, y: int) -> int:
            """Count adjacent mines for position (x, y)."""
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'M':
                    count += 1
            return count

        def dfs(x: int, y: int) -> None:
            if not (0 <= x < rows and 0 <= y < cols):
                return
            if board[x][y] != 'E':
                return

            mines = count_adjacent_mines(x, y)
            if mines > 0:
                # Rule 3: Show digit and stop
                board[x][y] = str(mines)
            else:
                # Rule 2: Reveal as blank and recurse
                board[x][y] = 'B'
                for dx, dy in directions:
                    dfs(x + dx, y + dy)

        dfs(r, c)
        return board


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS 模拟扫雷点击逻辑。首先检查点击位置是否为地雷 ('M')，若是则改为 'X' 并返回。
# 否则从点击位置开始 DFS：统计当前格子 8 个方向上的地雷数量。若地雷数 > 0，将当前格设为
# 对应数字并停止递归；若地雷数 == 0，将当前格设为 'B' 并递归揭露所有 8 个相邻的未揭露格子。
# 已揭露的格子（非 'E'）直接跳过，避免无限递归。
#
# 时间复杂度: O(M * N) — 最坏情况揭露整个面板的所有格子
# 空间复杂度: O(M * N) — 递归栈最坏深度（整个面板都是空格）
#
# 关键点:
# - 统计 8 方向相邻地雷数量，不仅仅是上下左右
# - 只有当前格子地雷数为 0 时才递归展开；有数字则停止，模拟真实扫雷
# - 可以用 BFS 替代 DFS 避免递归栈溢出（虽然本题 M,N <= 50，DFS 足够）
