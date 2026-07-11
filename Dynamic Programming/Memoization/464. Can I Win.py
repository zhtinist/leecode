"""
LeetCode #464 - Can I Win
中文题名：我能赢吗
https://leetcode.com/problems/can-i-win/

In the "100 game," two players take turns adding, to a running total, any integer from 1..10.
The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15
without replacement until they reach a total >= 100.

Given an integer `maxChoosableInteger` and another integer
`desiredTotal`, determine if the first player to move can force a win, assuming
both players play optimally.

You can always assume that `maxChoosableInteger` will not be larger than 20 and
`desiredTotal` will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

【中文翻译】
在 "100 游戏" 中，两人轮流从 1 到 10 中选整数加到累计总和上，首个使累计总和达到或超过 100 的
玩家获胜。如果修改规则：已选过的数字不能重复使用。例如，两人从 1..15 的公共数字池中轮流
不放回地选取，直到累计总和 >= 100。

给定 `maxChoosableInteger`（最大可选整数）和 `desiredTotal`（目标总和），判断先手玩家
能否必胜，假设双方均采取最优策略。可假设 maxChoosableInteger 不超过 20，
desiredTotal 不超过 300。

示例：
    输入：maxChoosableInteger = 10, desiredTotal = 11
    输出：false
    解释：无论先手选哪个整数都会输。先手选 1，后手选 10 立即达到 11 获胜；其他选择同理。
"""

from typing import List, Optional


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        Game theory with memoization + bitmask DP.
        Use a bitmask to track which numbers have been used, and
        recursively determine if the first player can force a win.
        """
        if desiredTotal <= 0:
            return True
        total = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if total < desiredTotal:
            return False

        memo = {}

        def dfs(used: int, remaining: int) -> bool:
            if remaining <= 0:
                return False  # opponent already reached the target on their turn
            if used in memo:
                return memo[used]

            for i in range(1, maxChoosableInteger + 1):
                mask = 1 << (i - 1)
                if used & mask:
                    continue  # number already used
                # Win immediately if we reach target, or opponent loses from new state
                if i >= remaining or not dfs(used | mask, remaining - i):
                    memo[used] = True
                    return True

            memo[used] = False
            return False

        return dfs(0, desiredTotal)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用带记忆化的博弈 DFS（状态压缩 DP）。用位掩码 (bitmask) 表示哪些数字已被选取，
# 递归判断在当前状态下先手是否能赢。对于每个可选数字 i：若选了 i 后直接达到
# desiredTotal 则立即获胜；否则若对手在新状态下必输，则我方获胜。使用 memo 字典
# 缓存已计算状态避免重复计算。两个边界提前判断：(1) desiredTotal <= 0 直接赢；
# (2) 所有可选数字之和 < desiredTotal 则无论如何都无法达到，直接输。
#
# 时间复杂度: O(2^M * M)，M = maxChoosableInteger ≤ 20，记忆化剪枝使实际开销远小于理论上限
# 空间复杂度: O(2^M) — memo 字典存储最多 2^M 个状态
#
# 关键点:
# - 位掩码压缩状态（used 的每一位表示对应数字是否已选）
# - 记忆化搜索避免重复子问题
# - 博弈关键：当前玩家赢 ⇔ 存在一步使对手面临必输状态
# - 边界条件：总和不足以达到目标时直接返回 False
