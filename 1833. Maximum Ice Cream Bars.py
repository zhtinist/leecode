"""
LeetCode #1833 - Maximum Ice Cream Bars
中文题名：购买冰淇淋的最大数量
https://leetcode.com/problems/maximum-ice-cream-bars/

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are `n` ice cream bars. You are given an array `costs` of length `n`, where `costs[i]` is the price of the `ith` ice cream bar in coins. The boy initially has `coins` coins to spend, and he wants to buy as many ice cream bars as possible.

Return the maximum number of ice cream bars the boy can buy with `coins` coins.

Note: The boy can buy the ice cream bars in any order.

Example 1:

Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

Example 2:

Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.

Example 3:

Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

Constraints:

`costs.length == n`

`1 <= n <= 105`

`1 <= costs[i] <= 105`

`1 <= coins <= 108`

【中文翻译】

炎热的夏天，一个男孩想买一些冰淇淋。商店里有n个冰淇淋，给定数组 `costs`，`costs[i]` 是第i个冰淇淋的价格。男孩最初有 `coins` 个硬币，他想买尽可能多的冰淇淋。返回男孩用 `coins` 个硬币最多可以购买的冰淇淋数量。

注意：男孩可以按任意顺序购买冰淇淋。

示例：
输入：costs = [1,3,2,4,1], coins = 7
输出：4
解释：可以买索引0,1,2,4的冰淇淋，总价1+3+2+1=7。

"""

from typing import List, Optional


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break
        return count










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略。要买最多数量的冰淇淋，应该优先买最便宜的。
# 将costs数组升序排序，从最便宜的冰淇淋开始购买，
# 只要当前硬币数大于等于价格就买下，硬币减少，计数加1。
# 当硬币不够买下一个时停止。
#
# 时间复杂度: O(N log N)，排序开销
# 空间复杂度: O(1)，原地排序（或O(log N)排序递归栈）
#
# 关键点:
# - 贪心选择最便宜的冰淇淋是最优策略
# - 排序后按顺序购买
