"""
LeetCode #1158 - Market Analysis I
中文题名：市场分析 I
https://leetcode.com/problems/market-analysis-i/

Table: `Users`

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.

Table: `Orders`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key of this table.
item_id is a foreign key to the Items table.
buyer_id and seller_id are foreign keys to the Users table.

Table: `Items`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id is the primary key of this table.

Write an SQL query to find for each user, the join date and the number of orders they made as
a buyer in 2019.

The query result format is in the following example:

Users table:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2018-01-01 | Lenovo         |
| 2       | 2018-02-09 | Samsung        |
| 3       | 2018-01-19 | LG             |
| 4       | 2018-05-21 | HP             |
+---------+------------+----------------+

Orders table:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2018-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2018-08-04 | 1       | 4        | 2         |
| 5        | 2018-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+

Items table:
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+

Result table:
+-----------+------------+----------------+
| buyer_id  | join_date  | orders_in_2019 |
+-----------+------------+----------------+
| 1         | 2018-01-01 | 1              |
| 2         | 2018-02-09 | 2              |
| 3         | 2018-01-19 | 0              |
| 4         | 2018-05-21 | 0              |
+-----------+------------+----------------+

【中文翻译】
表：Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id 是此表的主键。此表包含在线购物网站的用户信息，用户可以在该网站买卖商品。

表：Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id 是此表的主键。item_id 是 Items 表的外键。buyer_id 和 seller_id 是 Users 表的外键。

表：Items

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id 是此表的主键。

编写一个 SQL 查询，为每个用户查找加入日期以及他们在 2019 年作为买家下达的订单数。

查询结果格式如下例所示：

Users 表：
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2018-01-01 | Lenovo         |
| 2       | 2018-02-09 | Samsung        |
| 3       | 2018-01-19 | LG             |
| 4       | 2018-05-21 | HP             |
+---------+------------+----------------+

Orders 表：
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2018-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2018-08-04 | 1       | 4        | 2         |
| 5        | 2018-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+

Items 表：
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+

结果表：
+-----------+------------+----------------+
| buyer_id  | join_date  | orders_in_2019 |
+-----------+------------+----------------+
| 1         | 2018-01-01 | 1              |
| 2         | 2018-02-09 | 2              |
| 3         | 2018-01-19 | 0              |
| 4         | 2018-05-21 | 0              |
+-----------+------------+----------------+
"""

import pandas as pd
from typing import List, Optional


def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    # Filter orders from 2019
    orders_2019 = orders[orders['order_date'].dt.year == 2019]

    # Count orders per buyer in 2019
    buyer_counts = orders_2019.groupby('buyer_id').size().reset_index(name='orders_in_2019')

    # Left join with all users to include users with 0 orders
    result = users[['user_id', 'join_date']].merge(
        buyer_counts, left_on='user_id', right_on='buyer_id', how='left'
    )

    # Fill NaN with 0 for users with no 2019 orders
    result['orders_in_2019'] = result['orders_in_2019'].fillna(0).astype(int)

    return result[['buyer_id', 'join_date', 'orders_in_2019']]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题为 SQL 题，使用 pandas 实现：
# 1. 从 Orders 表中筛选出 2019 年的订单（order_date 年份为 2019）。
# 2. 按 buyer_id 分组统计每个买家在 2019 年的订单数量。
# 3. 将 Users 表（所有用户）与统计结果进行左连接（LEFT JOIN），
#    确保没有 2019 年订单的用户也出现在结果中（orders_in_2019 = 0）。
# 4. 选择需要的列：buyer_id、join_date、orders_in_2019。
#
# SQL 等价写法：
# SELECT u.user_id AS buyer_id, u.join_date,
#        COUNT(o.order_id) AS orders_in_2019
# FROM Users u
# LEFT JOIN Orders o ON u.user_id = o.buyer_id AND YEAR(o.order_date) = 2019
# GROUP BY u.user_id, u.join_date;
#
# 时间复杂度: O(N_users + N_orders) - 遍历两个表
# 空间复杂度: O(N_users) - 存储结果
#
# 关键点:
# - LEFT JOIN 确保所有用户都在结果中，包括没有订单的用户
# - 筛选条件 YEAR(order_date) = 2019 放在 JOIN 条件中而非 WHERE 中
# - 没有订单的用户 orders_in_2019 设为 0
# - 返回列名为 buyer_id（不是 user_id）
