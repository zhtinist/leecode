"""
LeetCode #3220 - Odd and Even Transactions
奇数和偶数交易
https://leetcode.cn/problems/odd-and-even-transactions/

表：`transactions`
+------------------+------+ | Column Name      | Type |  +------------------+------+ | transaction_id   | int  | | amount           | int  | | transaction_date | date | +------------------+------+ transactions_id 列唯一标识了表中的每一行。 这张表的每一行包含交易 id，金额总和和交易日期。
编写一个解决方案来查找每天 奇数 交易金额和 偶数 交易金额的 总和。如果某天没有奇数或偶数交易，显示为 `0`。
返回结果表以 `transaction_date` 升序 排序。
结果格式如下所示。

示例：

输入：
`transactions` 表：
+----------------+--------+------------------+ | transaction_id | amount | transaction_date | +----------------+--------+------------------+ | 1              | 150    | 2024-07-01       | | 2              | 200    | 2024-07-01       | | 3              | 75     | 2024-07-01       | | 4              | 300    | 2024-07-02       | | 5              | 50     | 2024-07-02       | | 6              | 120    | 2024-07-03       | +----------------+--------+------------------+
输出：
+------------------+---------+----------+ | transaction_date | odd_sum | even_sum | +------------------+---------+----------+ | 2024-07-01       | 75      | 350      | | 2024-07-02       | 0       | 350      | | 2024-07-03       | 0       | 120      | +------------------+---------+----------+
解释：
对于交易日期：
2024-07-01:
奇数交易金额总和：75
偶数交易金额总和：150 + 200 = 350
2024-07-02:
奇数交易金额总和：0
偶数交易金额总和：300 + 50 = 350
2024-07-03:
奇数交易金额总和：0
偶数交易金额总和：120
注意：输出表以 `transaction_date` 升序排序。
"""

from typing import List, Optional


class Solution:
    def odd_even_transactions(self, transactions: List[List]) -> List[List]:
        """
        transactions: list of [transaction_id, amount, transaction_date]
        returns: list of [transaction_date, odd_sum, even_sum]
        """
        from collections import defaultdict
        odd = defaultdict(int)
        even = defaultdict(int)
        dates = set()
        for _, amount, date in transactions:
            dates.add(date)
            if amount % 2 == 1:
                odd[date] += amount
            else:
                even[date] += amount
        result = []
        for date in sorted(dates):
            result.append([date, odd.get(date, 0), even.get(date, 0)])
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 数据库
#
# 解题思路:
# SQL 问题在 Python 中的等价实现。
# 遍历交易记录，根据金额的奇偶性分别累加到对应日期的 odd_sum 和 even_sum。
# 使用字典按日期分组统计，最后按日期升序输出。
# SQL 等价写法：
# SELECT transaction_date,
#   SUM(CASE WHEN amount % 2 = 1 THEN amount ELSE 0 END) AS odd_sum,
#   SUM(CASE WHEN amount % 2 = 0 THEN amount ELSE 0 END) AS even_sum
# FROM transactions GROUP BY transaction_date ORDER BY transaction_date;
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 按日期分组聚合
# - 区分奇偶金额分别求和
# - 某天无奇数/偶数交易时显示 0
