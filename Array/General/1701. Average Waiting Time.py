"""
LeetCode #1701 - Average Waiting Time
中文题名：平均等待时间
https://leetcode.com/problems/average-waiting-time/

There is a restaurant with a single chef. You are given an array
`customers`, where `customers[i] = [arrivali,
timei]:`

`arrivali` is the arrival time of the `ith`
customer. The arrival times are sorted in non-decreasing order.

`timei` is the time needed to prepare the order of the
`ith` customer.

When a customer arrives, he gives the chef his order, and the chef starts preparing
it once he is idle. The customer waits till the chef finishes preparing his order.
The chef does not prepare food for more than one customer at a time. The chef
prepares food for customers in the order they were given in the
input.

Return the average waiting time of all customers. Solutions
within `10-5` from the actual answer are considered accepted.

Example 1:

Input: customers = [[1,2],[2,5],[4,3]]
Output: 5.00000
Explanation:
1) The first customer arrives at time 1, the chef takes his order and starts preparing it immediately at time 1, and finishes at time 3, so the waiting time of the first customer is 3 - 1 = 2.
2) The second customer arrives at time 2, the chef takes his order and starts preparing it at time 3, and finishes at time 8, so the waiting time of the second customer is 8 - 2 = 6.
3) The third customer arrives at time 4, the chef takes his order and starts preparing it at time 8, and finishes at time 11, so the waiting time of the third customer is 11 - 4 = 7.
So the average waiting time = (2 + 6 + 7) / 3 = 5.

Example 2:

Input: customers = [[5,2],[5,4],[10,3],[20,1]]
Output: 3.25000
Explanation:
1) The first customer arrives at time 5, the chef takes his order and starts preparing it immediately at time 5, and finishes at time 7, so the waiting time of the first customer is 7 - 5 = 2.
2) The second customer arrives at time 5, the chef takes his order and starts preparing it at time 7, and finishes at time 11, so the waiting time of the second customer is 11 - 5 = 6.
3) The third customer arrives at time 10, the chef takes his order and starts preparing it at time 11, and finishes at time 14, so the waiting time of the third customer is 14 - 10 = 4.
4) The fourth customer arrives at time 20, the chef takes his order and starts preparing it immediately at time 20, and finishes at time 21, so the waiting time of the fourth customer is 21 - 20 = 1.
So the average waiting time = (2 + 6 + 4 + 1) / 4 = 3.25.

Constraints:

`1 <= customers.length <= 105`

`1 <= arrivali, timei <= 104`

`arrivali <= arrivali+1`

【中文翻译】
有一家餐厅只有一位厨师。给定一个数组 `customers`，其中 `customers[i] = [arrival_i, time_i]`：

- `arrival_i` 是第 `i` 位顾客的到达时间。到达时间按非递减顺序排列。
- `time_i` 是准备第 `i` 位顾客订单所需的时间。

当顾客到达时，他把订单交给厨师，厨师在空闲时开始准备。
顾客一直等到厨师准备好其订单。厨师一次只能为一位顾客准备食物，
且按输入顺序处理订单。

返回所有顾客的平均等待时间。与正确答案误差在 `10^-5` 以内的解均被接受。

示例 1：

输入: customers = [[1,2],[2,5],[4,3]]
输出: 5.00000
解释:
1) 第一位顾客在时刻 1 到达，厨师立即开始准备，时刻 3 完成，等待时间 = 3 - 1 = 2
2) 第二位顾客在时刻 2 到达，厨师从时刻 3 开始准备，时刻 8 完成，等待时间 = 8 - 2 = 6
3) 第三位顾客在时刻 4 到达，厨师从时刻 8 开始准备，时刻 11 完成，等待时间 = 11 - 4 = 7
平均等待时间 = (2 + 6 + 7) / 3 = 5

示例 2：

输入: customers = [[5,2],[5,4],[10,3],[20,1]]
输出: 3.25000
解释:
1) 第一位顾客在时刻 5 到达，立即开始，时刻 7 完成，等待时间 = 7 - 5 = 2
2) 第二位顾客在时刻 5 到达，从时刻 7 开始，时刻 11 完成，等待时间 = 11 - 5 = 6
3) 第三位顾客在时刻 10 到达，从时刻 11 开始，时刻 14 完成，等待时间 = 14 - 10 = 4
4) 第四位顾客在时刻 20 到达，立即开始，时刻 21 完成，等待时间 = 21 - 20 = 1
平均等待时间 = (2 + 6 + 4 + 1) / 4 = 3.25

约束条件：

`1 <= customers.length <= 10^5`
`1 <= arrival_i, time_i <= 10^4`
`arrival_i <= arrival_{i+1}`
"""

from typing import List, Optional


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        """
        模拟：跟踪当前时间 cur_time。
        对每位顾客 [arrival, prep_time]：
        - start_time = max(cur_time, arrival)  # 厨师有空 或 顾客到达
        - finish_time = start_time + prep_time
        - wait_time = finish_time - arrival
        - 累加总等待时间，更新 cur_time = finish_time
        最后返回 total_wait / n
        """
        cur_time = 0
        total_wait = 0

        for arrival, prep_time in customers:
            start_time = max(cur_time, arrival)
            finish_time = start_time + prep_time
            total_wait += finish_time - arrival
            cur_time = finish_time

        return total_wait / len(customers)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 简单的模拟题。维护当前时间 cur_time 表示厨师何时可以开始下一单。
# 对于每位顾客 [arrival, prep_time]：
# - 开始时间 = max(cur_time, arrival)，即要么厨师空闲时开始，要么顾客到达时开始
# - 完成时间 = 开始时间 + prep_time
# - 等待时间 = 完成时间 - arrival（注意不是完成时间 - 开始时间！）
# - 累加等待时间，更新 cur_time = 完成时间
# 最后返回总等待时间 / n。
#
# 时间复杂度: O(n)，遍历一次
# 空间复杂度: O(1)，仅使用常数额外空间
#
# 关键点:
# - 等待时间 = 完成时间 - 到达时间，而非完成时间 - 开始时间
# - 当前时间 cur_time 按顺序更新即可（输入已按 arrival 排序）
# - 用 float 除法返回平均值
