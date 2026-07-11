"""
LeetCode #2240 - Number of Ways to Buy Pens and Pencils
买钢笔和铅笔的方案数
https://leetcode.cn/problems/number-of-ways-to-buy-pens-and-pencils/

给你一个整数 `total` ，表示你拥有的总钱数。同时给你两个整数 `cost1` 和 `cost2` ，分别表示一支钢笔和一支铅笔的价格。你可以花费你部分或者全部的钱，去买任意数目的两种笔。
请你返回购买钢笔和铅笔的 不同方案数目 。

示例 1：
输入：total = 20, cost1 = 10, cost2 = 5 输出：9 解释：一支钢笔的价格为 10 ，一支铅笔的价格为 5 。 - 如果你买 0 支钢笔，那么你可以买 0 ，1 ，2 ，3 或者 4 支铅笔。 - 如果你买 1 支钢笔，那么你可以买 0 ，1 或者 2 支铅笔。 - 如果你买 2 支钢笔，那么你没法买任何铅笔。 所以买钢笔和铅笔的总方案数为 5 + 3 + 1 = 9 种。
示例 2：
输入：total = 5, cost1 = 10, cost2 = 10 输出：1 解释：钢笔和铅笔的价格都为 10 ，都比拥有的钱数多，所以你没法购买任何文具。所以只有 1 种方案：买 0 支钢笔和 0 支铅笔。

提示：
`1 <= total, cost1, cost2 <= 10^6`
"""

from typing import List, Optional


class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        pens = 0
        # 枚举买 pens 支钢笔（0 到 total // cost1）
        while pens * cost1 <= total:
            remaining = total - pens * cost1
            ans += remaining // cost2 + 1  # 铅笔可选 0 到 remaining // cost2 支
            pens += 1
        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Enumeration
#
# 解题思路:
# 枚举购买钢笔的数量（0 到 total // cost1 支），对于每种钢笔数量，
# 剩下的钱可以买 0 到 remaining // cost2 支铅笔，共 (remaining // cost2 + 1) 种方案。
# 将所有钢笔数量对应的铅笔方案数累加即为总方案数。
# 注意：包括买 0 支钢笔 0 支铅笔这一种方案。
#
# 时间复杂度: O(total / cost1) 最坏 O(10^6)，cost1 最小为 1 时最多循环 10^6 次
# 空间复杂度: O(1) 只使用常量空间
#
# 关键点:
# - 每种钢笔数量下可买铅笔方案数为 remaining // cost2 + 1（+1 因为可以买 0 支）
# - 不要用 range(0, total + 1, cost1)，应逐个枚举钢笔支数（开销可控）
# - total, cost1, cost2 上限 10^6，最坏循环 10^6 次在 Python 中可通过
