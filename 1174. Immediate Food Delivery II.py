"""
LeetCode #1174 - Immediate Food Delivery II
中文题名：即时食物配送 II
https://leetcode.com/problems/immediate-food-delivery-ii/

Table: `Delivery`

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the primary key of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).

If the preferred delivery date of the customer is the same as the order date then
the order is called immediate otherwise it's called scheduled.

The first order of a customer is the order with the earliest order date
that customer made. It is guaranteed that a customer has exactly one first order.

Write an SQL query to find the percentage of immediate orders in the first orders of all
customers, rounded to 2 decimal places.

The query result format is in the following example:

Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+

Result table:
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
The customer id 1 has a first order with delivery id 1 and it is scheduled.
The customer id 2 has a first order with delivery id 2 and it is immediate.
The customer id 3 has a first order with delivery id 5 and it is scheduled.
The customer id 4 has a first order with delivery id 7 and it is immediate.
Hence, half the customers have immediate first orders.

【中文翻译】
表：Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id 是此表的主键。此表包含顾客的食物配送信息，顾客在某个日期下单并指定一个期望配送日期（与订单日期相同或在其之后）。

如果顾客的期望配送日期与订单日期相同，则该订单称为即时订单，否则称为计划订单。

每个顾客的第一笔订单是该顾客下单日期最早的订单。保证每个顾客恰好有一笔第一订单。

编写一个 SQL 查询，计算所有顾客的第一笔订单中即时订单的百分比，结果四舍五入保留两位小数。

查询结果格式如下例所示：

Delivery 表：
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 2           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-12                  |
| 4           | 3           | 2019-08-24 | 2019-08-24                  |
| 5           | 3           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
| 7           | 4           | 2019-08-09 | 2019-08-09                  |
+-------------+-------------+------------+-----------------------------+

结果表：
+----------------------+
| immediate_percentage |
+----------------------+
| 50.00                |
+----------------------+
顾客 1 的第一笔订单是 delivery_id 为 1 的订单，它是计划订单。
顾客 2 的第一笔订单是 delivery_id 为 2 的订单，它是即时订单。
顾客 3 的第一笔订单是 delivery_id 为 5 的订单，它是计划订单。
顾客 4 的第一笔订单是 delivery_id 为 7 的订单，它是即时订单。
因此，一半顾客的第一笔订单是即时订单。
"""

import pandas as pd
from typing import List, Optional


def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Find the first order (earliest order_date) for each customer
    first_orders = delivery.loc[delivery.groupby('customer_id')['order_date'].idxmin()]

    # Count how many first orders are immediate
    immediate_count = (first_orders['order_date'] == first_orders['customer_pref_delivery_date']).sum()
    total_count = len(first_orders)

    # Calculate percentage, rounded to 2 decimal places
    percentage = round(immediate_count / total_count * 100, 2)

    return pd.DataFrame({'immediate_percentage': [percentage]})










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题为 SQL 题，使用 pandas 实现：
# 1. 找出每个顾客的第一笔订单（最早 order_date）：
#    使用 groupby('customer_id')['order_date'].idxmin() 获取每个顾客最早订单的索引。
# 2. 从原始表中提取这些第一笔订单的记录。
# 3. 统计其中即时订单的数量：
#    即时订单 = order_date == customer_pref_delivery_date。
# 4. 计算百分比：即时订单数 / 总第一笔订单数 * 100，四舍五入到两位小数。
# 5. 返回包含 immediate_percentage 列的 DataFrame。
#
# SQL 等价写法：
# SELECT ROUND(
#     SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)
#     / COUNT(*) * 100, 2
# ) AS immediate_percentage
# FROM Delivery
# WHERE (customer_id, order_date) IN (
#     SELECT customer_id, MIN(order_date)
#     FROM Delivery
#     GROUP BY customer_id
# );
#
# 时间复杂度: O(N log N) - groupby 排序操作
# 空间复杂度: O(N) - 存储分组结果
#
# 关键点:
# - "第一笔订单"定义为每个顾客最早的 order_date
# - 即时订单的判断：order_date == customer_pref_delivery_date
# - 百分比计算并四舍五入到两位小数
# - idxmin 返回 groupby 中最小值的索引位置
