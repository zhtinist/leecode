"""
LeetCode #1798 - Maximum Number of Consecutive Values You Can Make
中文题名：你能构造出连续值的最大数目
https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

You are given an integer array `coins` of length `n` which represents the `n` coins that you own. The value of the `ith` coin is `coins[i]`. You can make some value `x` if you can choose some of your `n` coins such that their values sum up to `x`.

Return the maximum number of consecutive integer values that you can make with your coins starting from and including `0`.

Note that you may have multiple coins of the same value.

Example 1:

Input: coins = [1,3]
Output: 2
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.

Example 2:

Input: coins = [1,1,1,4]
Output: 8
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
- 2: take [1,1]
- 3: take [1,1,1]
- 4: take [4]
- 5: take [4,1]
- 6: take [4,1,1]
- 7: take [4,1,1,1]
You can make 8 consecutive integer values starting from 0.

Example 3:

Input: nums = [1,4,10,3,1]
Output: 20

Constraints:

`coins.length == n`

`1 <= n <= 4 * 104`

`1 <= coins[i] <= 4 * 104`

【中文翻译】
给定一个整数数组 coins，表示你拥有的一些硬币面额。
从这些硬币中可以选取若干个（每个最多一次），将它们的面额相加得到一些值。
求从 0 开始最多能构造出多少个连续的整数值。

示例 1：
输入: coins = [1,3]
输出: 2
解释: 可构造的值：0(不选)，1(选1)，3(选3)，4(选1+3)。连续的从0开始：0和1连续，但缺2。所以答案是2。

示例 2：
输入: coins = [1,1,1,4]
输出: 8
解释: 可构造 0,1,2,3,4,5,6,7（0到7连续），缺8。答案是8。
"""

from typing import List, Optional


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        reachable = 0  # 当前可以构造出的连续范围 [0, reachable]

        for coin in coins:
            if coin <= reachable + 1:
                reachable += coin
            else:
                break

        return reachable + 1  # 从 0 开始的可构造数量
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心。排序硬币面额。初始可构造区间 [0, 0]。
# 遍历每个硬币 coin：
# - 如果 coin <= reachable + 1，则新区间为 [0, reachable + coin]
# - 否则出现断层（reachable+1 无法构造），停止
# 最终可构造的连续值数目 = reachable + 1（从0开始计数）。
#
# 时间复杂度: O(N log N) — 排序
# 空间复杂度: O(1)
#
# 关键点:
# - 关键结论：如果当前可构造 [0, x]，下一个硬币面额 c <= x+1，可扩展到 [0, x+c]
# - 若 c > x+1，则 x+1 永远无法构造
# - 这利用了硬币可选或不选的性质
