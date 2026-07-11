"""
LeetCode #1341 - Movie Rating
中文题名：电影评分
https://leetcode.com/problems/movie-rating/

SQL Schema

Table: `Movies`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key for this table.
title is the name of the movie.

Table: `Users`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key for this table.

Table: `Movie_Rating`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date.

Write the following SQL query:

Find the name of the user who has rated the greatest number of the movies.

In case of a tie, return lexicographically smaller user name.

Find the movie name with the highest average rating in February 2020.

In case of a tie, return lexicographically smaller movie name..

Query is returned in 2 rows, the query result format is in the folowing example:

Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+

Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+

Movie_Rating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  |
| 2           | 2            | 2            | 2020-02-01  |
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  |
| 3           | 2            | 4            | 2020-02-25  |
+-------------+--------------+--------------+-------------+

Result table:
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+

Daniel and Maria have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.

【中文翻译】
这是一个 SQL 数据库问题，需要编写 SQL 查询来返回两行结果。

有三张表：
- Movies 表（movie_id, title）：存储电影信息
- Users 表（user_id, name）：存储用户信息
- Movie_Rating 表（movie_id, user_id, rating, created_at）：存储用户对电影的评分和评分日期

查询要求：
1. 第一行：找出评价电影数量最多的用户姓名。如果并列，返回字典序较小的姓名。
2. 第二行：找出在 2020 年 2 月平均评分最高的电影名称。如果并列，返回字典序较小的电影名称。

示例：
Movies 表中，Daniel 和 Maria 都评价了 3 部电影（"Avengers"、"Frozen 2" 和 "Joker"），
但 Daniel 的字典序更小，所以返回 "Daniel"。
Frozen 2 和 Joker 在二月的平均评分都是 3.5，但 Frozen 2 的字典序更小，所以返回 "Frozen 2"。

SQL 参考解法：
(SELECT u.name AS results
 FROM Movie_Rating mr
 JOIN Users u ON mr.user_id = u.user_id
 GROUP BY mr.user_id
 ORDER BY COUNT(*) DESC, u.name ASC
 LIMIT 1)

UNION ALL

(SELECT m.title AS results
 FROM Movie_Rating mr
 JOIN Movies m ON mr.movie_id = m.movie_id
 WHERE mr.created_at >= '2020-02-01' AND mr.created_at <= '2020-02-29'
 GROUP BY mr.movie_id
 ORDER BY AVG(mr.rating) DESC, m.title ASC
 LIMIT 1);
"""

from typing import List, Optional


class Solution:
    def movieRating(
        self,
        movies: List[List],
        users: List[List],
        movie_rating: List[List]
    ) -> List[str]:
        """
        这是一个 SQL 问题。LeetCode 上此题期望用 SQL 解答，而非 Python。
        如需 Python 实现，请参考以下逻辑或使用 SQL 方案。

        SQL 参考解法：
        (SELECT u.name AS results
         FROM Movie_Rating mr
         JOIN Users u ON mr.user_id = u.user_id
         GROUP BY mr.user_id
         ORDER BY COUNT(*) DESC, u.name ASC
         LIMIT 1)
        UNION ALL
        (SELECT m.title AS results
         FROM Movie_Rating mr
         JOIN Movies m ON mr.movie_id = m.movie_id
         WHERE mr.created_at >= '2020-02-01' AND mr.created_at <= '2020-02-29'
         GROUP BY mr.movie_id
         ORDER BY AVG(mr.rating) DESC, m.title ASC
         LIMIT 1);
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
# SQL 问题，使用 UNION ALL 合并两个子查询：
# 1. 第一个子查询：从 Movie_Rating 和 Users 表联合查询，按 user_id 分组统计评分次数，
#    按评分次数降序排列，并列时按姓名字典序升序，取第一名。
# 2. 第二个子查询：从 Movie_Rating 和 Movies 表联合查询，筛选 2020 年 2 月的评分记录，
#    按 movie_id 分组计算平均评分，按平均分降序排列，并列时按电影名字典序升序，取第一名。
# 3. 用 UNION ALL 将两个结果合并为两行输出。
#
# 时间复杂度: O(N log N) — SQL 内部排序开销
# 空间复杂度: O(N) — 临时分组和排序的中间结果
#
# 关键点:
# - 使用 UNION ALL 而非 UNION，因为两行结果来自不同的逻辑，不会重复
# - 日期范围筛选：created_at 在 2020-02-01 到 2020-02-29 之间
# - 字典序排序使用 ASC，配合 LIMIT 1 自动取字典序最小的记录
# - COUNT(*) 统计每个用户的评分次数










