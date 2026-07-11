"""
LeetCode #1648 - Sell Diminishing-Valued Colored Balls
中文题名：销售价值减少的颜色球
https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

You have an `inventory` of different colored balls, and there is a
customer that wants `orders` balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the
number of balls of that color you currently have in your
`inventory`. For example, if you own `6` yellow balls, the
customer would pay `6` for the first yellow ball. After the transaction,
there are only `5` yellow balls left, so the next yellow ball is then
valued at `5` (i.e., the value of the balls decreases as you sell more to
the customer).

You are given an integer array, `inventory`, where
`inventory[i]` represents the number of balls of the `ith`
color that you initially own. You are also given an integer `orders`,
which represents the total number of balls that the customer wants. You can sell the
balls in any order.

Return the maximum total value that you can attain after selling
`orders` colored balls. As the answer may be too large, return
it modulo `109 + 7`.

Example 1:

Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.

Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.

Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110

Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.

Constraints:

`1 <= inventory.length <= 105`

`1 <= inventory[i] <= 109`

`1 <= orders <= min(sum(inventory[i]), 109)`

【中文翻译】
给定 inventory 数组表示每种颜色的球的数量，以及 orders 表示顾客订单数量。
每个球的价值等于当前该颜色球的数量（即价值会随着售出而递减）。
每次卖出一个球后，该颜色球数量减1。求出售 orders 个球能获得的最大总价值，结果对 10^9+7 取模。

示例 1：
输入: inventory = [2,5], orders = 4
输出: 14
解释: 卖出顺序：价值5的球(剩4)，价值4的球(剩3)，价值3的球(剩2)，价值2(另一种)的球(剩1)。总和=5+4+3+2=14。
"""

from typing import List, Optional


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10 ** 9 + 7

        inventory.sort(reverse=True)
        inventory.append(0)
        n = len(inventory)
        ans = 0

        for i in range(n - 1):
            width = i + 1
            diff = inventory[i] - inventory[i + 1]
            total_balls = width * diff

            if orders >= total_balls:
                low, high = inventory[i + 1], inventory[i]
                ans = (ans + width * (high + low + 1) * (high - low) // 2) % MOD
                orders -= total_balls
            else:
                full_layers = orders // width
                remainder = orders % width
                low = inventory[i] - full_layers
                high = inventory[i]
                ans = (ans + width * (high + low + 1) * (high - low) // 2) % MOD
                ans = (ans + remainder * low) % MOD
                break

        return ans % MOD
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略：每次卖出当前数量最多的那种颜色的球。将 inventory 排序后从大到小处理。
# 使用分层方法：将 inventory[i] 到 inventory[i+1] 之间的值视为一层一层的矩形。
# 每层有 (i+1) 个球（前i+1种颜色都达到这个高度）。逐层卖出，直到满足 orders。
#
# 时间复杂度: O(N log N) — 排序
# 空间复杂度: O(1)
#
# 关键点:
# - 等差数列求和公式计算每层贡献
# - 分层处理避免逐个球模拟
# - MOD 取模注意使用 // 整除
