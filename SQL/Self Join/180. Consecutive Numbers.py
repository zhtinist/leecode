"""
LeetCode #180 - Consecutive Numbers
中文题名：连续出现的数字
https://leetcode.com/problems/consecutive-numbers/

Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+

For example, given the above `Logs` table, `1` is the only number that
appears consecutively for at least three times.

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+

【中文翻译】
编写一个 SQL 查询，查找所有至少连续出现三次的数字。

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+

例如，给定上面的 `Logs` 表，`1` 是唯一连续出现至少三次的数字。

+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
"""

from typing import List, Optional


class Solution:
    def findConsecutiveNumbers(self):
        """
        SQL Solution:
            SELECT DISTINCT l1.Num AS ConsecutiveNums
            FROM Logs l1
            JOIN Logs l2 ON l1.Id = l2.Id - 1
            JOIN Logs l3 ON l2.Id = l3.Id - 1
            WHERE l1.Num = l2.Num AND l2.Num = l3.Num;
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
# 自连接三张Logs表，通过 Id+1 关系确保连续性。
# l1.Id = l2.Id - 1 AND l2.Id = l3.Id - 1 确保三行ID连续。
# WHERE l1.Num = l2.Num AND l2.Num = l3.Num 确保值相同。
# DISTINCT 去除可能的重复输出。
#
# 时间复杂度: O(N) — 合理索引下
# 空间复杂度: O(1)
#
# 关键点:
# - 连续出现至少3次 = 三行连续且值相同
# - JOIN条件用Id差值而非Num比较
# - DISTINCT避免重复
