"""
LeetCode #2087 - Minimum Cost Homecoming of a Robot in a Grid
网格图中机器人回家的最小代价
https://leetcode.cn/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

给你一个 `m x n` 的网格图，其中 `(0, 0)` 是最左上角的格子，`(m - 1, n - 1)` 是最右下角的格子。给你一个整数数组 `startPos` ，`startPos = [start_row, start_col]` 表示 初始 有一个 机器人 在格子 `(start_row, start_col)` 处。同时给你一个整数数组 `homePos` ，`homePos = [home_row, home_col]` 表示机器人的 家 在格子 `(home_row, home_col)` 处。
机器人需要回家。每一步它可以往四个方向移动：上，下，左，右，同时机器人不能移出边界。每一步移动都有一定代价。再给你两个下标从 0 开始的整数数组：长度为 `m` 的数组 `rowCosts`  和长度为 `n` 的数组 `colCosts` 。
如果机器人往 上 或者往 下 移动到第 `r` 行 的格子，那么代价为 `rowCosts[r]` 。
如果机器人往 左 或者往 右 移动到第 `c` 列 的格子，那么代价为 `colCosts[c]` 。
请你返回机器人回家需要的 最小总代价 。

示例 1：

输入：startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7] 输出：18 解释：一个最优路径为： 从 (1, 0) 开始 -> 往下走到 (2, 0) 。代价为 rowCosts[2] = 3 。 -> 往右走到 (2, 1) 。代价为 colCosts[1] = 2 。 -> 往右走到 (2, 2) 。代价为 colCosts[2] = 6 。 -> 往右走到 (2, 3) 。代价为 colCosts[3] = 7 。 总代价为 3 + 2 + 6 + 7 = 18
示例 2：
输入：startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26] 输出：0 解释：机器人已经在家了，所以不需要移动。总代价为 0 。

提示：
`m == rowCosts.length`
`n == colCosts.length`
`1 <= m, n <= 10^5`
`0 <= rowCosts[r], colCosts[c] <= 10^4`
`startPos.length == 2`
`homePos.length == 2`
`0 <= start_row, home_row < m`
`0 <= start_col, home_col < n`
"""

from typing import List, Optional


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        r1, c1 = startPos
        r2, c2 = homePos
        total = 0

        # Move vertically
        if r1 <= r2:
            for r in range(r1 + 1, r2 + 1):
                total += rowCosts[r]
        else:
            for r in range(r1 - 1, r2 - 1, -1):
                total += rowCosts[r]

        # Move horizontally
        if c1 <= c2:
            for c in range(c1 + 1, c2 + 1):
                total += colCosts[c]
        else:
            for c in range(c1 - 1, c2 - 1, -1):
                total += colCosts[c]

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 由于所有移动代价都是正数，绕路只会增加代价，所以最优路径就是直接走向目标。
# 分别从行和列方向计算代价：行的移动代价取决于目标行号，列的移动代价取决于目标列号。
# 从start到home，每走一步都加上目标格子的行/列代价。
#
# 时间复杂度: O(|r2-r1| + |c2-c1|)
# 空间复杂度: O(1)
#
# 关键点:
# - 所有代价为正，不存在绕路收益
# - 直接移动是最优解
# - 分别计算行和列的代价
