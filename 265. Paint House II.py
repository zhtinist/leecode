"""
LeetCode #265 - Paint House II
https://leetcode.com/problems/paint-house-ii/

There are a row of *n* houses, each house can be painted with one of the *k*
colors. The cost of painting each house with a certain color is different. You have to paint
all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a `*n* x *k*`
cost matrix. For example, `costs[0][0]` is the cost of painting house 0 with
color 0; `costs[1][2]` is the cost of painting house 1 with color 2, and so on...
Find the minimum cost to paint all houses.

Note:

All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

Follow up:

Could you solve it in *O*(*nk*) runtime?
"""

from typing import List, Optional


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0

        n = len(costs)
        k = len(costs[0])

        # 记录前一行的最小花费和次小花费及其颜色索引
        # 这样可以在 O(k) 时间内找到当前行每种颜色的最优前驱
        prev_min_cost = 0
        prev_second_min_cost = 0
        prev_min_color = -1

        for i in range(n):
            cur_min_cost = float('inf')
            cur_second_min_cost = float('inf')
            cur_min_color = -1

            for j in range(k):
                # 选择前一行的最优颜色（如果 j 与前一行的 min_color 不同，直接取 min_cost；否则取 second_min_cost）
                prev_best = prev_min_cost if j != prev_min_color else prev_second_min_cost
                cur_cost = costs[i][j] + prev_best

                # 更新当前行的最小和次小
                if cur_cost < cur_min_cost:
                    cur_second_min_cost = cur_min_cost
                    cur_min_cost = cur_cost
                    cur_min_color = j
                elif cur_cost < cur_second_min_cost:
                    cur_second_min_cost = cur_cost

            prev_min_cost = cur_min_cost
            prev_second_min_cost = cur_second_min_cost
            prev_min_color = cur_min_color

        return prev_min_cost


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: Yes
#
# 解题思路：
# 这是 #256 的泛化版本（k 种颜色而非 3 种）。如果按照 #256 的方法对每个颜色
# 遍历 k-1 种其他颜色，复杂度为 O(n*k^2)。优化方法：对于每一行，只需要知道
# 前一行最小值和次小值对应的花费及其颜色索引。当前房子刷颜色 j 时：
# - 若 j != prev_min_color，则用 prev_min_cost
# - 若 j == prev_min_color，则用 prev_second_min_cost
# 这样每行只需 O(k) 时间。
#
# 时间复杂度: O(n*k)
# 空间复杂度: O(1) — 只维护最小/次小值
#
# 关键点：
# - 维护前一行的最小和次小花费及其颜色索引
# - 相邻不能同色：用次小值替代最小值
# - 初始 prev_min_cost 和 prev_second_min_cost 为 0
