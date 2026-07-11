"""
LeetCode #1927 - Sum Game
求和游戏
https://leetcode.cn/problems/sum-game/

Alice 和 Bob 玩一个游戏，两人轮流行动，Alice 先手 。
给你一个 偶数长度 的字符串 `num` ，每一个字符为数字字符或者 `'?'` 。每一次操作中，如果 `num` 中至少有一个 `'?'` ，那么玩家可以执行以下操作：
选择一个下标 `i` 满足 `num[i] == '?'` 。
将 `num[i]` 用 `'0'` 到 `'9'` 之间的一个数字字符替代。
当 `num` 中没有 `'?'` 时，游戏结束。
Bob 获胜的条件是 `num` 中前一半数字的和 等于 后一半数字的和。Alice 获胜的条件是前一半的和与后一半的和 不相等 。
比方说，游戏结束时 `num = "243801"` ，那么 Bob 获胜，因为 `2+4+3 = 8+0+1` 。如果游戏结束时 `num = "243803"` ，那么 Alice 获胜，因为 `2+4+3 != 8+0+3` 。
在 Alice 和 Bob 都采取 最优 策略的前提下，如果 Alice 获胜，请返回 `true` ，如果 Bob 获胜，请返回 `false` 。

示例 1：
输入：num = "5023" 输出：false 解释：num 中没有 '?' ，没法进行任何操作。 前一半的和等于后一半的和：5 + 0 = 2 + 3 。
示例 2：
输入：num = "25??" 输出：true 解释：Alice 可以将两个 '?' 中的一个替换为 '9' ，Bob 无论如何都无法使前一半的和等于后一半的和。
示例 3：
输入：num = "?3295???" 输出：false 解释：Bob 总是能赢。一种可能的结果是： - Alice 将第一个 '?' 用 '9' 替换。num = "93295???" 。 - Bob 将后面一半中的一个 '?' 替换为 '9' 。num = "932959??" 。 - Alice 将后面一半中的一个 '?' 替换为 '2' 。num = "9329592?" 。 - Bob 将后面一半中最后一个 '?' 替换为 '7' 。num = "93295927" 。 Bob 获胜，因为 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7 。

提示：
`2 <= num.length <= 10^5`
`num.length` 是 偶数 。
`num` 只包含数字字符和 `'?'` 。
"""

from typing import List, Optional


class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        left_q = 0
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        right_sum = 0
        right_q = 0
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # The key insight: Bob wants to make left_sum + left_picks = right_sum + right_picks
        # Each player picks digits 0-9, but the game theory simplifies to:
        # Alice wins if she can force inequality

        # After optimal play, the difference in sums is:
        # diff = left_sum - right_sum + (left_q/2 * 9) - (right_q/2 * 9)
        # = left_sum - right_sum + 4.5 * (left_q - right_q)

        # Bob can only win if the equation can be balanced
        # For Bob to win: left_sum - right_sum + 4.5*(left_q - right_q) == 0
        # i.e., 2*(right_sum - left_sum) == 9*(left_q - right_q)

        # More precisely: each pair of '?' (one on left, one on right)
        # that Alice and Bob fill, Alice can make the sum differ by 9
        # if she plays opposite to Bob.

        # The condition for Bob to win:
        # Total question marks must be even (so equal turns)
        # And: right_sum - left_sum == 9 * (left_q - right_q) / 2

        total_q = left_q + right_q

        # After optimal play, the net effect of question marks:
        # Alice's advantage = 9 * (left_q - right_q) / 2
        # For Bob to tie: left_sum + 9 * left_q / 2 == right_sum + 9 * right_q / 2
        # Multiply by 2: 2*left_sum + 9*left_q == 2*right_sum + 9*right_q
        # Rearranged: 2*(right_sum - left_sum) == 9*(left_q - right_q)

        return 2 * (right_sum - left_sum) != 9 * (left_q - right_q)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Math, String, Game Theory
#
# 解题思路:
# 博弈论 + 数学分析。
# 1. 统计左半和右半的数字和以及问号数量。
# 2. Bob 的目标是让左右和相等。每个问号由玩家填入 0-9。
#    双方都最优时，Alice 填左边问号想让和不等，Bob 填右边问号想让和相等。
# 3. 数学推导：每对问号（左右各一个），最优博弈下 Alice 可以
#    让差值偏向自己 9（她填 9 在左边或 0 在右边）。
# 4. 平衡条件：2*(right_sum - left_sum) == 9*(left_q - right_q)
#    若满足则 Bob 能赢（返回 False），否则 Alice 赢（返回 True）。
#
# 时间复杂度: O(n) — 遍历字符串
# 空间复杂度: O(1) — 常数变量
#
# 关键点:
# - 博弈论简化：最优策略下每方的选择可以推导出统一条件
# - 每对问号（左边一个+右边一个），Alice 可以获得 9 的优势
# - 平衡等式是关键推导结果
# - Alice 先手有优势
