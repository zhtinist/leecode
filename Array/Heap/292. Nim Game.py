"""
LeetCode #292 - Nim Game
中文题名：Nim 游戏
https://leetcode.com/problems/nim-game/

You are playing the following Nim Game with your friend: There is a heap of stones on the
table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last
stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to
determine whether you can win the game given the number of stones in the heap.

Example:

Input: `4`
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
No matter 1, 2, or 3 stones you remove, the last stone will always be
removed by your friend.

【中文翻译】
你和你的朋友一起玩 Nim 游戏：桌子上有一堆石头，每次你们轮流拿掉 1 到 3 块石头。拿掉最后一块石头的人获胜。

你们都非常聪明，对游戏有最优策略。编写一个函数来判断，给定初始石头数，你是否能赢得游戏。

示例：

输入：`4`
输出：false
解释：如果堆中有 4 块石头，那么你永远不会赢得比赛；
无论你拿走 1、2 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
"""

from typing import List, Optional


class Solution:
    def canWinNim(self, n: int) -> bool:
        """Determine if you can win the Nim game given n stones.

        Mathematical insight: You lose if and only if n % 4 == 0.
        Because whatever you take (1-3), the opponent can always take
        enough to make the total removed 4, eventually leaving you with 4 stones.
        """
        return n % 4 != 0


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 数学推理。每次可以拿 1-3 颗石子。如果剩下的石子数是 4 的倍数，无论你拿几颗
# （1, 2, 或 3），对手都可以拿对应的数量使得你们两人这轮总共拿 4 颗，
# 从而使剩下的石子数仍然是 4 的倍数。最终你会面对 4 颗石子的局面，必输。
# 因此，初始石子数是 4 的倍数时先手必败，否则先手必胜（你可以先拿 n % 4 颗
# 来让对手面对 4 的倍数的局面）。
#
# 时间复杂度: O(1) - 一次取模运算
# 空间复杂度: O(1)
#
# 关键点:
# - 本质是 Bash Game（巴什博弈）的变体
# - 每次可取 1-3 颗，关键数字是 4 = (3+1)
# - 先手面对 4 的倍数必败
# - 直接返回 n % 4 != 0 即可
