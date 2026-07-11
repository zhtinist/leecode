"""
LeetCode #877 - Stone Game
中文题名：石子游戏
https://leetcode.com/problems/stone-game/

Alex and Lee play a game with piles of stones.  There are an even number of piles
arranged in a row, and each pile has a positive integer number of stones
`piles[i]`.

The objective of the game is to end with the most stones.  The total number of
stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the
entire pile of stones from either the beginning or the end of the row.  This continues
until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return `True` if and only if Alex wins
the game.

Example 1:

Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

Note:

`2 <= piles.length <= 500`

`piles.length` is even.

`1 <= piles[i] <= 500`

`sum(piles)` is odd.

【中文翻译】
亚历克斯和李用几堆石子做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i]。
游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
亚历克斯和李轮流进行，亚历克斯先手。每回合，玩家从行的开始或结束处取走整堆石头。
这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true。

"""

from typing import List, Optional


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # 方法一：数学洞察 — 由于堆数是偶数，Alex 可以先手选策略获胜
        # Alex 可以将石子按奇偶索引分成两组：一组是偶数索引(0,2,4,...)，
        # 另一组是奇数索引(1,3,5,...)。因为 sum(piles) 是奇数，两组和不等。
        # Alex 先手可以选择总和更大的那组的所有石子。
        # 例如：Alex 第一手选 piles[0]，则 Lee 只能选 piles[1] 或 piles[n-1]，
        # 两者都是奇数索引。无论 Lee 选哪个，下一轮 Alex 仍能选偶数索引的堆。
        return True

        # 方法二：DP（通用解法，适用于非偶数堆的情况）
        # n = len(piles)
        # dp = [[0] * n for _ in range(n)]
        # # dp[i][j] = 当前玩家在先手面对 piles[i..j] 时的最大净胜分数
        # for i in range(n):
        #     dp[i][i] = piles[i]
        # for length in range(2, n + 1):
        #     for i in range(n - length + 1):
        #         j = i + length - 1
        #         dp[i][j] = max(piles[i] - dp[i + 1][j],
        #                        piles[j] - dp[i][j - 1])
        # return dp[0][n - 1] > 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 巧妙解法：由于 piles.length 是偶数，Alex 作为先手必胜。原因：将石子按索引奇偶分为两组。
# Alex 第一手可以选择 piles[0]（偶数索引组），此时剩余的堆 piles[1..n-1] 的两端分别是
# piles[1]（奇数索引）和 piles[n-1]（奇数索引，因为 n 为偶数时 n-1 为奇数）。
# 无论 Lee 选哪端，下一轮暴露给 Alex 的选项中至少有一个是偶数索引的堆。
# 因此 Alex 可以始终只选偶数索引的堆，同理也可以一开始选 piles[n-1] 从而只选奇数索引的堆。
# 因为 sum(piles) 是奇数，这两组的和必然不等，Alex 选较大的那组即可必胜。
#
# 时间复杂度: O(1)（数学解法）或 O(N^2)（DP 解法）
# 空间复杂度: O(1)（数学解法）或 O(N^2)（DP 解法）
#
# 关键点:
# - 偶数堆 + 先后手 = Alex 必胜的数学洞察
# - 石子按奇偶索引自然分为两组，先手可以控制始终取同一组
# - DP 通用解法：dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
