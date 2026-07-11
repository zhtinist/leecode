"""
LeetCode #688 - Knight Probability in Chessboard
中文题名：骑士在棋盘上的概率
https://leetcode.com/problems/knight-probability-in-chessboard/

On an `N`x`N` chessboard, a knight starts at the `r`-th row
and `c`-th column and attempts to make exactly `K` moves. The rows and
columns are 0 indexed, so the top-left square is `(0, 0)`, and the bottom-right
square is `(N-1, N-1)`.

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two
squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random
(even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly `K` moves or has moved off
the chessboard. Return the probability that the knight remains on the board after it has
stopped moving.

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Note:

`N` will be between 1 and 25.

`K` will be between 0 and 100.

The knight always initially starts on the board.

【中文翻译】
在一个 `N`x`N` 的棋盘上，骑士从第 `r` 行第 `c` 列开始，尝试进行恰好 `K` 次移动。行和列从 0 开始索引，因此左上角坐标为 `(0, 0)`，右下角坐标为 `(N-1, N-1)`。

国际象棋中的骑士有 8 种可能的移动方式，如下图所示。每次移动是在一个基本方向上走两格，然后在正交方向上走一格。

每次骑士要移动时，它会从 8 种可能的移动方式中均匀随机地选择一种（即使棋子会走出棋盘），然后移动到那里。

骑士会持续移动直到完成恰好 `K` 次移动或者已经移出棋盘。返回骑士在停止移动后仍然留在棋盘上的概率。

示例：

输入: 3, 2, 0, 0
输出: 0.0625
解释: 有两种走法（到 (1,2)、(2,1)）可以让骑士留在棋盘上。从这些位置出发，也分别有两种走法可以让骑士留在棋盘上。骑士留在棋盘上的总概率是 0.0625。

注意：

`N` 在 1 到 25 之间。

`K` 在 0 到 100 之间。

骑士始终从棋盘上出发。
"""

from typing import List, Optional


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]

        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            ndp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            ndp[nr][nc] += dp[r][c] / 8.0
            dp = ndp

        return sum(dp[r][c] for r in range(n) for c in range(n))









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划，dp[r][c] 表示经过当前步数后骑士在位置 (r, c) 的概率。
# 初始时 dp[row][column] = 1.0。
# 对于每一步，计算下一步的 ndp：
# - 对于每个有非零概率的位置，向 8 个方向各分配 1/8 的概率。
# - 只有落在棋盘内的移动才计入 ndp（移出棋盘的概率被丢弃）。
# 经过 K 步后，dp 中所有位置的概率之和即为留在棋盘上的总概率。
#
# 时间复杂度: O(K * N^2) - K 步，每步遍历棋盘
# 空间复杂度: O(N^2) - 两个 N*N 的 dp 数组
#
# 关键点:
# - 每次移动有 8 个方向，概率均分（1/8）
# - 走出棋盘的概率被视为"丢失"
# - 使用滚动数组（两个 dp）节省空间
# - 最终答案 = 所有位置概率之和
