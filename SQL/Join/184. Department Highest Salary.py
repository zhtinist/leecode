"""
LeetCode #184 - Department Highest Salary
中文题名：部门工资最高的员工
https://leetcode.com/problems/department-highest-salary/

The `Employee` table holds all employees. Every employee has an Id, a salary, and
there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+

The `Department` table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

Write a SQL query to find employees who have the highest salary in each of the departments. For
the above tables, your SQL query should return the following rows (order of rows does not
matter).

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

Explanation:

Max and Jim both have the highest salary in the IT department and Henry has the highest
salary in the Sales department.

【中文翻译】
`Employee` 表包含所有员工信息，每个员工有其对应的 Id、Salary 和 DepartmentId。

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+

`Department` 表包含公司所有部门的信息。

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+

编写一个 SQL 查询，找出每个部门中工资最高的员工。对于上述表格，你的 SQL 查询应返回以下行（行的顺序不重要）。

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

解释：Max 和 Jim 在 IT 部门的工资都是最高的，Henry 在 Sales 部门的工资是最高的。
"""

from typing import List, Optional


class Solution:
    def departmentHighestSalary(self):
        """
        SQL Solution:
            SELECT d.Name AS Department, e.Name AS Employee, e.Salary
            FROM Employee e
            JOIN Department d ON e.DepartmentId = d.Id
            WHERE (e.DepartmentId, e.Salary) IN (
                SELECT DepartmentId, MAX(Salary)
                FROM Employee
                GROUP BY DepartmentId
            );
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
# 先按DepartmentId分组找出每部门最高工资（子查询），
# 再用 (DepartmentId, Salary) IN 子查询筛选符合条件的员工。
# 也可使用窗口函数 RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC)
# 更简洁且支持并列最高。
#
# 时间复杂度: O(N) — 合理索引下
# 空间复杂度: O(N)
#
# 关键点:
# - 多列IN子查询确保部门+工资同时匹配
# - 并列最高工资员工都需要输出
# - 窗口函数方案更可读
