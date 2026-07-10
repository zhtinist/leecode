"""
LeetCode #289 - Game of Life
https://leetcode.com/problems/game-of-life/

According to the Wikipedia's article: "The Game of
Life, also known simply as Life, is a cellular automaton devised by the British
mathematician John Horton Conway in 1970."

Given a *board* with *m* by *n* cells, each cell has an initial state
*live* (1) or *dead* (0). Each cell interacts with its eight
neighbors (horizontal, vertical, diagonal) using the following four rules (taken
from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by
under-population.

Any live cell with two or three live neighbors lives on to the next generation.

Any live cell with more than three live neighbors dies, as if by over-population..

Any dead cell with exactly three live neighbors becomes a live cell, as if by
reproduction.

Write a function to compute the next state (after one update) of the board given its current
state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
[0,1,0],
[0,0,1],
[1,1,1],
[0,0,0]
]
Output:
[
[0,0,0],
[1,0,1],
[0,1,1],
[0,1,0]
]

Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same
time: You cannot update some cells first and then use their updated values to update
other cells.

In this question, we represent the board using a 2D array. In principle, the board is
infinite, which would cause problems when the active area encroaches the border of the
array. How would you address these problems?
"""

from typing import List, Optional


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """Compute the next state of the Game of Life in-place.

        Use state encoding to update in-place without extra space:
        - 0: dead -> dead (00)
        - 1: live -> live (01)
        - 2: live -> dead (10) - was live, becomes dead
        - 3: dead -> live (11) - was dead, becomes live

        After computing next state for all cells, decode: new_state = state >> 1
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        for i in range(m):
            for j in range(n):
                # Count live neighbors (original state: 1 or 2 means was live)
                live_neighbors = 0
                for dr, dc in directions:
                    r, c = i + dr, j + dc
                    if 0 <= r < m and 0 <= c < n:
                        if board[r][c] == 1 or board[r][c] == 2:
                            live_neighbors += 1

                # Apply rules
                if board[i][j] == 1:  # currently live
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # live -> dead
                    # else: stays 1 (live -> live)
                else:  # currently dead
                    if live_neighbors == 3:
                        board[i][j] = 3  # dead -> live
                    # else: stays 0 (dead -> dead)

        # Decode: 0->0, 1->1, 2->0, 3->1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用状态编码实现原地更新。由于需要同时更新所有细胞（使用原始状态判断邻居），
# 不能直接修改原始值。解决方案是用额外的 bit 位来编码下一个状态：
# - 0 (00): 死 -> 死
# - 1 (01): 活 -> 活
# - 2 (10): 活 -> 死
# - 3 (11): 死 -> 活
# 判断邻居死活时检查状态是否为 1 或 2（原始是活的）。
# 第一遍遍历计算所有细胞的下一状态并编码。
# 第二遍遍历将编码解码为最终的 0/1（除以 2 或右移一位）。
#
# 时间复杂度: O(M * N) - 两遍遍历
# 空间复杂度: O(1) - 原地操作，不使用额外矩阵
#
# 关键点:
# - 状态编码用两个 bit 表示：低位是当前状态，高位是下一状态
# - 判断邻居原始状态：board[r][c] == 1 or board[r][c] == 2
# - 解码：2 -> 0, 3 -> 1（或 board[i][j] >>= 1）
# - 四条规则转化为条件判断即可
