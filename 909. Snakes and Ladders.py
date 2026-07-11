"""
LeetCode #909 - Snakes and Ladders
中文题名：蛇梯棋
https://leetcode.com/problems/snakes-and-ladders/

On an N x N `board`, the numbers from `1` to `N*N` are
written boustrophedonically starting from the bottom left of
the board, and alternating direction each row.  For example, for a 6 x 6
board, the numbers are written as follows:

You start on square `1` of the board (which is always in the last row and first
column).  Each move, starting from square `x`, consists of the following:

You choose a destination square `S` with number `x+1`, `x+2`,
`x+3`, `x+4`, `x+5`, or `x+6`, provided this number
is `<= N*N`.

(This choice simulates the result of a standard 6-sided die roll: ie., there are
always at most 6 destinations, regardless of the size of the
board.)

If `S` has a snake or ladder, you move to the destination of that snake
or ladder.  Otherwise, you move to `S`.

A board square on row `r` and column `c` has a "snake or
ladder" if `board[r][c] != -1`.  The destination of that snake or
ladder is `board[r][c]`.

Note that you only take a snake or ladder at most once per move: if the destination to a
snake or ladder is the start of another snake or ladder, you do not
continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first
move your destination square is `2`, then you finish your first move at `3`, because
you do not continue moving to `4`.)

Return the least number of moves required to reach square N*N.
If it is not possible, return `-1`.

Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.

Note:

`2 <= board.length = board[0].length <= 20`

`board[i][j]` is between `1` and `N*N` or is equal
to `-1`.

The board square with number `1` has no snake or ladder.

The board square with number `N*N` has no snake or ladder.

【中文翻译】
在一个 N x N 的棋盘 `board` 上，数字从 `1` 到 `N*N` 按照"牛耕式转行书写法"（Boustrophedon）从棋盘的左下角开始交替方向逐行编号。例如，对于一个 6 x 6 的棋盘，编号如下：

你从棋盘上的方格 `1`（位于最后一行、第一列）开始出发。每一轮，从方格 `x` 开始，执行以下操作：

你选择一个目标方格 `S`，其编号为 `x+1`、`x+2`、`x+3`、`x+4`、`x+5` 或 `x+6`，前提是该编号 `<= N*N`。

（这个选择模拟了标准六面骰子的结果：即无论棋盘大小，每轮最多有 6 个目的地。）

如果 `S` 上有蛇或梯子，你就移动到那条蛇或梯子的目的地。否则，你移动到 `S`。

在棋盘第 `r` 行、第 `c` 列的方格如果有"蛇或梯子"，则 `board[r][c] != -1`。那条蛇或梯子的目的地为 `board[r][c]`。

注意，你每回合最多只能经历一次蛇或梯子：如果蛇或梯子的目的地是另一条蛇或梯子的起点，你不会继续移动。（例如，如果棋盘为 `[[4,-1],[-1,3]]`，且你第一轮的目的地为 `2`，那么你将在 `3` 结束第一轮，因为不会继续移动到 `4`。）

返回到达方格 N*N 所需的最少移动次数。如果不可能，返回 `-1`。

示例 1：

输入：[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
输出：4
解释：
开始时你在方格 1 [第 5 行，第 0 列]。
你决定移动到方格 2，并必须通过梯子到达方格 15。
然后你决定移动到方格 17（第 3 行，第 5 列），并必须通过蛇到达方格 13。
然后你决定移动到方格 14，并必须通过梯子到达方格 35。
然后你决定移动到方格 36，游戏结束。
可以证明至少需要 4 次移动才能到达第 N*N 个方格，所以答案是 4。

"""

from typing import List, Optional


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque

        n = len(board)
        target = n * n

        # 将棋盘编号 s 转换为 (r, c) 坐标
        def get_pos(s: int):
            # s 从 1 开始编号
            quot, rem = divmod(s - 1, n)
            r = n - 1 - quot               # 行号从底部开始
            c = rem if quot % 2 == 0 else n - 1 - rem  # 偶数行正向，奇数行反向
            return r, c

        visited = [False] * (target + 1)
        q = deque([(1, 0)])  # (当前位置, 步数)
        visited[1] = True

        while q:
            curr, steps = q.popleft()

            if curr == target:
                return steps

            for dice in range(1, 7):
                nxt = curr + dice
                if nxt > target:
                    break

                r, c = get_pos(nxt)
                # 如果有蛇或梯子，跳转
                if board[r][c] != -1:
                    nxt = board[r][c]

                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, steps + 1))

        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# BFS 最短路径问题。将棋盘看作一个图，格子编号 1 到 N*N 为节点，骰子点数 1~6
# 决定邻接边（最多 6 条出边）。BFS 从 1 出发，首次到达 N*N 的步数即为最短步数。
#
# 关键细节：
# 1. 坐标转换：编号 s → (r, c)
#    - quot = (s-1) // n, rem = (s-1) % n
#    - r = n-1 - quot（从底部向上）
#    - c = rem if quot 为偶数 else n-1-rem（之字形）
# 2. 蛇/梯子跳转：若 board[r][c] != -1，直接跳转到目标编号（只跳一次）
# 3. visited 数组避免重复访问，且需要 N*N 大小
#
# 时间复杂度: O(N^2) — BFS 每个节点最多访问一次，每个节点最多扩展 6 个邻居
# 空间复杂度: O(N^2) — visited 数组和队列
#
# 关键点:
# - 坐标转换是最容易出错的部分，务必处理之字形排列
# - 蛇/梯子跳转只在一次移动中发生一次（跳完后不继续跳）
# - visited 数组记录的是"处理过的编号"，当蛇/梯子修改目标后更新 visited 到最终位置
