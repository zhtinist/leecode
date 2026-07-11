"""
LeetCode #2861 - Maximum Number of Alloys
最大合金数
https://leetcode.cn/problems/maximum-number-of-alloys/

假设你是一家合金制造公司的老板，你的公司使用多种金属来制造合金。现在共有 `n` 种不同类型的金属可以使用，并且你可以使用 `k` 台机器来制造合金。每台机器都需要特定数量的每种金属来创建合金。
对于第 `i` 台机器而言，创建合金需要 `composition[i][j]` 份 `j` 类型金属。最初，你拥有 `stock[x]` 份 `x` 类型金属，而每购入一份 `x` 类型金属需要花费 `cost[x]` 的金钱。
给你整数 `n`、`k`、`budget`，下标从 1 开始的二维数组 `composition`，两个下标从 1 开始的数组 `stock` 和 `cost`，请你在预算不超过 `budget` 金钱的前提下，最大化 公司制造合金的数量。
所有合金都需要由同一台机器制造。
返回公司可以制造的最大合金数。

示例 1：
输入：n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,0], cost = [1,2,3] 输出：2 解释：最优的方法是使用第 1 台机器来制造合金。 要想制造 2 份合金，我们需要购买： - 2 份第 1 类金属。 - 2 份第 2 类金属。 - 2 份第 3 类金属。 总共需要 2 * 1 + 2 * 2 + 2 * 3 = 12 的金钱，小于等于预算 15 。 注意，我们最开始时候没有任何一类金属，所以必须买齐所有需要的金属。 可以证明在示例条件下最多可以制造 2 份合金。
示例 2：
输入：n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3] 输出：5 解释：最优的方法是使用第 2 台机器来制造合金。  要想制造 5 份合金，我们需要购买：  - 5 份第 1 类金属。 - 5 份第 2 类金属。  - 0 份第 3 类金属。  总共需要 5 * 1 + 5 * 2 + 0 * 3 = 15 的金钱，小于等于预算 15 。  可以证明在示例条件下最多可以制造 5 份合金。
示例 3：
输入：n = 2, k = 3, budget = 10, composition = [[2,1],[1,2],[1,1]], stock = [1,1], cost = [5,5] 输出：2 解释：最优的方法是使用第 3 台机器来制造合金。 要想制造 2 份合金，我们需要购买： - 1 份第 1 类金属。 - 1 份第 2 类金属。 总共需要 1 * 5 + 1 * 5 = 10 的金钱，小于等于预算 10 。 可以证明在示例条件下最多可以制造 2 份合金。

提示：
`1 <= n, k <= 100`
`0 <= budget <= 10^8`
`composition.length == k`
`composition[i].length == n`
`1 <= composition[i][j] <= 100`
`stock.length == cost.length == n`
`0 <= stock[i] <= 10^8`
`1 <= cost[i] <= 100`
"""

from typing import List, Optional


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int,
                          composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:
        def can_make(machine_idx: int, cnt: int) -> bool:
            total = 0
            comp = composition[machine_idx]
            for j in range(n):
                need = comp[j] * cnt
                if need > stock[j]:
                    total += (need - stock[j]) * cost[j]
                    if total > budget:
                        return False
            return total <= budget

        ans = 0
        for i in range(k):
            lo, hi = 0, budget + max(stock) + 1  # upper bound
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if can_make(i, mid):
                    lo = mid
                else:
                    hi = mid - 1
            ans = max(ans, lo)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search
#
# 解题思路:
# 由于所有合金必须由同一台机器制造，枚举每台机器，对该机器二分查找最大可制造的合金数。
# 对于给定的合金数 x，计算需要的每种金属数量 = composition[j] * x，超出库存的部分按价格购买，
# 总花费不超过 budget 即表示可行。取所有机器的最大值。
#
# 时间复杂度: O(k * n * log(B)) 其中 B = budget + max(stock)
# 空间复杂度: O(1)
#
# 关键点:
# - 每台机器独立计算，使用二分查找最大化合金数
# - check 函数：计算制造 x 个合金所需额外购买金属的总花费
# - 上限可取 budget + sum(stock) + 1（极端情况）
