"""
LeetCode #176 - Second Highest Salary
中文题名：第二高的薪水
https://leetcode.com/problems/second-highest-salary/

Write a SQL query to get the second highest salary from the `Employee` table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the query should return `200` as the
second highest salary. If there is no second highest salary, then the query should return
`null`.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

【中文翻译】
编写一个 SQL 查询，获取 `Employee` 表中第二高的薪水（Salary）。

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

例如上述 `Employee` 表，SQL 查询应该返回 `200` 作为第二高的薪水。
如果不存在第二高的薪水，那么查询应返回 `null`。

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
"""

from typing import List, Optional


class Solution:
    def secondHighestSalary(self, employees: List[dict]) -> Optional[int]:
        """
        SQL Solution:
            SELECT MAX(Salary) AS SecondHighestSalary
            FROM Employee
            WHERE Salary < (SELECT MAX(Salary) FROM Employee);
        """
        pass


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用子查询：先查出最高工资 SELECT MAX(Salary)，再查询低于最高工资的最大值。
# 如果不存在第二高工资（所有员工工资相同或只有一条记录），MAX 会返回 NULL。
# 也可使用 OFFSET: SELECT DISTINCT Salary ORDER BY Salary DESC LIMIT 1 OFFSET 1
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - MAX + 子查询 或 LIMIT OFFSET 两种方式
# - 注意处理没有第二高工资的情况，应返回 NULL 而非空
# - DISTINCT 确保不同工资值只计一次
