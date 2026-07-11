"""
LeetCode #1907 - Count Salary Categories
按分类统计薪水
https://leetcode.cn/problems/count-salary-categories/

表: `Accounts`
+-------------+------+ | 列名        | 类型  | +-------------+------+ | account_id  | int  | | income      | int  | +-------------+------+ 在 SQL 中，account_id 是这个表的主键。 每一行都包含一个银行帐户的月收入的信息。

查询每个工资类别的银行账户数量。 工资类别如下：
`"Low Salary"`：所有工资 严格低于 `20000` 美元。
`"Average Salary"`： 包含 范围内的所有工资 `[$20000, $50000]` 。

`"High Salary"`：所有工资 严格大于 `50000` 美元。
结果表 必须 包含所有三个类别。 如果某个类别中没有帐户，则报告 `0` 。
按 任意顺序 返回结果表。
查询结果格式如下示例。

示例 1：
输入： Accounts 表: +------------+--------+ | account_id | income | +------------+--------+ | 3          | 108939 | | 2          | 12747  | | 8          | 87709  | | 6          | 91796  | +------------+--------+ 输出： +----------------+----------------+ | category       | accounts_count | +----------------+----------------+ | Low Salary     | 1              | | Average Salary | 0              | | High Salary    | 3              | +----------------+----------------+ 解释： 低薪: 有一个账户 2. 中等薪水: 没有. 高薪: 有三个账户，他们是 3, 6和 8.
"""

from typing import List, Optional


import pandas as pd




# Note: This is a SQL problem on LeetCode. The Python solution below
# demonstrates the logic using pandas for reference.
# Actual LeetCode submission should be in SQL.

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_count = (accounts['income'] < 20000).sum()
    avg_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_count = (accounts['income'] > 50000).sum()

    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_count, avg_count, high_count]
    })
    return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 数据库
#
# 解题思路:
# 这是一个 SQL 问题（LeetCode 数据库题），非算法题。
# 如果使用 Python/pandas 解决：
# 1. 按收入范围分类统计账户数量。
# 2. 三个类别都必须出现在结果中，即使计数为 0。
# 3. 使用条件筛选和计数完成统计。
#
# SQL 解题思路：
# 使用 UNION ALL 组合三个类别，用 CASE WHEN 或条件聚合统计。
#
# 时间复杂度: O(n) — 遍历所有账户
# 空间复杂度: O(1) — 结果固定大小
#
# 关键点:
# - 该题是数据库题，LeetCode 上需用 SQL 提交
# - 所有三个类别必须出现在结果中（即使数量为 0）
# - 分类边界：Low < 20000, Average [20000, 50000], High > 50000
