"""
LeetCode #178 - Rank Scores
中文题名：分数排名
https://leetcode.com/problems/rank-scores/

Write a SQL query to rank scores. If there is a tie between two scores, both should have the
same ranking. Note that after a tie, the next ranking number should be the next consecutive
integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

For example, given the above `Scores` table, your query should generate the
following report (order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+

【中文翻译】
编写一个 SQL 查询来实现分数排名。如果两个分数相同，则两个分数排名（Rank）相同。
请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，排名之间不应该有"间隔"。

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+

例如，根据上述给定的 `Scores` 表，你的查询应该生成以下报告（按最高分排序）：

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
"""

from typing import List, Optional


class Solution:
    def rankScores(self):
        """
        SQL Solution:
            SELECT Score,
                   DENSE_RANK() OVER (ORDER BY Score DESC) AS \`Rank\`
            FROM Scores
            ORDER BY Score DESC;
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
# 使用窗口函数 DENSE_RANK() OVER (ORDER BY Score DESC)。
# DENSE_RANK 与 RANK 的区别：分数相同时排名相同，且不跳过排名数字（连续排名）。
# 例如两个并列第一后，下一个是第二而非第三。
#
# 时间复杂度: O(N log N) — 排序
# 空间复杂度: O(N)
#
# 关键点:
# - DENSE_RANK vs RANK vs ROW_NUMBER
# - 按Score DESC降序排名
# - 连续排名，无空洞
