"""
LeetCode #570 - Managers with at Least 5 Direct Reports
中文题名：至少有5名直接下属的经理
https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

The `Employee` table holds all employees including their managers. Every employee
has an Id, and there is also a column for the manager Id.

+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+

Given the `Employee` table, write a SQL query that finds out managers with at
least 5 direct report. For the above table, your SQL query should return:

+-------+
| Name  |
+-------+
| John  |
+-------+

Note:

No one would report to himself.

【中文翻译】
编写一个 SQL 查询，找出至少有 5 名直接下属的经理。

`Employee` 表包含所有员工及其经理的信息。每个员工都有一个 Id，此外还有一列对应其经理的 Id。

+------+----------+-----------+----------+
|Id    |Name      |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John      |A          |null      |
|102   |Dan       |A          |101       |
|103   |James     |A          |101       |
|104   |Amy       |A          |101       |
|105   |Anne      |A          |101       |
|106   |Ron       |B          |101       |
+------+----------+-----------+----------+

对于上表，SQL 查询应返回：

+-------+
| Name  |
+-------+
| John  |
+-------+

注意：没有人会向自己汇报。
"""

from typing import List, Optional


class Solution:
    def managersWithAtLeast5DirectReports(self, employees: List[dict]) -> List[str]:
        """
        SQL Solution:
            SELECT Name
            FROM Employee
            WHERE Id IN (
                SELECT ManagerId
                FROM Employee
                GROUP BY ManagerId
                HAVING COUNT(*) >= 5
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
# 按 ManagerId 分组统计每个经理有多少直接下属，HAVING COUNT(*) >= 5 筛选出满足条件的经理。
# 再用子查询结果与 Employee 表关联，通过 Id 匹配获取经理姓名。
# 也可以用自连接（JOIN）实现，但子查询更直观。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)（子查询临时结果集）
#
# 关键点:
# - GROUP BY ManagerId 统计每个经理的下属数量
# - HAVING COUNT(*) >= 5 筛选至少5名下属的经理
# - 注意排除 ManagerId 为 NULL 的行（没有经理的员工不应被计入分组）
