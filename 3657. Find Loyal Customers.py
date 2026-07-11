"""
LeetCode #3657 - Find Loyal Customers
寻找忠实客户
https://leetcode.cn/problems/find-loyal-customers/

表：`customer_transactions`
+------------------+---------+ | Column Name      | Type    |  +------------------+---------+ | transaction_id   | int     | | customer_id      | int     | | transaction_date | date    | | amount           | decimal | | transaction_type | varchar | +------------------+---------+ transaction_id 是这张表的唯一主键。 transaction_type 可以是 “purchase” 或 “refund”。
编写一个解决方案来查找 忠实客户。如果满足下述所有条件，可以认为该客户是 忠实 客户：
进行了 至少 `3` 次购买交易。
活跃了 至少 `30` 天。
他们的 退款率 少于 `20%`。
退款率是退款交易占交易总数（购买加退款）的比例，计算公式为退款交易数量除以总交易数量。
返回结果表以 `customer_id` 升序 排序。
结果格式如下所示。

示例：

输入：
customer_transactions 表：
+----------------+-------------+------------------+--------+------------------+ | transaction_id | customer_id | transaction_date | amount | transaction_type | +----------------+-------------+------------------+--------+------------------+ | 1              | 101         | 2024-01-05       | 150.00 | purchase         | | 2              | 101         | 2024-01-15       | 200.00 | purchase         | | 3              | 101         | 2024-02-10       | 180.00 | purchase         | | 4              | 101         | 2024-02-20       | 250.00 | purchase         | | 5              | 102         | 2024-01-10       | 100.00 | purchase         | | 6              | 102         | 2024-01-12       | 120.00 | purchase         | | 7              | 102         | 2024-01-15       | 80.00  | refund           | | 8              | 102         | 2024-01-18       | 90.00  | refund           | | 9              | 102         | 2024-02-15       | 130.00 | purchase         | | 10             | 103         | 2024-01-01       | 500.00 | purchase         | | 11             | 103         | 2024-01-02       | 450.00 | purchase         | | 12             | 103         | 2024-01-03       | 400.00 | purchase         | | 13             | 104         | 2024-01-01       | 200.00 | purchase         | | 14             | 104         | 2024-02-01       | 250.00 | purchase         | | 15             | 104         | 2024-02-15       | 300.00 | purchase         | | 16             | 104         | 2024-03-01       | 350.00 | purchase         | | 17             | 104         | 2024-03-10       | 280.00 | purchase         | | 18             | 104         | 2024-03-15       | 100.00 | refund           | +----------------+-------------+------------------+--------+------------------+
输出：
+-------------+ | customer_id | +-------------+ | 101         | | 104         | +-------------+
解释：
客户 101:
购买交易：4 (IDs: 1, 2, 3, 4)
退款交易：0
退款率：0/4 = 0%（少于 20%）
活跃时期：1 月 5 日到 2 月 20 日 = 46 天（至少 30 天）
符合忠诚客户条件
客户 102:
购买交易：3 (IDs: 5, 6, 9)
退款交易：2 (IDs: 7, 8)
退款率：2/5 = 40% (超过 20%)
不符合忠诚客户条件
客户 103:
购买交易：3 (IDs: 10, 11, 12)
退款交易：0
退款率：0/3 = 0%（少于 20%）
活跃时期：1 月 1 日到 1 月 3 日 = 2 天（少于 30 天）
不符合忠诚客户条件
客户 104:
购买交易：5 (IDs: 13, 14, 15, 16, 17)
退款交易：1 (ID: 18)
退款率：1/6 = 16.67%（少于 20%）
活跃时期：1 月 1 日到 3 月 15 日 = 73 天（至少 30 天）
符合忠诚客户条件
结果表以 customer_id 升序排序。
"""

from typing import List, Optional


class Solution:
    def find_loyal_customers(self, customer_transactions: 'pd.DataFrame') -> 'pd.DataFrame':
        import pandas as pd

        # 按 customer_id 分组聚合
        agg = customer_transactions.groupby('customer_id').agg(
            purchase_count=('transaction_type', lambda x: (x == 'purchase').sum()),
            total_count=('transaction_id', 'count'),
            refund_count=('transaction_type', lambda x: (x == 'refund').sum()),
            min_date=('transaction_date', 'min'),
            max_date=('transaction_date', 'max')
        ).reset_index()

        # 活跃天数
        agg['active_days'] = (agg['max_date'] - agg['min_date']).dt.days

        # 退款率
        agg['refund_rate'] = agg['refund_count'] / agg['total_count']

        # 筛选条件
        loyal = agg[
            (agg['purchase_count'] >= 3) &
            (agg['active_days'] >= 30) &
            (agg['refund_rate'] < 0.2)
        ]

        # 返回 customer_id 升序
        result = loyal[['customer_id']].sort_values('customer_id').reset_index(drop=True)
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Pandas, Data Aggregation
#
# 解题思路:
# 使用 pandas groupby 对每位客户进行聚合：
# 1. 统计购买交易数 (transaction_type == 'purchase')
# 2. 统计总交易数和退款交易数
# 3. 计算最早和最晚交易日期，得到活跃天数
# 4. 计算退款率 = 退款数 / 总交易数
# 筛选满足三个条件的客户：
#   - 购买 >= 3 次
#   - 活跃 >= 30 天
#   - 退款率 < 20%
# 结果按 customer_id 升序排列。
#
# 时间复杂度: O(n) 其中 n 为交易记录数
# 空间复杂度: O(m) 其中 m 为客户数
#
# 关键点:
# - groupby 一次聚合所有统计量
# - 日期差用 .dt.days 获取天数
# - 退款率用浮点数比较，注意是严格小于 20%
