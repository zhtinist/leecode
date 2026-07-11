"""
LeetCode #1801 - Number of Orders in the Backlog
中文题名：积压订单中的订单总数
https://leetcode.com/problems/number-of-orders-in-the-backlog/

You are given a 2D integer array `orders`, where each `orders[i] = [pricei, amounti, orderTypei]` denotes that `amounti` orders have been placed of type `orderTypei` at the price `pricei`. The `orderTypei` is:

`0` if it is a batch of `buy` orders, or

`1` if it is a batch of `sell` orders.

Note that `orders[i]` represents a batch of `amounti` independent orders with the same price and order type. All orders represented by `orders[i]` will be placed before all orders represented by `orders[i+1]` for all valid `i`.

There is a backlog that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:

If the order is a `buy` order, you look at the `sell` order with the smallest price in the backlog. If that `sell` order's price is smaller than or equal to the current `buy` order's price, they will match and be executed, and that `sell` order will be removed from the backlog. Else, the `buy` order is added to the backlog.

Vice versa, if the order is a `sell` order, you look at the `buy` order with the largest price in the backlog. If that `buy` order's price is larger than or equal to the current `sell` order's price, they will match and be executed, and that `buy` order will be removed from the backlog. Else, the `sell` order is added to the backlog.

Return the total amount of orders in the backlog after placing all the orders from the input. Since this number can be large, return it modulo `109 + 7`.

Example 1:

Input: orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
Output: 6
Explanation: Here is what happens with the orders:
- 5 orders of type buy with price 10 are placed. There are no sell orders, so the 5 orders are added to the backlog.
- 2 orders of type sell with price 15 are placed. There are no buy orders with prices larger than or equal to 15, so the 2 orders are added to the backlog.
- 1 order of type sell with price 25 is placed. There are no buy orders with prices larger than or equal to 25 in the backlog, so this order is added to the backlog.
- 4 orders of type buy with price 30 are placed. The first 2 orders are matched with the 2 sell orders of the least price, which is 15 and these 2 sell orders are removed from the backlog. The 3rd order is matched with the sell order of the least price, which is 25 and this sell order is removed from the backlog. Then, there are no more sell orders in the backlog, so the 4th order is added to the backlog.
Finally, the backlog has 5 buy orders with price 10, and 1 buy order with price 30. So the total number of orders in the backlog is 6.

Example 2:

Input: orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
Output: 999999984
Explanation: Here is what happens with the orders:
- 109 orders of type sell with price 7 are placed. There are no buy orders, so the 109 orders are added to the backlog.
- 3 orders of type buy with price 15 are placed. They are matched with the 3 sell orders with the least price which is 7, and those 3 sell orders are removed from the backlog.
- 999999995 orders of type buy with price 5 are placed. The least price of a sell order is 7, so the 999999995 orders are added to the backlog.
- 1 order of type sell with price 5 is placed. It is matched with the buy order of the highest price, which is 5, and that buy order is removed from the backlog.
Finally, the backlog has (1000000000-3) sell orders with price 7, and (999999995-1) buy orders with price 5. So the total number of orders = 1999999991, which is equal to 999999984 % (109 + 7).

Constraints:

`1 <= orders.length <= 105`

`orders[i].length == 3`

`1 <= pricei, amounti <= 109`

`orderTypei` is either `0` or `1`.

【中文翻译】
给定订单数组 orders，orders[i] = [price, amount, orderType]。
orderType = 0 表示买单（愿意用 <= price 的价格购买），1 表示卖单（愿意用 >= price 的价格出售）。
如果存在匹配的买卖单（买入价 >= 卖出价），执行交易并移除订单。
返回积压订单中未执行订单的总数，对 10^9+7 取模。

示例 1：
输入: orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
输出: 6
"""

from typing import List, Optional
import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        # 买单用最大堆（取负值），卖单用最小堆
        buy_heap = []   # (-price, amount)
        sell_heap = []  # (price, amount)

        for price, amount, otype in orders:
            if otype == 0:  # 买单
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell_heap)
                    if sell_amount > amount:
                        heapq.heappush(sell_heap, (sell_price, sell_amount - amount))
                        amount = 0
                    else:
                        amount -= sell_amount
                if amount > 0:
                    heapq.heappush(buy_heap, (-price, amount))
            else:  # 卖单
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    buy_neg_price, buy_amount = heapq.heappop(buy_heap)
                    if buy_amount > amount:
                        heapq.heappush(buy_heap, (buy_neg_price, buy_amount - amount))
                        amount = 0
                    else:
                        amount -= buy_amount
                if amount > 0:
                    heapq.heappush(sell_heap, (price, amount))

        total = 0
        for _, amt in buy_heap:
            total = (total + amt) % MOD
        for _, amt in sell_heap:
            total = (total + amt) % MOD
        return total
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 用两个优先队列：
# - 买单用最大堆（取负的价格值存入最小堆），每次匹配价格最低的卖单
# - 卖单用最小堆，每次匹配价格最高的买单
# 买入订单进来时，找到所有价格 <= 当前买单价的卖单，逐一匹配。
# 卖单同理，找到所有价格 >= 当前卖单价的买单匹配。
# 最后堆中剩余的订单就是积压订单。
#
# 时间复杂度: O(N log N) — 每个订单最多入堆和出堆一次
# 空间复杂度: O(N) — 堆存储积压订单
#
# 关键点:
# - 买单匹配最低卖价，卖单匹配最高买价
# - 最大堆通过存负值实现
# - 可能部分匹配（amount 大于对方时，剩余的保留）
