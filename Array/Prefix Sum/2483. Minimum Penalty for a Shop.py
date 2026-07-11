"""
LeetCode #2483 - Minimum Penalty for a Shop
商店的最少代价
https://leetcode.cn/problems/minimum-penalty-for-a-shop/

给你一个顾客访问商店的日志，用一个下标从 0 开始且只包含字符 `'N'` 和 `'Y'` 的字符串 `customers` 表示：
如果第 `i` 个字符是 `'Y'` ，它表示第 `i` 小时有顾客到达。
如果第 `i` 个字符是 `'N'` ，它表示第 `i` 小时没有顾客到达。
如果商店在第 `j` 小时关门（`0 <= j <= n`），代价按如下方式计算：
在开门期间，如果某一个小时没有顾客到达，代价增加 `1` 。
在关门期间，如果某一个小时有顾客到达，代价增加 `1` 。
请你返回在确保代价 最小 的前提下，商店的 最早 关门时间。
注意，商店在第 `j` 小时关门表示在第 `j` 小时以及之后商店处于关门状态。

示例 1：
输入：customers = "YYNY" 输出：2 解释： - 第 0 小时关门，总共 1+1+0+1 = 3 代价。 - 第 1 小时关门，总共 0+1+0+1 = 2 代价。 - 第 2 小时关门，总共 0+0+0+1 = 1 代价。 - 第 3 小时关门，总共 0+0+1+1 = 2 代价。 - 第 4 小时关门，总共 0+0+1+0 = 1 代价。 在第 2 或第 4 小时关门代价都最小。由于第 2 小时更早，所以最优关门时间是 2 。
示例 2：
输入：customers = "NNNNN" 输出：0 解释：最优关门时间是 0 ，因为自始至终没有顾客到达。
示例 3：
输入：customers = "YYYY" 输出：4 解释：最优关门时间是 4 ，因为每一小时均有顾客到达。

提示：
`1 <= customers.length <= 10^5`
`customers` 只包含字符 `'Y'` 和 `'N'` 。
"""

from typing import List, Optional


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        贪心 + 前缀思想：
        - 首先计算在 j=0 关门的代价 = 所有 'Y' 的数量（因为关门期间有顾客到达都要计罚）
        - 然后依次将关门时间 j 从 1 移到 n：
          如果前一小时 customers[j-1] == 'Y'，则该顾客不再算关门期间的罚金，penalty--
          如果前一小时 customers[j-1] == 'N'，则该小时变成开门期间无顾客，penalty++
        - 记录过程中最小的 penalty 和最早的下标
        """
        penalty = customers.count('Y')  # 在 j=0 关门时的代价
        min_penalty = penalty
        earliest = 0

        for j in range(1, len(customers) + 1):
            if customers[j - 1] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < min_penalty:
                min_penalty = penalty
                earliest = j

        return earliest



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Prefix Sum
#
# 解题思路:
# 采用贪心策略与滚动更新代价的方法。首先计算在时刻 0 关门的初始代价（即统计所有
# 'Y' 的个数，因为关门时段有顾客就会产生罚金）。然后从 j=1 到 j=n 逐步右移关门
# 时间：如果前一小时有顾客（'Y'），则该顾客从"关门时段"移到"开门时段"，代价减 1；
# 如果前一小时无顾客（'N'），则该小时进入开门时段但没有顾客，代价加 1。在遍历过
# 程中持续追踪最小代价及对应的最早下标。
#
# 时间复杂度: O(n) — 只需两次遍历（count + 一次扫描）
# 空间复杂度: O(1) — 仅使用常数个变量
#
# 关键点:
# - 关门时间取值范围是 [0, n]，即 n+1 种可能
# - 利用滚动更新避免重复计算前缀/后缀和
# - 只在 penalty < min_penalty 时更新，确保返回最早的最优关门时间
