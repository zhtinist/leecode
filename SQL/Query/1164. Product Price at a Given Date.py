"""
LeetCode #1164 - Product Price at a Given Date
中文题名：指定日期的产品价格
https://leetcode.com/problems/product-price-at-a-given-date/

Table: `Products`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.

Write an SQL query to find the prices of all products on 2019-08-16. Assume
the price of all products before any change is 10.

The query result format is in the following example:

`Products` table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+

Result table:
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+

【中文翻译】
表：Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) 是此表的主键。此表的每一行表示某个产品在某个日期的价格被更改为新价格。

编写一个 SQL 查询，找出所有产品在 2019-08-16 这一天的价格。假设所有产品在修改前的初始价格为 10。

查询结果的格式如下例所示：

Products 表：
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+

结果表：
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
"""

import pandas as pd
from typing import List, Optional


def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    target_date = pd.Timestamp('2019-08-16')

    # Get all unique product_ids with price changes before or on target date
    valid_changes = products[products['change_date'] <= target_date]

    # For each product, get the latest change before or on target date
    latest_changes = valid_changes.sort_values('change_date').groupby('product_id').last().reset_index()
    latest_changes = latest_changes[['product_id', 'new_price']]
    latest_changes = latest_changes.rename(columns={'new_price': 'price'})

    # Get all unique product_ids
    all_products = products[['product_id']].drop_duplicates()

    # Left join to include products with no change before target date (price = 10)
    result = all_products.merge(latest_changes, on='product_id', how='left')
    result['price'] = result['price'].fillna(10).astype(int)

    return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题为 SQL 题，使用 pandas 实现：
# 1. 找出所有在目标日期（2019-08-16）或之前有价格变更的产品。
# 2. 对于每个产品，取最晚的（离目标日期最近的）价格变更记录。
# 3. 对于没有任何在目标日期之前变更记录的产品，价格为默认值 10。
# 4. 确保所有 product_id 都出现在结果中（UNION 或 LEFT JOIN）。
#
# SQL 等价写法（使用 UNION + 子查询）：
# SELECT product_id, new_price AS price
# FROM Products
# WHERE (product_id, change_date) IN (
#     SELECT product_id, MAX(change_date)
#     FROM Products
#     WHERE change_date <= '2019-08-16'
#     GROUP BY product_id
# )
# UNION
# SELECT product_id, 10 AS price
# FROM Products
# GROUP BY product_id
# HAVING MIN(change_date) > '2019-08-16';
#
# 时间复杂度: O(N log N) - 排序操作主导
# 空间复杂度: O(N) - 存储中间结果
#
# 关键点:
# - 只关注目标日期及之前的变更记录
# - 取每个产品的最新变更（最接近目标日期的）
# - 没有历史变更的产品默认价格为 10
# - 需要返回所有 product_id（包括只有未来变更的产品）
