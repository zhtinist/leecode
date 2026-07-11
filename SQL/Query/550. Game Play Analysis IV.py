"""
LeetCode #550 - Game Play Analysis IV
中文题名：游戏玩法分析 IV
https://leetcode.com/problems/game-play-analysis-iv/

Table: `Activity`

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key of this table.
This table shows the activity of players of some game.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some day using some device.

Write an SQL query that reports the fraction of players that logged in again
on the day after the day they first logged in, rounded to 2 decimal
places. In other words, you need to count the number of players that
logged in for at least two consecutive days starting from their first login date, then
divide that number by the total number of players.

The query result format is in the following example:

Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33

【中文翻译】
编写一个 SQL 查询，报告在首次登录的第二天再次登录的玩家比率，四舍五入到小数点后两位。
换句话说，需要统计从首次登录日期开始至少连续两天登录的玩家数量，然后除以玩家总数。

表 `Activity`：

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) 是此表的主键。
该表显示了某些游戏的玩家活动。每一行是一个玩家在某天使用某个设备登录并玩了一定数量游戏（可能为 0）的记录。

示例输入（Activity 表）：
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

输出：
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+

解释：只有 ID 为 1 的玩家在首次登录后第二天又登录了，所以答案为 1/3 ≈ 0.33
"""

from typing import List, Optional


class Solution:
    def gameplayAnalysisIV(self, activities: List[dict]) -> Optional[float]:
        """
        SQL Solution:
            SELECT ROUND(
                COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2
            ) AS fraction
            FROM Activity a
            WHERE (a.player_id, a.event_date) IN (
                SELECT player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
                FROM Activity
                GROUP BY player_id
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
# 两步走：首先找出每个玩家的首次登录日期（MIN(event_date) GROUP BY player_id），
# 然后检查该玩家在首次登录日期的后一天（DATE_ADD）是否有登录记录。
# 使用子查询找到所有在次日登录的玩家，除以玩家总数得到比率，用 ROUND 保留两位小数。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)（子查询临时结果集）
#
# 关键点:
# - 使用 MIN(event_date) + GROUP BY 获取每个玩家的首次登录日期
# - DATE_ADD(first_date, INTERVAL 1 DAY) 计算次日日期
# - 分子用 DISTINCT 避免同一玩家多次匹配
# - ROUND(x, 2) 保留两位小数，符合题目要求
