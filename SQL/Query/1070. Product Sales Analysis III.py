"""
LeetCode #1070 - Product Sales Analysis III
中文题名：产品销售分析 III
https://leetcode.com/problems/product-sales-analysis-iii/

Table: `Sales`

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
sale_id is the primary key of this table.
product_id is a foreign key to `Product` table.
Note that the price is per unit.

Table: `Product`

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key of this table.

Write an SQL query that selects the product id,
year, quantity, and price for the
first year of every product sold.

The query result format is in the following example:

`Sales` table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+

Result table:
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+

【中文翻译】
Sales 表：

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
sale_id 是该表的主键。
product_id 是 Product 表的外键。
注意：price 表示每单位的价格。

Product 表：

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id 是该表的主键。

编写一个 SQL 查询，选出每个产品第一年的销售产品 id、年份、数量和价格。

查询结果格式如下所示：

Sales 表：
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+

Product 表：
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+

Result 表：
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+

"""

from typing import List, Optional


class Solution:
    def productSalesAnalysisIII(self, sales: List[List[int]], product: List[List[int]]) -> List[List[int]]:
        """
        sales: list of [sale_id, product_id, year, quantity, price]
        product: list of [product_id, product_name]
        returns: list of [product_id, first_year, quantity, price]
        """
        from collections import defaultdict

        min_year = {}
        for _, pid, year, qty, price in sales:
            if pid not in min_year or year < min_year[pid][0]:
                min_year[pid] = (year, qty, price)

        result = []
        for pid, (year, qty, price) in sorted(min_year.items()):
            result.append([pid, year, qty, price])

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题是 SQL 问题，核心是找到每个产品的第一年销售记录。
# SQL 解法：使用子查询或窗口函数找到每个 product_id 的最小 year，
# 然后筛选出 year 等于最小 year 的记录。
# SQL 示例：
# SELECT product_id, year AS first_year, quantity, price
# FROM Sales
# WHERE (product_id, year) IN (
#     SELECT product_id, MIN(year) FROM Sales GROUP BY product_id
# )
# Python 模拟：遍历 sales 表，用哈希表记录每个产品的最早年份及对应的数量和价格。
#
# 时间复杂度: O(n) - 遍历 sales 表一次
# 空间复杂度: O(m) - m 为不同产品数
#
# 关键点:
# - 使用 GROUP BY + MIN(year) 找到每个产品的最早销售年份
# - 用子查询或 JOIN 筛选出对应记录
# - Python 模拟时用字典记录每个产品的最小年份信息
