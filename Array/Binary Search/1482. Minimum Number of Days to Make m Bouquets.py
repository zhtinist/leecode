"""
LeetCode #1482 - Minimum Number of Days to Make m Bouquets
中文题名：制作 m 束花所需的最少天数
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

Given an integer array `bloomDay`, an integer `m` and an
integer `k`.

We need to make `m` bouquets. To make a bouquet, you need to use
`k` adjacent flowers from the garden.

The garden consists of `n` flowers, the `ith` flower will bloom
in the `bloomDay[i]` and then can be used in exactly
one bouquet.

Return the minimum number of days you need to wait to be able to make `m`
bouquets from the garden. If it is impossible to make `m` bouquets return
-1.

Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here's the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.

Example 4:

Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
Output: 1000000000
Explanation: You need to wait 1000000000 days to have a flower ready for a bouquet.

Example 5:

Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
Output: 9

Constraints:

`bloomDay.length == n`

`1 <= n <= 10^5`

`1 <= bloomDay[i] <= 10^9`

`1 <= m <= 10^6`

`1 <= k <= n`

【中文翻译】

给定一个整数数组 `bloomDay`、一个整数 `m` 和一个整数 `k`。

我们需要制作 `m` 束花。要制作一束花，你需要使用花园中 `k` 朵相邻的花。

花园由 `n` 朵花组成，第 `i` 朵花将在 `bloomDay[i]` 天开花，然后可以用于恰好一束花。

返回能够从花园中制作 `m` 束花所需等待的最少天数。如果无法制作 `m` 束花，返回 -1。

示例 1：
输入：bloomDay = [1,10,3,10,2], m = 3, k = 1
输出：3
解释：让我们看看前三天发生的情况。x 表示花开了，_ 表示花还没开。
我们需要 3 束花，每束应包含 1 朵花。
第 1 天后：[x, _, _, _, _]   // 我们只能做一束花。
第 2 天后：[x, _, _, _, x]   // 我们只能做两束花。
第 3 天后：[x, _, x, _, x]   // 我们可以做 3 束花。答案是 3。

示例 2：
输入：bloomDay = [1,10,3,10,2], m = 3, k = 2
输出：-1
解释：我们需要 3 束花，每束需要 2 朵花，这意味着我们需要 6 朵花。但我们只有 5 朵花，所以无法得到需要的花束，返回 -1。

示例 3：
输入：bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
输出：12
解释：我们需要 2 束花，每束应有 3 朵花。
第 7 天和第 12 天后花园如下：
第 7 天后：[x, x, x, x, _, x, x]
我们可以用前三朵开花的花做一束花。不能用最后三朵开花的花做另一束花，因为它们不相邻。
第 12 天后：[x, x, x, x, x, x, x]
显然我们可以用不同的方式做两束花。

示例 4：
输入：bloomDay = [1000000000,1000000000], m = 1, k = 1
输出：1000000000
解释：你需要等待 1000000000 天才有一朵花可用于花束。

示例 5：
输入：bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
输出：9

约束条件：
bloomDay.length == n
1 <= n <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= m <= 10^6
1 <= k <= n

"""

from typing import List, Optional


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        # Impossible: not enough flowers
        if m * k > n:
            return -1

        def canMake(day: int) -> bool:
            bouquets = 0
            consecutive = 0
            for bloom in bloomDay:
                if bloom <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMake(mid):
                right = mid
            else:
                left = mid + 1

        return left



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 首先检查是否可能：如果需要的总花数 m * k > n，直接返回 -1。
# 2. 使用二分搜索在 [min(bloomDay), max(bloomDay)] 范围内
#    寻找最小的满足条件的天数。
# 3. canMake(day) 辅助函数：遍历 bloomDay 数组，统计在给定天数下
#    连续开花的花的数量。当连续开花数达到 k 时，可以做一束花，
#    重置连续计数并继续。
# 4. 如果 canMake(mid) 为 true，说明 mid 天可行，尝试更小的天数
#    （right = mid）；否则需要更多天数（left = mid + 1）。
# 5. 二分搜索的单调性：天数越多，开花的花越多，越容易完成目标。
#
# 时间复杂度: O(N log M)，其中 M = max(bloomDay)
# 空间复杂度: O(1)
#
# 关键点:
# - 二分搜索答案（最小天数）
# - 单调性：天数越多，能做的花束越多
# - 统计连续开花数：遇到未开花的就重置计数
# - 需要检查 m * k > n 的提前返回条件










