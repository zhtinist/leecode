"""
LeetCode #1393 - Capital Gain/Loss
中文题名：资本损益
https://leetcode.com/problems/capital-gainloss/

SQL Schema

Table: `Stocks`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| stock_name    | varchar |
| operation     | enum    |
| operation_day | int     |
| price         | int     |
+---------------+---------+
(stock_name, day) is the primary key for this table.
The operation column is an ENUM of type ('Sell', 'Buy')
Each row of this table indicates that the stock which has stock_name had an operation on the day operation_day with the price.
It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day.

Write an SQL query to report the Capital gain/loss for each stock.

The capital gain/loss of a stock is total gain or loss after buying and selling the
stock one or many times.

Return the result table in any order.

The query result format is in the following example:

`Stocks` table:
+---------------+-----------+---------------+--------+
| stock_name    | operation | operation_day | price  |
+---------------+-----------+---------------+--------+
| Leetcode      | Buy       | 1             | 1000   |
| Corona Masks  | Buy       | 2             | 10     |
| Leetcode      | Sell      | 5             | 9000   |
| Handbags      | Buy       | 17            | 30000  |
| Corona Masks  | Sell      | 3             | 1010   |
| Corona Masks  | Buy       | 4             | 1000   |
| Corona Masks  | Sell      | 5             | 500    |
| Corona Masks  | Buy       | 6             | 1000   |
| Handbags      | Sell      | 29            | 7000   |
| Corona Masks  | Sell      | 10            | 10000  |
+---------------+-----------+---------------+--------+

Result table:
+---------------+-------------------+
| stock_name    | capital_gain_loss |
+---------------+-------------------+
| Corona Masks  | 9500              |
| Leetcode      | 8000              |
| Handbags      | -23000            |
+---------------+-------------------+
Leetcode stock was bought at day 1 for 1000$ and was sold at day 5 for 9000$. Capital gain = 9000 - 1000 = 8000$.
Handbags stock was bought at day 17 for 30000$ and was sold at day 29 for 7000$. Capital loss = 7000 - 30000 = -23000$.
Corona Masks stock was bought at day 1 for 10$ and was sold at day 3 for 1010$. It was bought again at day 4 for 1000$ and was sold at day 5 for 500$. At last, it was bought at day 6 for 1000$ and was sold at day 10 for 10000$. Capital gain/loss is the sum of capital gains/losses for each ('Buy' --> 'Sell') operation = (1010 - 10) + (500 - 1000) + (10000 - 1000) = 1000 - 500 + 9000 = 9500$.

【中文翻译】

SQL Schema

表 Stocks：

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| stock_name    | varchar |
| operation     | enum    |
| operation_day | int     |
| price         | int     |
+---------------+---------+
(stock_name, day) 是该表的主键。
operation 列为 ENUM 类型（'Sell', 'Buy'）。
表中每行表示 stock_name 股票在 operation_day 以 price 价格进行了一次操作。
保证每个股票的每次 'Sell' 操作都对应之前某天的 'Buy' 操作。

编写 SQL 查询报告每只股票的资本损益。

股票的资本损益是买入和卖出后获得的总收益或亏损。

以任意顺序返回结果表。

示例：
Stocks 表：
+---------------+-----------+---------------+--------+
| stock_name    | operation | operation_day | price  |
+---------------+-----------+---------------+--------+
| Leetcode      | Buy       | 1             | 1000   |
| Corona Masks  | Buy       | 2             | 10     |
| Leetcode      | Sell      | 5             | 9000   |
| Handbags      | Buy       | 17            | 30000  |
| Corona Masks  | Sell      | 3             | 1010   |
| Corona Masks  | Buy       | 4             | 1000   |
| Corona Masks  | Sell      | 5             | 500    |
| Corona Masks  | Buy       | 6             | 1000   |
| Handbags      | Sell      | 29            | 7000   |
| Corona Masks  | Sell      | 10            | 10000  |
+---------------+-----------+---------------+--------+

结果表：
+---------------+-------------------+
| stock_name    | capital_gain_loss |
+---------------+-------------------+
| Corona Masks  | 9500              |
| Leetcode      | 8000              |
| Handbags      | -23000            |
+---------------+-------------------+
Leetcode 股票在第 1 天以 1000$ 买入，在第 5 天以 9000$ 卖出。资本收益 = 9000 - 1000 = 8000$。
Handbags 股票在第 17 天以 30000$ 买入，在第 29 天以 7000$ 卖出。资本损失 = 7000 - 30000 = -23000$。
Corona Masks 股票在第 1 天以 10$ 买入，第 3 天以 1010$ 卖出。第 4 天再以 1000$ 买入，第 5 天以 500$ 卖出。最后第 6 天以 1000$ 买入，第 10 天以 10000$ 卖出。资本损益 = (1010 - 10) + (500 - 1000) + (10000 - 1000) = 9500$。

约束条件：保证每个 Sell 操作都有一个之前对应的 Buy 操作。
"""

from typing import List, Optional


class Solution:
    def capital_gain_loss(self, stocks):
        # SQL 问题 - 计算每只股票的资本损益
        # SELECT stock_name, SUM(CASE WHEN operation='Buy' THEN -price ELSE price END) as capital_gain_loss
        # FROM Stocks
        # GROUP BY stock_name
        pass



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这是 SQL 问题，使用 GROUP BY 按股票名称分组求和。
# 对于买入（Buy）操作，价格取负值；卖出（Sell）操作价格取正值。
# 求和后的结果即为资本损益。SQL 写法：
# SELECT stock_name, SUM(CASE WHEN operation='Buy' THEN -price ELSE price END) as capital_gain_loss
# FROM Stocks GROUP BY stock_name;
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 将 Buy 视为负现金流（支出），Sell 视为正现金流（收入）
# - 使用 CASE WHEN 条件表达式分别处理买入和卖出
# - 按 stock_name 分组后对价格求和










