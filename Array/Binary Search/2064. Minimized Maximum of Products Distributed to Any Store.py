"""
LeetCode #2064 - Minimized Maximum of Products Distributed to Any Store
分配给商店的最多商品的最小值
https://leetcode.cn/problems/minimized-maximum-of-products-distributed-to-any-store/

给你一个整数 `n` ，表示有 `n` 间零售商店。总共有 `m` 种商品，每种商品的数目用一个下标从 0 开始的整数数组 `quantities` 表示，其中 `quantities[i]` 表示第 `i` 种商品的数目。
你需要将 所有商品 分配到零售商店，并遵守这些规则：
一间商店 至多 只能有 一种商品 ，但一间商店拥有的商品数目可以为 任意 件。
分配后，每间商店都会被分配一定数目的商品（可能为 `0` 件）。用 `x` 表示所有商店中分配商品数目的最大值，你希望 `x` 越小越好。也就是说，你想 最小化 分配给任意商店商品数目的 最大值 。
请你返回最小的可能的 `x` 。

示例 1：
输入：n = 6, quantities = [11,6] 输出：3 解释： 一种最优方案为： - 11 件种类为 0 的商品被分配到前 4 间商店，分配数目分别为：2，3，3，3 。 - 6 件种类为 1 的商品被分配到另外 2 间商店，分配数目分别为：3，3 。 分配给所有商店的最大商品数目为 max(2, 3, 3, 3, 3, 3) = 3 。
示例 2：
输入：n = 7, quantities = [15,10,10] 输出：5 解释：一种最优方案为： - 15 件种类为 0 的商品被分配到前 3 间商店，分配数目为：5，5，5 。 - 10 件种类为 1 的商品被分配到接下来 2 间商店，数目为：5，5 。 - 10 件种类为 2 的商品被分配到最后 2 间商店，数目为：5，5 。 分配给所有商店的最大商品数目为 max(5, 5, 5, 5, 5, 5, 5) = 5 。
示例 3：
输入：n = 1, quantities = [100000] 输出：100000 解释：唯一一种最优方案为： - 所有 100000 件商品 0 都分配到唯一的商店中。 分配给所有商店的最大商品数目为 max(100000) = 100000 。

提示：
`m == quantities.length`
`1 <= m <= n <= 10^5`
`1 <= quantities[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(x: int) -> bool:
            # Check if we can distribute all products such that no store gets more than x
            stores_needed = 0
            for q in quantities:
                stores_needed += (q + x - 1) // x  # ceil division
            return stores_needed <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1
        return left



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Binary Search
#
# 解题思路:
# 二分搜索答案x（每店最多分配的商品数）。对于给定的x，检查是否可行：
# 每种商品i需要ceil(quantities[i] / x)个商店来分配。
# 如果所有商品所需商店总数 <= n，则x可行，尝试更小；否则需要更大的x。
# 二分找到满足条件的最小x。
#
# 时间复杂度: O(m * log(max(quantities)))
# 空间复杂度: O(1)
#
# 关键点:
# - 二分搜索答案
# - 可行性判断：每种商品需要的商店数 = ceil(q / x)
# - 向上取整公式：(q + x - 1) // x
