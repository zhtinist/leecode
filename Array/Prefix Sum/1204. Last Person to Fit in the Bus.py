"""
LeetCode #1204 - Last Person to Fit in the Bus
中文题名：最后一个能进入电梯的人
https://leetcode.com/problems/last-person-to-fit-in-the-bus/

Table: `Queue`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id is the primary key column for this table.
This table has the information about all people waiting for an elevator.
The `person_id` and `turn` columns will contain all numbers from 1 to n, where n is the number of rows in the table.

The maximum weight the elevator can hold is 1000.

Write an SQL query to find the `person_name` of the last person who will fit
in the elevator without exceeding the weight limit. It is guaranteed that the person who is first
in the queue can fit in the elevator.

The query result format is in the following example:

Queue table
+-----------+-------------------+--------+------+
| person_id | person_name       | weight | turn |
+-----------+-------------------+--------+------+
| 5         | George Washington | 250    | 1    |
| 3         | John Adams        | 350    | 2    |
| 6         | Thomas Jefferson  | 400    | 3    |
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Thomas Jefferson  | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |
+-----------+-------------------+--------+------+

Result table
+-------------------+
| person_name       |
+-------------------+
| Thomas Jefferson  |
+-------------------+

Queue table is ordered by turn in the example for simplicity.
In the example George Washington(id 5), John Adams(id 3) and Thomas Jefferson(id 6) will enter the elevator as their weight sum is 250 + 350 + 400 = 1000.
Thomas Jefferson(id 6) is the last person to fit in the elevator because he has the last turn in these three people.

【中文翻译】
表：Queue

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id 是该表的主键。
该表包含所有等待电梯的人的信息。
person_id 和 turn 列包含从 1 到 n 的所有数字，其中 n 是表中的行数。

电梯最大载重量为 1000。

编写一个 SQL 查询，找出最后一个能进入电梯且不超过重量限制的人的 person_name。题目保证队列中第一个人可以进入电梯。

查询结果格式如下例所示：

Queue 表：
+-----------+-------------------+--------+------+
| person_id | person_name       | weight | turn |
+-----------+-------------------+--------+------+
| 5         | George Washington | 250    | 1    |
| 3         | John Adams        | 350    | 2    |
| 6         | Thomas Jefferson  | 400    | 3    |
| 2         | Will Johnliams    | 200    | 4    |
| 4         | Thomas Jefferson  | 175    | 5    |
| 1         | James Elephant    | 500    | 6    |
+-----------+-------------------+--------+------+

结果表：
+-------------------+
| person_name       |
+-------------------+
| Thomas Jefferson  |
+-------------------+

为了简化，Queue 表按 turn 列由小到大排序。
上例中 George Washington（id 5），John Adams（id 3）和 Thomas Jefferson（id 6）将进入电梯，因为他们的体重和为 250 + 350 + 400 = 1000。
Thomas Jefferson（id 6）是最后一个能进入电梯的人，因为他在他们三人中 turn 最大。

"""

from typing import List, Optional


class Solution:
    """
    SQL Solution (submit this in LeetCode SQL editor):

    SELECT person_name
    FROM (
        SELECT person_name, turn,
               SUM(weight) OVER (ORDER BY turn) AS running_weight
        FROM Queue
    ) t
    WHERE running_weight <= 1000
    ORDER BY turn DESC
    LIMIT 1;
    """










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题需要找到累计重量不超过 1000 的最后一个人。
# 使用窗口函数 SUM() OVER (ORDER BY turn) 计算按 turn 排序的累计重量（运行总和）。
# 然后筛选出累计重量 <= 1000 的行，按 turn 降序排列取第一条即为最后进入的人。
#
# 具体步骤：
# 1. 子查询：按 turn 顺序计算 running_weight = SUM(weight) OVER (ORDER BY turn)
# 2. 外层查询：WHERE running_weight <= 1000 筛选不超重的记录
# 3. ORDER BY turn DESC LIMIT 1 取最后一条（即 turn 最大的满足条件的记录）
#
# 时间复杂度: O(n log n) - 窗口函数需要排序
# 空间复杂度: O(n) - 子查询中间结果
#
# 关键点:
# - 窗口函数 SUM() OVER (ORDER BY turn) 实现累计求和（前缀和）
# - 筛选 running_weight <= 1000 得到所有能进入电梯的人
# - ORDER BY turn DESC LIMIT 1 取最后一个满足条件的记录
# - 题目保证第一个人能进入电梯（running_weight 至少有一个 <= 1000）
