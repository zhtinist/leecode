"""
LeetCode #1774 - Closest Dessert Cost
中文题名：最接近目标价格的甜点成本
https://leetcode.com/problems/closest-dessert-cost/

You would like to make dessert and are preparing to buy the ingredients. You have `n` ice cream base flavors and `m` types of toppings to choose from. You must follow these rules when making your dessert:

There must be exactly one ice cream base.

You can add one or more types of topping or have no toppings at all.

There are at most two of each type of topping.

You are given three inputs:

`baseCosts`, an integer array of length `n`, where each `baseCosts[i]` represents the price of the `ith` ice cream base flavor.

`toppingCosts`, an integer array of length `m`, where each `toppingCosts[i]` is the price of one of the `ith` topping.

`target`, an integer representing your target price for dessert.

You want to make a dessert with a total cost as close to `target` as possible.

Return the closest possible cost of the dessert to `target`. If there are multiple, return the lower one.

Example 1:

Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
Output: 10
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 7
- Take 1 of topping 0: cost 1 x 3 = 3
- Take 0 of topping 1: cost 0 x 4 = 0
Total: 7 + 3 + 0 = 10.

Example 2:

Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
Output: 17
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 3
- Take 1 of topping 0: cost 1 x 4 = 4
- Take 2 of topping 1: cost 2 x 5 = 10
- Take 0 of topping 2: cost 0 x 100 = 0
Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.

Example 3:

Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
Output: 8
Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.

Example 4:

Input: baseCosts = [10], toppingCosts = [1], target = 1
Output: 10
Explanation: Notice that you don't have to have any toppings, but you must have exactly one base.

Constraints:

`n == baseCosts.length`

`m == toppingCosts.length`

`1 <= n, m <= 10`

`1 <= baseCosts[i], toppingCosts[i] <= 104`

`1 <= target <= 104`

【中文翻译】
给定 baseCosts 数组（基料价格）和 toppingCosts 数组（配料价格），以及目标价格 target。
制作甜点需要选择一种基料，然后可以选择每种配料 0、1 或 2 份。
求与 target 最接近的总成本。如果有多个相同接近的，返回较低的那个。

示例 1：
输入: baseCosts = [1,7], toppingCosts = [3,4], target = 10
输出: 10
解释: 基料7 + 配料3*1 = 10。基料1 + 配料3*2 + 配料4*1 = 1+6+4=11。最接近的是10和11...最小接近的是10。
"""

from typing import List, Optional


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.best = float('inf')

        def dfs(idx: int, cur_cost: int) -> None:
            # 更新最佳结果
            if abs(cur_cost - target) < abs(self.best - target):
                self.best = cur_cost
            elif abs(cur_cost - target) == abs(self.best - target) and cur_cost < self.best:
                self.best = cur_cost

            if idx == len(toppingCosts):
                return

            # 剪枝：如果当前成本已经远超 target 且比 best 差，可以跳过
            # 但这种剪枝不完全安全，因为后面还可能有更接近的

            # 三种选择：0份、1份、2份
            for times in range(3):
                dfs(idx + 1, cur_cost + toppingCosts[idx] * times)

        for base in baseCosts:
            dfs(0, base)

        return self.best
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 回溯/DFS。枚举所有基料，对每种基料递归尝试每种配料的 0/1/2 份选择。
# 维护全局最优值 best（与 target 最接近的成本，接近程度相同时取较小值）。
# toppingCosts 长度 <= 10，总状态数 = 3^10 = 59049，在可接受范围内。
#
# 时间复杂度: O(B * 3^T) — B 为基料数，T 为配料种类数
# 空间复杂度: O(T) — 递归栈深度
#
# 关键点:
# - 每种配料有 0/1/2 三种选择
# - 回溯遍历所有组合
# - 相同接近度取较小成本
