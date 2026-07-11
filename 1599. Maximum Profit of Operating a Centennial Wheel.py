"""
LeetCode #1599 - Maximum Profit of Operating a Centennial Wheel
中文题名：经营摩天轮的最大利润
https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/


You are the operator of a Centennial Wheel that has four gondolas,
and each gondola has room for up to four
people. You have the ability to rotate the gondolas counterclockwise,
which costs you `runningCost` dollars.

You are given an array `customers` of length `n` where `customers[i]`
is the number of new customers arriving just before the `ith`
rotation (0-indexed). This means you must rotate the wheel
`i` times before `customers[i]` arrive. Each customer pays
`boardingCost` dollars when they board on the gondola closest to the
ground and will exit once that gondola reaches the ground again.

You can stop the wheel at any time, including before
serving all customers. If you
decide to stop serving customers, all subsequent rotations are free
in order to get all the customers down safely. Note that if there are currently more
than four customers waiting at the wheel, only four will board the gondola, and the
rest will wait for the next rotation.

Return the minimum number of rotations you need to perform to maximize your
profit. If there is no scenario where the profit is positive,
return `-1`.

Example 1:

Input: customers = [8,3], boardingCost = 5, runningCost = 6
Output: 3
Explanation: The numbers written on the gondolas are the number of people currently there.
1. 8 customers arrive, 4 board and 4 wait for the next gondola, the wheel rotates. Current profit is 4 * $5 - 1 * $6 = $14.
2. 3 customers arrive, the 4 waiting board the wheel and the other 3 wait, the wheel rotates. Current profit is 8 * $5 - 2 * $6 = $28.
3. The final 3 customers board the gondola, the wheel rotates. Current profit is 11 * $5 - 3 * $6 = $37.
The highest profit was $37 after rotating the wheel 3 times.

Example 2:

Input: customers = [10,9,6], boardingCost = 6, runningCost = 4
Output: 7
Explanation:
1. 10 customers arrive, 4 board and 6 wait for the next gondola, the wheel rotates. Current profit is 4 * $6 - 1 * $4 = $20.
2. 9 customers arrive, 4 board and 11 wait (2 originally waiting, 9 newly waiting), the wheel rotates. Current profit is 8 * $6 - 2 * $4 = $40.
3. The final 6 customers arrive, 4 board and 13 wait, the wheel rotates. Current profit is 12 * $6 - 3 * $4 = $60.
4. 4 board and 9 wait, the wheel rotates. Current profit is 16 * $6 - 4 * $4 = $80.
5. 4 board and 5 wait, the wheel rotates. Current profit is 20 * $6 - 5 * $4 = $100.
6. 4 board and 1 waits, the wheel rotates. Current profit is 24 * $6 - 6 * $4 = $120.
7. 1 boards, the wheel rotates. Current profit is 25 * $6 - 7 * $4 = $122.
The highest profit was $122 after rotating the wheel 7 times.

Example 3:

Input: customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92
Output: -1
Explanation:
1. 3 customers arrive, 3 board and 0 wait, the wheel rotates. Current profit is 3 * $1 - 1 * $92 = -$89.
2. 4 customers arrive, 4 board and 0 wait, the wheel rotates. Current profit is 7 * $1 - 2 * $92 = -$177.
3. 0 customers arrive, 0 board and 0 wait, the wheel rotates. Current profit is 7 * $1 - 3 * $92 = -$269.
4. 5 customers arrive, 4 board and 1 waits, the wheel rotates. Current profit is 12 * $1 - 4 * $92 = -$356.
5. 1 customer arrives, 2 board and 0 wait, the wheel rotates. Current profit is 13 * $1 - 5 * $92 = -$447.
The profit was never positive, so return -1.

Example 4:

Input: customers = [10,10,6,4,7], boardingCost = 3, runningCost = 8
Output: 9
Explanation:
1. 10 customers arrive, 4 board and 6 wait, the wheel rotates. Current profit is 4 * $3 - 1 * $8 = $4.
2. 10 customers arrive, 4 board and 12 wait, the wheel rotates. Current profit is 8 * $3 - 2 * $8 = $8.
3. 6 customers arrive, 4 board and 14 wait, the wheel rotates. Current profit is 12 * $3 - 3 * $8 = $12.
4. 4 customers arrive, 4 board and 14 wait, the wheel rotates. Current profit is 16 * $3 - 4 * $8 = $16.
5. 7 customers arrive, 4 board and 17 wait, the wheel rotates. Current profit is 20 * $3 - 5 * $8 = $20.
6. 4 board and 13 wait, the wheel rotates. Current profit is 24 * $3 - 6 * $8 = $24.
7. 4 board and 9 wait, the wheel rotates. Current profit is 28 * $3 - 7 * $8 = $28.
8. 4 board and 5 wait, the wheel rotates. Current profit is 32 * $3 - 8 * $8 = $32.
9. 4 board and 1 waits, the wheel rotates. Current profit is 36 * $3 - 9 * $8 = $36.
10. 1 board and 0 wait, the wheel rotates. Current profit is 37 * $3 - 10 * $8 = $31.
The highest profit was $36 after rotating the wheel 9 times.

Constraints:

`n == customers.length`

`1 <= n <= 105`

`0 <= customers[i] <= 50`

`1 <= boardingCost, runningCost <= 100`

【中文翻译】
摩天轮有 4 个座舱，每个可容纳 4 人。每轮旋转成本为 runningCost，
每位乘客登舱收费 boardingCost。customers[i] 表示第 i 次旋转前到达的新乘客数。
每次旋转前，先让等待的乘客登舱（最多 4 人），旋转后再允许新乘客到达。
返回使利润最大化的最少旋转次数（1 索引）。如果从不盈利，返回 -1。

示例 1：输入：customers = [8,3], boardingCost = 5, runningCost = 6
输出：3

示例 2：输入：customers = [10,9,6], boardingCost = 6, runningCost = 4
输出：7
"""

from typing import List, Optional


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        best_rotation = -1
        waiting = 0
        profit = 0
        i = 0
        rotation = 0
        while i < len(customers) or waiting > 0:
            if i < len(customers):
                waiting += customers[i]
                i += 1
            rotation += 1
            board = min(4, waiting)
            waiting -= board
            profit += board * boardingCost - runningCost
            if profit > max_profit:
                max_profit = profit
                best_rotation = rotation
        return best_rotation



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 模拟过程。维护等待队列人数 waiting。对于每次旋转：
# 如果还有顾客到达（i < n），将新顾客加入等待队列。
# 每次登舱最多 4 人。利润 += 登船人数 * boardingCost - runningCost。
# 持续旋转直到所有顾客都到达且等待队列为空。
# 记录最大利润对应的旋转次数。如果最大利润 <= 0，返回 -1。
#
# 时间复杂度: O(N + T) — N 为到达批次数，T 为总旋转次数
# 空间复杂度: O(1)
#
# 关键点:
# - 模拟每一轮旋转过程
# - 每次最多登舱 4 人
# - 记录最大利润对应的最早旋转次数












