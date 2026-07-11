"""
LeetCode #3021 - Alice and Bob Playing Flower Game
Alice 和 Bob 玩鲜花游戏
https://leetcode.cn/problems/alice-and-bob-playing-flower-game/

Alice 和 Bob 在一片田野上玩一个回合制游戏，他们之间有两排花。Alice 和 Bob 之间第一排有 `x` 朵花，第二排有 `y` 朵花。

游戏过程如下：
Alice 先行动。
每一次行动中，当前玩家必须选择其中一排，然后在这边摘一朵鲜花。
一次行动结束后，如果两排上都没有剩下鲜花，那么 当前 玩家抓住对手并赢得游戏的胜利。
给你两个整数 `n` 和 `m` ，你的任务是求出满足以下条件的所有 `(x, y)` 对：
按照上述规则，Alice 必须赢得游戏。
第一排的鲜花数目 `x` 必须在区间 `[1,n]` 之间。
第二排的鲜花数目 `y` 必须在区间 `[1,m]` 之间。
请你返回满足题目描述的数对 `(x, y)` 的数目。

示例 1：
输入：n = 3, m = 2 输出：3 解释：以下数对满足题目要求：(1,2) ，(3,2) ，(2,1) 。
示例 2：
输入：n = 1, m = 1 输出：0 解释：没有数对满足题目要求。

提示：
`1 <= n, m <= 10^5`
"""

from typing import List, Optional


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        Alice wins if total moves (x + y) is odd (Alice makes the last move).
        Count pairs (x, y) where x in [1,n], y in [1,m] and x+y is odd.
        """
        odd_n = (n + 1) // 2
        even_n = n // 2
        odd_m = (m + 1) // 2
        even_m = m // 2

        # Odd sum: odd_x + even_y, or even_x + odd_y
        return odd_n * even_m + even_n * odd_m



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math
#
# 解题思路:
# 每次操作摘一朵花，总操作次数为 x + y。Alice 先手，最后摘花的人获胜。
# 因此 Alice 获胜当且仅当总操作次数为奇数（Alice 做第 1,3,5,...,x+y 次操作）。
# x+y 为奇数等价于 x 和 y 一奇一偶。分别统计 [1,n] 和 [1,m] 中奇数和偶数的数量，相乘相加。
#
# 时间复杂度: O(1)，常数计算
# 空间复杂度: O(1)
#
# 关键点:
# - 这是一个取子游戏的特例（每次只能取 1 个），总步数决定胜负
# - 先手胜当且仅当 x+y 为奇数
# - 只需计算奇偶组合数：(奇x × 偶y) + (偶x × 奇y)
