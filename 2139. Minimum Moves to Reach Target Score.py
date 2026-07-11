"""
LeetCode #2139 - Minimum Moves to Reach Target Score
得到目标值的最少行动次数
https://leetcode.cn/problems/minimum-moves-to-reach-target-score/

你正在玩一个整数游戏。从整数 `1` 开始，期望得到整数 `target` 。
在一次行动中，你可以做下述两种操作之一：
递增，将当前整数的值加 1（即， `x = x + 1`）。
加倍，使当前整数的值翻倍（即，`x = 2 * x`）。
在整个游戏过程中，你可以使用 递增 操作 任意 次数。但是只能使用 加倍 操作 至多 `maxDoubles` 次。
给你两个整数 `target` 和 `maxDoubles` ，返回从 1 开始得到 `target` 需要的最少行动次数。

示例 1：
输入：target = 5, maxDoubles = 0 输出：4 解释：一直递增 1 直到得到 target 。
示例 2：
输入：target = 19, maxDoubles = 2 输出：7 解释：最初，x = 1 。 递增 3 次，x = 4 。 加倍 1 次，x = 8 。 递增 1 次，x = 9 。 加倍 1 次，x = 18 。 递增 1 次，x = 19 。
示例 3：
输入：target = 10, maxDoubles = 4 输出：4 解释： 最初，x = 1 。  递增 1 次，x = 2 。  加倍 1 次，x = 4 。  递增 1 次，x = 5 。  加倍 1 次，x = 10 。

提示：
`1 <= target <= 10^9`
`0 <= maxDoubles <= 100`
"""

from typing import List, Optional


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 1:
                target -= 1
                moves += 1
            target //= 2
            moves += 1
            maxDoubles -= 1
        return moves + (target - 1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Math
#
# 解题思路:
# 贪心从 target 反向操作回到 1。加倍操作的收益在数值越大时越显著，因此逆向思考：
# 当 target 为偶数且有加倍次数剩余时，使用除以 2（反向加倍）比连续减 1 更优；
# 当 target 为奇数时，必须先减 1 使其变为偶数。循环直到 target 回到 1 或用完加倍次数，
# 剩余步数全部为减 1 操作，共需要 (target - 1) 步。
#
# 时间复杂度: O(log target)，每次循环 target 至少减半。
# 空间复杂度: O(1)，只使用常数级别的额外变量。
#
# 关键点:
# - 逆向贪心：从目标往起点反推，加倍操作的逆向是除以 2
# - 当 target 为奇数时必须先减到偶数才能除以 2
# - 最后剩余的 target-1 步全部是加 1 操作（正向）
