"""
LeetCode #1193 - Monthly Transactions I
中文题名：每月交易 I
https://leetcode.com/problems/monthly-transactions-i/

Table: `Transactions`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].

Write an SQL query to find for each month and country, the number of transactions and their
total amount, the number of approved transactions and their total amount.

The query result format is in the following example:

`Transactions` table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+

Result table:
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+

【中文翻译】
表：Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id 是这个表的主键。
该表包含有关传入交易的信息。
state 列的类型是 ["approved", "declined"]。

编写一个 SQL 查询，查找每个月和每个国家/地区，已交易的数量及其总金额、已批准交易的数量及其总金额。

查询结果格式如下例所示：

Transactions 表：
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+

结果表：
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+

"""

from typing import List, Optional


class Solution:
    """
    SQL Solution (submit this in LeetCode SQL editor):

    SELECT
        DATE_FORMAT(trans_date, '%Y-%m') AS month,
        country,
        COUNT(*) AS trans_count,
        SUM(state = 'approved') AS approved_count,
        SUM(amount) AS trans_total_amount,
        SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
    FROM Transactions
    GROUP BY month, country;
    """










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题为 SQL 聚合查询问题，核心是 GROUP BY + 条件聚合。
# 1. 使用 DATE_FORMAT(trans_date, '%Y-%m') 提取年月作为分组维度。
# 2. 按 month 和 country 分组 GROUP BY。
# 3. 使用聚合函数计算各指标：
#    - COUNT(*)：总交易数
#    - SUM(state = 'approved')：利用 MySQL 中布尔表达式返回 0/1 的特性计算批准交易数
#    - SUM(amount)：总交易金额
#    - SUM(IF(state = 'approved', amount, 0))：批准交易的总金额（条件求和）
#
# 时间复杂度: O(n) - 全表扫描
# 空间复杂度: O(k) - k 为分组数量（月份 * 国家数）
#
# 关键点:
# - 日期格式化函数：DATE_FORMAT(trans_date, '%Y-%m') 或 LEFT(trans_date, 7)
# - 条件聚合技巧：SUM(state = 'approved') 利用布尔值转整数
# - 条件求和：SUM(IF(state = 'approved', amount, 0)) 或 SUM(CASE WHEN ...)
