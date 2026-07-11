"""
LeetCode #901 - Online Stock Span
中文题名：股票价格跨度
https://leetcode.com/problems/online-stock-span/

Write a class `StockSpanner` which collects daily price quotes for some stock, and
returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive
days (starting from today and going backwards) for which the price of the stock was
less than or equal to today's price.

For example, if the price of a stock over the next 7 days were `[100, 80, 60, 70, 60,
75, 85]`, then the stock spans would be `[1, 1, 1, 2, 1, 4, 6]`.

Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation:
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

Note:

Calls to `StockSpanner.next(int price)` will have `1 <= price
<= 10^5`.

There will be at most `10000` calls to `StockSpanner.next` per
test case.

There will be at most `150000` calls to `StockSpanner.next`
across all test cases.

The total time limit for this problem has been reduced by 75% for C++, and
50% for all other languages.

【中文翻译】
编写一个 `StockSpanner` 类，它收集某只股票的每日报价，并返回该股票当日价格的跨度。

今天股票价格的跨度定义为：从今天开始往回数，股票价格小于或等于今天价格的最大连续天数（包括今天）。

例如，如果一只股票在未来 7 天的价格为 `[100, 80, 60, 70, 60, 75, 85]`，那么股票跨度将是 `[1, 1, 1, 2, 1, 4, 6]`。

示例 1：

输入：["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
输出：[null,1,1,1,2,1,4,6]
解释：
首先，初始化 S = StockSpanner()，然后：
S.next(100) 被调用并返回 1，
S.next(80) 被调用并返回 1，
S.next(60) 被调用并返回 1，
S.next(70) 被调用并返回 2，
S.next(60) 被调用并返回 1，
S.next(75) 被调用并返回 4，
S.next(85) 被调用并返回 6。

注意（例如）S.next(75) 返回 4，因为最后 4 个价格（包括今天的 75）都小于或等于今天价格。

"""

from typing import List, Optional


class StockSpanner:

    def __init__(self):
        self.stack = []  # 单调递减栈，元素为 (price, span)

    def next(self, price: int) -> int:
        span = 1
        # 弹出所有 <= 当前价格的元素，累加它们的 span
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用单调递减栈（Monotonic Stack），栈中存储 (price, span) 元组。
# 对于每一个新的 price：
# 1. 初始化 span = 1（当天本身）
# 2. 弹出栈中所有 price <= 当前价格 的元素，并将它们的 span 累加到当前 span
#    （这些天都比当前价格小，所以它们的跨度可以并入当前天）
# 3. 将 (price, span) 压入栈，返回 span
#
# 因为每个元素最多入栈/出栈各一次，所以总体上 O(N)。
#
# 例如 [100, 80, 60, 70, 60, 75, 85]：
# 100 → span=1, stack=[(100,1)]
# 80 → span=1, stack=[(100,1),(80,1)]
# 60 → span=1, stack=[(100,1),(80,1),(60,1)]
# 70 → 弹出 (60,1), span=2, stack=[(100,1),(80,1),(70,2)]
# 60 → span=1, stack=[(100,1),(80,1),(70,2),(60,1)]
# 75 → 弹出 (60,1), (70,2), span=4, stack=[(100,1),(80,1),(75,4)]
# 85 → 弹出 (75,4), (80,1), span=6, stack=[(100,1),(85,6)]
#
# 时间复杂度: O(N) — 均摊 O(1)，每个元素最多入栈出栈各一次
# 空间复杂度: O(N) — 栈中最多存储 N 个元素
#
# 关键点:
# - 单调栈的核心：维护递减序列，弹出较小值并累加跨度
# - 不是每次暴力向前扫描 O(N^2)，而是利用栈 O(1) 均摊
# - 栈同时存储 price 和 span，避免额外计算
