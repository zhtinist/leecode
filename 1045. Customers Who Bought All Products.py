"""
LeetCode #1045 - Customers Who Bought All Products
中文题名：买下所有产品的客户
https://leetcode.com/problems/customers-who-bought-all-products/

Table: `Customer`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
product_key is a foreign key to `Product` table.

Table: `Product`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key column for this table.

Write an SQL query for a report that provides the customer ids from
the `Customer` table that bought all the products in the `Product` table.

For example:

Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+

Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+

Result table:
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
The customers who bought all the products (5 and 6) are customers with id 1 and 3.

【中文翻译】
表：Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
product_key 是 Product 表的外键。

表：Product

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key 是该表的主键列。

编写一个 SQL 查询，报告 Customer 表中购买了 Product 表中所有产品的客户 ID。

例如：

Customer 表：
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+

Product 表：
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+

结果表：
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
购买了所有产品（5 和 6）的客户是 ID 为 1 和 3 的客户。
"""

from typing import List, Optional


class Solution:
    def findCustomers(self, customer: List[List[int]], product: List[List[int]]) -> List[int]:
        # Get all products
        all_products = set(row[0] for row in product)

        # Group by customer_id and collect their products
        customer_products = {}
        for cid, pid in customer:
            if cid not in customer_products:
                customer_products[cid] = set()
            customer_products[cid].add(pid)

        # Find customers who bought all products
        result = []
        for cid, products in customer_products.items():
            if products == all_products:
                result.append(cid)

        return sorted(result)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# SQL解法：使用 GROUP BY 和 HAVING 子句。按 customer_id 分组后，
# 统计每个客户购买的不同产品数量。如果该数量等于 Product 表中的总产品数，
# 说明该客户购买了所有产品。可以使用子查询或 JOIN 获取总产品数。
# SQL语句：SELECT customer_id FROM Customer GROUP BY customer_id
# HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)
#
# Python解法：先获取所有产品的集合。然后按客户ID分组，收集每个客户购买的产品集合。
# 比较客户的产品集合是否与全部产品集合相同。
#
# 时间复杂度: O(N + M) - N为Customer行数，M为Product行数
# 空间复杂度: O(N + M) - 存储产品集合和客户产品映射
#
# 关键点:
# - 需要 DISTINCT product_key，因为同一客户可能多次购买同一产品
# - 使用 HAVING 而非 WHERE，因为需要对分组后的聚合结果进行过滤
# - 比较集合是否相等即可判断是否购买了所有产品
