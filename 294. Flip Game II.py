"""
LeetCode #294 - Flip Game II
中文题名：翻转游戏 II
https://leetcode.com/problems/flip-game-ii/

You are playing the following Flip Game with your friend: Given a string that contains only
these two characters: `+` and `-`, you and your friend take turns to
flip two consecutive `"++"` into `"--"`.
The game ends when a person can no longer make a move and therefore the other person will be
the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: `s = "++++"`
Output: true
Explanation: The starting player can guarantee a win by flipping the middle `"++"` to become `"+--+"`.

Follow up:

Derive your algorithm's runtime complexity.

【中文翻译】
你和你的朋友正在玩以下翻转游戏：给定一个只包含 `+` 和 `-` 两种字符的字符串，你和你的朋友轮流将两个连续的 `"++"` 翻转为 `"--"`。
当某人无法再进行移动时，游戏结束，另一人获胜。

编写一个函数，判断先手玩家是否能保证获胜。

示例：

输入：`s = "++++"`
输出：true
解释：先手玩家可以通过将中间的 `"++"` 翻转为 `"+--+"` 来保证获胜。

进阶：

推导你的算法的时间复杂度。
"""

from typing import List, Optional


class Solution:
    def canWin(self, s: str) -> bool:
        """Determine if the starting player can guarantee a win.

        Game theory with memoization: a player can win if there exists a move
        such that after making it, the opponent CANNOT win.
        For each "++", flip it and recursively check if opponent loses.
        Memoize results for each state string.
        """
        memo = {}

        def dfs(state: str) -> bool:
            if state in memo:
                return memo[state]

            # Try every possible move
            for i in range(len(state) - 1):
                if state[i] == '+' and state[i + 1] == '+':
                    # Make the move
                    next_state = state[:i] + "--" + state[i + 2:]
                    # If opponent cannot win from next_state, I win
                    if not dfs(next_state):
                        memo[state] = True
                        return True

            memo[state] = False
            return False

        return dfs(s)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 博弈论 + 记忆化搜索（Memoization）。对于当前状态，先手玩家能赢的条件是：
# 存在一种合法的翻转操作，使得翻转后对手无法赢。
# 因此，对每个状态，尝试所有可能的 "++" 翻转为 "--" 的操作。对每种翻转后的
# 新状态递归调用，如果任何一种翻转使得对手在新状态下为 "cannot win"，
# 则当前玩家获胜。使用 memo 字典缓存每个状态的结果，避免重复计算。
#
# 时间复杂度: O(N * 2^(N/2)) - 最坏情况无剪枝，但有记忆化优化
#   实际远小于此，因为很多状态会被缓存
# 空间复杂度: O(2^(N/2)) - memo 存储所有可能状态
#
# 关键点:
# - 博弈论核心：我能赢 = 存在一种走法使得对手不能赢
# - 记忆化搜索是必须的，否则会 TLE
# - 递归状态转移：翻转 "++" -> "--"
# - 可以进一步优化：使用 Sprague-Grundy 定理将游戏分解为独立子游戏
