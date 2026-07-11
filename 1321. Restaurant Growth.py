"""
LeetCode #1321 - Restaurant Growth
中文题名：餐馆营业额变化增长
https://leetcode.com/problems/restaurant-growth/


SQL Schema

Table: `Customer`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
(customer_id, visited_on) is the primary key for this table.
This table contains data about customer transactions in a restaurant.
visited_on is the date on which the customer with ID (customer_id) have visited the restaurant.
amount is the total paid by a customer.

You are the restaurant owner and you want to analyze a possible expansion (there will
be at least one customer every day).

Write an SQL query to compute moving average of how much customer paid in a 7 days
window (current day + 6 days before) .

The query result format is in the following example:

Return result table ordered by visited_on.

`average_amount `should be rounded to 2 decimal
places, all dates are in the format ('YYYY-MM-DD').

Customer table:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         |
| 6           | Elvis        | 2019-01-06   | 140         |
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         |
| 1           | Jhon         | 2019-01-10   | 130         |
| 3           | Jade         | 2019-01-10   | 150         |
+-------------+--------------+--------------+-------------+

Result table:
+--------------+--------------+----------------+
| visited_on   | amount       | average_amount |
+--------------+--------------+----------------+
| 2019-01-07   | 860          | 122.86         |
| 2019-01-08   | 840          | 120            |
| 2019-01-09   | 840          | 120            |
| 2019-01-10   | 1000         | 142.86         |
+--------------+--------------+----------------+

1st moving average from 2019-01-01 to 2019-01-07 has an average_amount of (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
2nd moving average from 2019-01-02 to 2019-01-08 has an average_amount of (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
3rd moving average from 2019-01-03 to 2019-01-09 has an average_amount of (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
4th moving average from 2019-01-04 to 2019-01-10 has an average_amount of (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86

【中文翻译】
这是一个 SQL 问题。请参考 LeetCode 原题获取完整的 SQL 问题描述。
题目要求计算每个顾客访问日期的 7 天滚动平均消费金额。
"""

from typing import List, Optional


class Solution:
    def restaurant_growth(self, customer):
        # This is a SQL problem. See problem description for SQL solution.
        # SQL: Use window function SUM OVER ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        # and GROUP BY visited_on with HAVING to ensure 7 days of data.
        pass



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# SQL 窗口函数问题。使用 ROWS BETWEEN 6 PRECEDING AND CURRENT ROW 计算 7 天滚动总和，
# 然后除以 7 得到平均值。需要使用子查询或 CTE 先按天聚合金额，
# 再使用窗口函数计算滚动平均。最后过滤掉不足 7 天的日期。
#
# 时间复杂度: O(N log N) — 排序和窗口函数
# 空间复杂度: O(N)
#
# 关键点:
# - 窗口函数 ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
# - 先按天聚合，再计算滚动平均
# - 使用 HAVING 或子查询确保至少 7 天数据












