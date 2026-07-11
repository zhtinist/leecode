"""
LeetCode #1140 - Stone Game II
中文题名：石子游戏 II
https://leetcode.com/problems/stone-game-ii/

Alex and Lee continue their games with piles of stones.  There are a number of piles arranged
in a row, and each pile has a positive integer number of
stones `piles[i]`.  The objective of the game is to end with the most stones.

Alex and Lee take turns, with Alex starting first.  Initially, `M = 1`.

On each player's turn, that player can take all the stones in the
first `X` remaining piles, where `1 <= X <= 2M`.
Then, we set `M = max(M, X)`.

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger.

Constraints:

`1 <= piles.length <= 100`

`1 <= piles[i] <= 10 ^ 4`

【中文翻译】
亚历克斯和李继续用石堆玩他们的游戏。有许多堆石子排成一行，每堆有正整数个石子 piles[i]。游戏的目标是在结束时拥有最多的石子。

亚历克斯和李轮流进行，亚历克斯先手。最初，M = 1。

在每个玩家的回合中，该玩家可以取走前 X 堆中剩余的所有石子，其中 1 <= X <= 2M。然后，我们令 M = max(M, X)。

游戏一直持续到所有石子都被取走。

假设亚历克斯和李都采取最优策略，返回亚历克斯最多可以获得的石子数量。

示例 1：

输入：piles = [2,7,9,4,4]
输出：10
解释：如果亚历克斯一开始取走一堆，李取走两堆，然后亚历克斯再取走两堆。亚历克斯总共可以获得 2 + 4 + 4 = 10 堆石子。如果亚历克斯一开始取走两堆，那么李可以取走剩下的全部三堆。这种情况下，亚历克斯获得 2 + 7 = 9 堆石子。所以返回 10，因为它更大。

约束条件：

`1 <= piles.length <= 100`

`1 <= piles[i] <= 10 ^ 4`
"""

from typing import List, Optional


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # suffixSum[i] = sum of piles[i:]
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]

        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            """
            Returns the maximum stones the current player can get
            starting from index i with current M = m.
            """
            if i >= n:
                return 0
            if i + 2 * m >= n:
                # Can take all remaining piles
                return suffix_sum[i]

            # Try taking X piles, where 1 <= X <= 2*m
            # The opponent will get dp(i+X, max(m, X))
            # So current player gets suffix_sum[i] - dp(i+X, max(m, X))
            best = 0
            for x in range(1, 2 * m + 1):
                opponent = dp(i + x, max(m, x))
                best = max(best, suffix_sum[i] - opponent)
            return best

        return dp(0, 1)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这是一道博弈论 + 动态规划问题。使用记忆化递归求解：
# 1. 首先计算后缀和数组 suffix_sum，suffix_sum[i] 表示从第 i 堆开始到末尾的石子总数。
# 2. 定义递归函数 dp(i, m)，表示当前玩家从第 i 堆开始取，且当前 M = m 时，能获得的最大石子数。
# 3. 边界条件：如果 i + 2*m >= n（可以取走剩余所有石子），直接返回 suffix_sum[i]。
# 4. 状态转移：当前玩家可以取 X 堆（1 <= X <= 2*m），取完后对手从 i+X 开始，
#    M 更新为 max(m, X)。对手获得 dp(i+X, max(m, X))，当前玩家从 i 开始到末尾
#    的总和为 suffix_sum[i]，所以当前玩家获得 suffix_sum[i] - dp(i+X, max(m, X))。
#    在所有可能的 X 中取最大值。
# 5. 使用 @lru_cache 进行记忆化，避免重复计算。
# 核心思想：当前玩家能获得的石子 = 剩余总石子 - 对手能获得的最多石子。
#
# 时间复杂度: O(n^3) - 状态数 O(n^2)，每个状态遍历 O(n) 种选择
# 空间复杂度: O(n^2) - 记忆化缓存和递归栈深度
#
# 关键点:
# - 后缀和数组用于快速获取剩余石子总数
# - 博弈论核心：当前最优 = 总量 - 对手最优
# - M 的上限分析：由于每次 X <= 2M，M 的增长是指数级的，实际状态数远小于 n^2
# - lru_cache 实现记忆化，避免手动管理 DP 表
