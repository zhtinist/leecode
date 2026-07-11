"""
LeetCode #3387 - Maximize Amount After Two Days of Conversions
两天自由外汇交易后的最大货币数
https://leetcode.cn/problems/maximize-amount-after-two-days-of-conversions/

给你一个字符串 `initialCurrency`，表示初始货币类型，并且你一开始拥有 `1.0` 单位的 `initialCurrency`。
另给你四个数组，分别表示货币对（字符串）和汇率（实数）：
`pairs1[i] = [startCurrency_i, targetCurrency_i]` 表示在 第 1 天，可以按照汇率 `rates1[i]` 将 `startCurrency_i` 转换为 `targetCurrency_i`。
`pairs2[i] = [startCurrency_i, targetCurrency_i]` 表示在 第 2 天，可以按照汇率 `rates2[i]` 将 `startCurrency_i` 转换为 `targetCurrency_i`。
此外，每种 `targetCurrency` 都可以以汇率 `1 / rate` 转换回对应的 `startCurrency`。
你可以在 第 1 天 使用 `rates1` 进行任意次数的兑换（包括 0 次），然后在 第 2 天 使用 `rates2` 再进行任意次数的兑换（包括 0 次）。
返回在两天兑换后，最大可能拥有的 `initialCurrency` 的数量。
注意：汇率是有效的，并且第 1 天和第 2 天的汇率之间相互独立，不会产生矛盾。

示例 1：

输入： initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]
输出： 720.00000
解释：
根据题目要求，需要最大化最终的 EUR 数量，从 1.0 EUR 开始：
第 1 天：
将 EUR 换成 USD，得到 2.0 USD。
将 USD 换成 JPY，得到 6.0 JPY。
第 2 天：
将 JPY 换成 USD，得到 24.0 USD。
将 USD 换成 CHF，得到 120.0 CHF。
最后将 CHF 换回 EUR，得到 720.0 EUR。
示例 2：

输入： initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0]
输出： 1.50000
解释：
在第 1 天将 NGN 换成 EUR，并在第 2 天用反向汇率将 EUR 换回 NGN，可以最大化最终的 NGN 数量。
示例 3：

输入： initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]
输出： 1.00000
解释：
在这个例子中，不需要在任何一天进行任何兑换。

提示：
`1 <= initialCurrency.length <= 3`
`initialCurrency` 仅由大写英文字母组成。
`1 <= n == pairs1.length <= 10`
`1 <= m == pairs2.length <= 10`
`pairs1[i] == [startCurrency_i, targetCurrency_i]`
`pairs2[i] == [startCurrency_i, targetCurrency_i]`
`1 <= startCurrency_i.length, targetCurrency_i.length <= 3`
`startCurrency_i` 和 `targetCurrency_i` 仅由大写英文字母组成。
`rates1.length == n`
`rates2.length == m`
`1.0 <= rates1[i], rates2[i] <= 10.0`
输入保证两个转换图在各自的天数中没有矛盾或循环。
输入保证输出 最大 为 `5 * 10^10`。
"""

from typing import List, Optional


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float],
                  pairs2: List[List[str]], rates2: List[float]) -> float:
        from collections import defaultdict

        def max_values(pairs, rates, start_currency, start_val):
            graph = defaultdict(list)
            all_currencies = set()
            for (a, b), rate in zip(pairs, rates):
                graph[a].append((b, rate))
                graph[b].append((a, 1.0 / rate))
                all_currencies.add(a)
                all_currencies.add(b)

            values = defaultdict(float)
            values[start_currency] = start_val

            # Bellman-Ford style relaxation
            nodes = list(all_currencies)
            if start_currency not in nodes:
                nodes.append(start_currency)
            for _ in range(len(nodes)):
                updated = False
                for u in list(values.keys()):
                    for v, rate in graph[u]:
                        if values[u] * rate > values[v]:
                            values[v] = values[u] * rate
                            updated = True
                if not updated:
                    break
            return values

        day1_vals = max_values(pairs1, rates1, initialCurrency, 1.0)
        best = 0.0
        for curr, val in day1_vals.items():
            day2_vals = max_values(pairs2, rates2, curr, val)
            if initialCurrency in day2_vals:
                best = max(best, day2_vals[initialCurrency])
        return best



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Graph, Array, String
#
# 解题思路:
# 两天相互独立，第一天从initialCurrency开始最大化各货币数量，第二天用第一天的结果继续最大化。
# 每天使用Bellman-Ford风格的松弛操作：遍历所有边，更新目标货币的最大值。
# 由于图无环（题目保证），多次松弛后收敛。最后取所有可能起始货币中能换回initialCurrency的最大值。
#
# 时间复杂度: O((n1+m1)*(V1+E1) + V1*(n2+m2)*(V2+E2))，其中V,E很小（<=20）
# 空间复杂度: O(V)
#
# 关键点:
# - 两天独立处理，第二天以第一天结果作为起始
# - 需要尝试每种货币作为第二天起点
# - 可以反向兑换（1/rate）
