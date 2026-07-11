"""
LeetCode #2034 - Stock Price Fluctuation 
股票价格波动
https://leetcode.cn/problems/stock-price-fluctuation/

给你一支股票价格的数据流。数据流中每一条记录包含一个 时间戳 和该时间点股票对应的 价格 。
不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条记录视为错误记录，后出现的记录 更正 前一条错误的记录。
请你设计一个算法，实现：
更新 股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将 更正 之前的错误价格。
找到当前记录里 最新股票价格 。最新股票价格 定义为时间戳最晚的股票价格。
找到当前记录里股票的 最高价格 。
找到当前记录里股票的 最低价格 。
请你实现 `StockPrice` 类：
`StockPrice()` 初始化对象，当前无股票价格记录。
`void update(int timestamp, int price)` 在时间点 `timestamp` 更新股票价格为 `price` 。
`int current()` 返回股票 最新价格 。
`int maximum()` 返回股票 最高价格 。
`int minimum()` 返回股票 最低价格 。

示例 1：
输入： ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"] [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []] 输出： [null, null, null, 5, 10, null, 5, null, 2]  解释： StockPrice stockPrice = new StockPrice(); stockPrice.update(1, 10); // 时间戳为 [1] ，对应的股票价格为 [10] 。 stockPrice.update(2, 5);  // 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。 stockPrice.current();     // 返回 5 ，最新时间戳为 2 ，对应价格为 5 。 stockPrice.maximum();     // 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。 stockPrice.update(1, 3);  // 之前时间戳为 1 的价格错误，价格更新为 3 。                           // 时间戳为 [1,2] ，对应股票价格为 [3,5] 。 stockPrice.maximum();     // 返回 5 ，更正后最高价格为 5 。 stockPrice.update(4, 2);  // 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。 stockPrice.minimum();     // 返回 2 ，最低价格时间戳为 4 ，价格为 2 。

提示：
`1 <= timestamp, price <= 10^9`
`update`，`current`，`maximum` 和 `minimum` 总 调用次数不超过 `10^5` 。
`current`，`maximum` 和 `minimum` 被调用时，`update` 操作 至少 已经被调用过 一次 。
"""

from typing import List, Optional


class StockPrice:

    def __init__(self):
        self.timestamp_to_price = {}
        self.latest_timestamp = 0
        self.max_heap = []  # (-price, timestamp)
        self.min_heap = []  # (price, timestamp)

    def update(self, timestamp: int, price: int) -> None:
        self.timestamp_to_price[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        import heapq
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.timestamp_to_price[self.latest_timestamp]

    def maximum(self) -> int:
        import heapq
        while self.max_heap:
            neg_price, timestamp = self.max_heap[0]
            if self.timestamp_to_price[timestamp] == -neg_price:
                return -neg_price
            heapq.heappop(self.max_heap)
        return 0

    def minimum(self) -> int:
        import heapq
        while self.min_heap:
            price, timestamp = self.min_heap[0]
            if self.timestamp_to_price[timestamp] == price:
                return price
            heapq.heappop(self.min_heap)
        return 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Hash Table, Data Stream, Ordered Set, Heap (Priority Queue)
#
# 解题思路:
# 使用哈希表存储每个时间戳的最新价格。使用最大堆和最小堆分别追踪最高和最低价格。
# 堆中存储(price, timestamp)对。当调用maximum()/minimum()时，从堆顶弹出过期的记录
# （即堆顶记录的价格与哈希表中当前时间戳的价格不一致），直到找到有效的记录。
# 这种懒删除策略避免了每次更新时从堆中删除旧记录。
#
# 时间复杂度: update O(log n), current O(1), maximum/minimum 均摊O(log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 懒删除策略：旧记录留在堆中，查询时跳过
# - 哈希表保证时间戳到最新价格的映射
# - 双堆分别维护最大和最小值
