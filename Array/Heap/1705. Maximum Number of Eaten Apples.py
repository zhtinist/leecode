"""
LeetCode #1705 - Maximum Number of Eaten Apples
中文题名：吃苹果的最大数目
https://leetcode.com/problems/maximum-number-of-eaten-apples/

There is a special kind of apple tree that grows apples every day for `n`
days. On the `ith` day, the tree grows `apples[i]`
apples that will rot after `days[i]` days, that is on day `i +
days[i]` the apples will be rotten and cannot be eaten. On some days, the
apple tree does not grow any apples, which are denoted by `apples[i] == 0`
and `days[i] == 0`.

You decided to eat at most one apple a day (to keep the doctors
away). Note that you can keep eating after the first `n` days.

Given two integer arrays `days` and `apples` of length
`n`, return the maximum number of apples you can eat.

Example 1:

Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
Output: 7
Explanation: You can eat 7 apples:
- On the first day, you eat an apple that grew on the first day.
- On the second day, you eat an apple that grew on the second day.
- On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
- On the fourth to the seventh days, you eat apples that grew on the fourth day.

Example 2:

Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
Output: 5
Explanation: You can eat 5 apples:
- On the first to the third day you eat apples that grew on the first day.
- Do nothing on the fouth and fifth days.
- On the sixth and seventh days you eat apples that grew on the sixth day.

Constraints:

`apples.length == n`

`days.length == n`

`1 <= n <= 2 * 104`

`0 <= apples[i], days[i] <= 2 * 104`

`days[i] = 0` if and only if `apples[i] = 0`.

【中文翻译】
有一种特殊的苹果树，在 `n` 天内每天都会长出苹果。在第 `i` 天，
树长出 `apples[i]` 个苹果，这些苹果将在 `days[i]` 天后腐烂，
即在第 `i + days[i]` 天，这些苹果会腐烂而不能食用。
在某些日子，苹果树不长苹果，此时 `apples[i] == 0` 且 `days[i] == 0`。

你决定每天最多吃一个苹果（为了远离医生）。注意你可以在 `n` 天之后继续吃苹果。

给定两个长度均为 `n` 的整数数组 `days` 和 `apples`，
返回你最多能吃到的苹果数量。

示例 1：

输入: apples = [1,2,3,5,2], days = [3,2,1,4,2]
输出: 7
解释: 你可以吃 7 个苹果：
- 第一天，吃一个第一天长出的苹果
- 第二天，吃一个第二天长出的苹果
- 第三天，吃一个第二天长出的苹果。这一天之后，第三天长出的苹果腐烂了
- 第四到第七天，吃第四天长出的苹果

示例 2：

输入: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
输出: 5
解释: 你可以吃 5 个苹果：
- 第一到第三天，吃第一天长出的苹果
- 第四和第五天，什么都不做
- 第六和第七天，吃第六天长出的苹果

约束条件：

`apples.length == n`
`days.length == n`
`1 <= n <= 2 * 10^4`
`0 <= apples[i], days[i] <= 2 * 10^4`
`days[i] = 0` 当且仅当 `apples[i] = 0`
"""

from typing import List, Optional
import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        """
        最小堆贪心：堆中存储 (腐烂日期, 苹果数量)。
        每一天：
        1. 如果当天有新苹果（apples[i] > 0），加入堆
        2. 移除堆顶所有已腐烂的苹果
        3. 如果堆非空，吃一个苹果（从最早腐烂的批次中取）
        4. 日期前进一天
        当 i >= n 后，不再有新苹果，但继续从堆中吃直到堆空。
        """
        n = len(apples)
        heap = []  # (rotten_day, count)
        day = 0
        eaten = 0

        # 继续循环：要么还有天数产生苹果，要么堆中还有苹果
        while day < n or heap:
            # 当天有新苹果，加入堆
            if day < n and apples[day] > 0:
                heapq.heappush(heap, (day + days[day], apples[day]))

            # 移除所有已腐烂的苹果
            while heap and heap[0][0] <= day:
                heapq.heappop(heap)

            # 吃一个苹果
            if heap:
                rotten_day, count = heapq.heappop(heap)
                eaten += 1
                if count > 1:
                    heapq.heappush(heap, (rotten_day, count - 1))

            day += 1

        return eaten










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略：每天应该吃那个最先腐烂的苹果（最急迫的），以保证不吃到腐烂苹果。
# 使用最小堆（优先队列）存储 (腐烂日期, 苹果数量)，腐烂日期最早的在堆顶。
#
# 每天的操作：
# 1. 如果还在 n 天内且有新苹果，将 (day + days[day], apples[day]) 入堆
# 2. 弹出堆顶所有腐烂日期 <= 当前日期的批次（已腐烂）
# 3. 如果堆非空，从堆顶取一个苹果吃（堆顶是最早腐烂的）
#    - 如果该批次还有剩余，重新入堆
# 4. day += 1
#
# 循环条件：day < n 或堆非空（第 n 天之后还可以继续吃库存）
#
# 时间复杂度: O((n + k) log n)，k 为超过 n 的天数，每次堆操作 O(log n)
# 空间复杂度: O(n)，堆的大小
#
# 关键点:
# - 永远吃最早腐烂的苹果（贪心最优性）
# - 堆存储 (腐烂日期, 数量)，而非每个苹果单独存储，减少堆操作
# - 循环直到 day >= n 且堆为空
# - 每天最多吃一个苹果
