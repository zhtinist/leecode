"""
LeetCode #1561 - Maximum Number of Coins You Can Get
中文题名：你可以获得的最大硬币数目
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/


There are 3n piles of coins of varying size, you and your friends will
take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not
necessarily consecutive).

Of your choice, Alice will pick the pile with the maximum number
of coins.

You will pick the next pile with maximum number of coins.

Your friend Bob will pick the last pile.

Repeat until there are no more piles of coins.

Given an array of integers `piles` where `piles[i]` is the
number of coins in the `ith` pile.

Return the maximum number of coins which you can have.

Example 1:

Input: piles = [2,4,1,2,7,8]
Output: 9
Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal.

Example 2:

Input: piles = [2,4,5]
Output: 4

Example 3:

Input: piles = [9,8,7,6,5,1,2,3,4]
Output: 18

Constraints:

`3 <= piles.length <= 10^5`

`piles.length % 3 == 0`

`1 <= piles[i] <= 10^4`

【中文翻译】
有 3n 堆硬币，每堆数量不同。你和两个朋友按以下规则取硬币：
每轮中，你选择任意 3 堆硬币。Alice 取最多的一堆，你取第二多的，Bob 取最少的一堆。
重复直到没有硬币堆。返回你可以获得的最大硬币数目。

示例 1：
输入：piles = [2,4,1,2,7,8]
输出：9
解释：选 (8,7,2) -> Alice 8, 你 7, Bob 2。选 (4,2,1) -> Alice 4, 你 2, Bob 1。你共得 7+2=9。

示例 2：
输入：piles = [2,4,5]
输出：4

示例 3：
输入：piles = [9,8,7,6,5,1,2,3,4]
输出：18
"""

from typing import List, Optional


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        result = 0
        # Take every second element from the sorted (desc) array, skipping the smallest n
        for i in range(1, 2 * n, 2):
            result += piles[i]
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 排序后贪心。为了让自己的收益最大，让 Alice 每次都拿最大的，自己拿第二大的，Bob 拿最小的。
# 排序（降序），取索引 1, 3, 5, ..., 2n-1 的元素求和即可。
# 因为 Alice 拿走最大的（索引 0, 2, 4, ...），Bob 拿走最小的 n 个（尾部），我们取剩下的次大值。
#
# 时间复杂度: O(N log N) — 排序
# 空间复杂度: O(1) — 忽略排序空间
#
# 关键点:
# - 策略：每次选最大、次大、最小三堆
# - 排序后取偶数索引（从 1 开始）的 n 个元素
# - Alice 总得最大的 1/3，我们得次大的 1/3












