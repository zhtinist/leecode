"""
LeetCode #626 - Exchange Seats
中文题名：换座位
https://leetcode.com/problems/exchange-seats/

Mary is a teacher in a middle school and she has a table `seat` storing students'
names and their corresponding seat ids.

The column id is continuous increment.

Mary wants to change seats for the adjacent students.

Can you write a SQL query to output the result for Mary?

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+

For the sample input, the output is:

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+

Note:

If the number of students is odd, there is no need to change the last one's seat.

【中文翻译】
Mary 是一名中学老师，她有一张名为 `seat` 的表，存储了学生姓名和对应的座位 ID。

id 列是连续递增的。

Mary 想要交换相邻的学生座位。

你能编写一个 SQL 查询来输出 Mary 想要的结果吗？

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+

对于上述示例输入，输出为：

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+

注意：

如果学生人数是奇数，则不需要改变最后一个学生的座位。
"""

from typing import List, Optional


class Solution:
    """
    SQL Solution:

    SELECT
        CASE
            WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM seat) THEN id
            WHEN id % 2 = 1 THEN id + 1
            ELSE id - 1
        END AS id,
        student
    FROM seat
    ORDER BY id;
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
# 使用 CASE WHEN 判断：
# - 如果 id 是奇数且它是最后一条记录（即最大 id），则保持不变。
# - 如果 id 是奇数（但不是最后一条），则 id 加 1（向右交换）。
# - 如果 id 是偶数，则 id 减 1（向左交换）。
# 最后按 id 排序即可。
#
# 时间复杂度: O(n log n) - n 为 seat 表的行数
# 空间复杂度: O(n)
#
# 关键点:
# - 核心逻辑：奇偶交换座位
# - 奇数最后一位不交换
# - 使用 CASE WHEN 而不是复杂的子查询
# - 输出按 id 排序
