"""
LeetCode #1052 - Grumpy Bookstore Owner
中文题名：爱生气的书店老板
https://leetcode.com/problems/grumpy-bookstore-owner/

Today, the bookstore owner has a store open for `customers.length` minutes.
Every minute, some number of customers (`customers[i]`) enter the store, and all
those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the
i-th minute, `grumpy[i] = 1`, otherwise `grumpy[i] = 0`.  When
the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise
they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for
`X` minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Note:

`1 <= X <= customers.length == grumpy.length <= 20000`

`0 <= customers[i] <= 1000`

`0 <= grumpy[i] <= 1`

【中文翻译】
今天，书店老板有一家店打算试营业 customers.length 分钟。每分钟都有一些顾客（customers[i]）会进入书店，所有这些顾客都会在那一分钟结束后离开。

在某些时候，书店老板会生气。如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。当书店老板生气时，那一分钟的顾客就会不满意，不生气则他们是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 X 分钟不生气，但只能使用一次。

请你返回这一天营业下来，最多有多少客户能够感到满意。

示例：

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
输出：16
解释：书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数 = 1 + 1 + 1 + 1 + 7 + 5 = 16。

注意：

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1

"""

from typing import List, Optional


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]

        extra = 0
        cur = 0
        for i in range(n):
            if grumpy[i] == 1:
                cur += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                cur -= customers[i - minutes]
            extra = max(extra, cur)

        return base + extra










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用滑动窗口。首先计算老板不生气时所有满意的顾客总数（基础值 base）。
# 然后使用一个大小为 X（minutes）的滑动窗口，计算窗口内如果使用"不生气"技巧能额外挽回的顾客数。
# 窗口内只累加原本 grumpy[i] == 1 的顾客（因为这些是在没有技巧时不满意的顾客）。
# 滑动窗口每次移动一位，更新额外挽回数，记录最大值。
# 最终结果 = base + 最大额外挽回数。
#
# 时间复杂度: O(n) - 遍历两次数组
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 基础满意顾客数（grumpy[i] == 0）是不变的
# - 滑动窗口只需关注 grumpy[i] == 1 的位置
# - 窗口内累加生气时的顾客数，窗口外减去滑出生气时的顾客数
# - 结果为 base + 最大额外挽回数
