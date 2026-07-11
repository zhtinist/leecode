"""
LeetCode #177 - Nth Highest Salary
中文题名：第N高的薪水
https://leetcode.com/problems/nth-highest-salary/

Write a SQL query to get the nth highest salary from the
`Employee` table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the nth highest salary where
n = 2 is `200`. If there is no nth highest salary,
then the query should return `null`.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

【中文翻译】
编写一个 SQL 查询，获取 `Employee` 表中第 n 高的薪水（Salary）。

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

例如上述 `Employee` 表，n = 2 时，应返回第二高的薪水，即 `200`。
如果不存在第 n 高的薪水，那么查询应返回 `null`。

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
"""

from typing import List, Optional


class Solution:
    def getNthHighestSalary(self, salaries: List[int], n: int) -> Optional[int]:
        """
        SQL Solution:
            CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
            BEGIN
              SET N = N - 1;
              RETURN (
                SELECT DISTINCT Salary FROM Employee
                ORDER BY Salary DESC
                LIMIT 1 OFFSET N
              );
            END
            
        Python equivalent:
        """
        distinct_sorted = sorted(set(salaries), reverse=True)
        if n > len(distinct_sorted):
            return None
        return distinct_sorted[n - 1]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# SQL解法：使用 LIMIT 1 OFFSET N-1 跳过前N-1条记录取第N条。
# 需要用 CREATE FUNCTION 创建函数，通过 SET N = N - 1 调整偏移量。
# Python解法：去重后降序排序，取索引 n-1 的元素。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(N)
#
# 关键点:
# - SQL用LIMIT+OFFSET实现第N高
# - 必须DISTINCT去重
# - 处理N超出范围返回NULL
