"""
LeetCode #3642 - Find Books with Polarized Opinions
查找有两极分化观点的书籍
https://leetcode.cn/problems/find-books-with-polarized-opinions/

表：`books`
+-------------+---------+ | Column Name | Type    | +-------------+---------+ | book_id     | int     | | title       | varchar | | author      | varchar | | genre       | varchar | | pages       | int     | +-------------+---------+ book_id 是这张表的唯一主键。 每一行包含关于一本书的信息，包括其类型和页数。
表：`reading_sessions`
+----------------+---------+ | Column Name    | Type    | +----------------+---------+ | session_id     | int     | | book_id        | int     | | reader_name    | varchar | | pages_read     | int     | | session_rating | int     | +----------------+---------+ session_id 是这张表的唯一主键。 每一行代表一次阅读事件，有人阅读了书籍的一部分。session_rating 在 1-5 的范围内。
编写一个解决方案来找到具有 两极分化观点 的书 - 同时获得不同读者极高和极低评分的书籍。
如果一本书有至少一个大于等于 `4` 的评分和至少一个小于等于 `2` 的评分则是有两极分化观点的书
只考虑有至少 `5` 次阅读事件的书籍
按 `highest_rating - lowest_rating` 计算评分差幅 rating spread
按极端评分（评分小于等于 `2` 或大于等于 `4`）的数量除以总阅读事件计算 极化得分 polarization score
只包含 极化得分大于等于 `0.6` 的书（至少 `60%` 极端评分）
返回结果表按极化得分 降序 排序，然后按标题 降序 排序。
极化得分应舍入到 2 位小数。
返回格式如下所示。

示例：

输入：
books 表：
+---------+------------------------+---------------+----------+-------+ | book_id | title                  | author        | genre    | pages | +---------+------------------------+---------------+----------+-------+ | 1       | The Great Gatsby       | F. Scott      | Fiction  | 180   | | 2       | To Kill a Mockingbird  | Harper Lee    | Fiction  | 281   | | 3       | 1984                   | George Orwell | Dystopian| 328   | | 4       | Pride and Prejudice    | Jane Austen   | Romance  | 432   | | 5       | The Catcher in the Rye | J.D. Salinger | Fiction  | 277   | +---------+------------------------+---------------+----------+-------+
reading_sessions 表：
+------------+---------+-------------+------------+----------------+ | session_id | book_id | reader_name | pages_read | session_rating | +------------+---------+-------------+------------+----------------+ | 1          | 1       | Alice       | 50         | 5              | | 2          | 1       | Bob         | 60         | 1              | | 3          | 1       | Carol       | 40         | 4              | | 4          | 1       | David       | 30         | 2              | | 5          | 1       | Emma        | 45         | 5              | | 6          | 2       | Frank       | 80         | 4              | | 7          | 2       | Grace       | 70         | 4              | | 8          | 2       | Henry       | 90         | 5              | | 9          | 2       | Ivy         | 60         | 4              | | 10         | 2       | Jack        | 75         | 4              | | 11         | 3       | Kate        | 100        | 2              | | 12         | 3       | Liam        | 120        | 1              | | 13         | 3       | Mia         | 80         | 2              | | 14         | 3       | Noah        | 90         | 1              | | 15         | 3       | Olivia      | 110        | 4              | | 16         | 3       | Paul        | 95         | 5              | | 17         | 4       | Quinn       | 150        | 3              | | 18         | 4       | Ruby        | 140        | 3              | | 19         | 5       | Sam         | 80         | 1              | | 20         | 5       | Tara        | 70         | 2              | +------------+---------+-------------+------------+----------------+
输出：
+---------+------------------+---------------+-----------+-------+---------------+--------------------+ | book_id | title            | author        | genre     | pages | rating_spread | polarization_score | +---------+------------------+---------------+-----------+-------+---------------+--------------------+ | 1       | The Great Gatsby | F. Scott      | Fiction   | 180   | 4             | 1.00               | | 3       | 1984             | George Orwell | Dystopian | 328   | 4             | 1.00               | +---------+------------------+---------------+-----------+-------+---------------+--------------------+
解释：
了不起的盖茨比（book_id = 1）：
有 5 次阅读事件（满足最少要求）
评分：5, 1, 4, 2, 5
大于等于 4 的评分：5，4，5（3 次事件）
小于等于 2 的评分：1，2（2 次事件）
评分差：5 - 1 = 4
极端评分（≤2 或 ≥4）：所有 5 次事件（5，1，4，2，5）
极化得分：5/5 = 1.00（≥ 0.6，符合）
1984 (book_id = 3):
有 6 次阅读事件（满足最少要求）
评分：2，1，2，1，4，5
大于等于 4 的评分：4，5（2 次事件）
小于等于 2 的评分：2，1，2，1（4 次事件）
评分差：5 - 1 = 4
极端评分（≤2 或 ≥4）：所有 6 次事件（2，1，2，1，4，5）
极化得分：6/6 = 1.00 (≥ 0.6，符合）
未包含的书：
杀死一只知更鸟（book_id = 2）：所有评分为 4-5，没有低分（≤2）
傲慢与偏见（book_id = 4）：只有 2 次事件（< 最少 5 次）
麦田里的守望者（book_id = 5）：只有 2 次事件（< 最少 5 次）
结果表按极化得分降序排序，然后按标题降序排序。
"""

from typing import List, Optional
import pandas as pd


class Solution:
    def findPolarizedBooks(self, books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
        # 按 book_id 聚合阅读会话
        stats = reading_sessions.groupby('book_id').agg(
            total_sessions=('session_id', 'count'),
            high_ratings=('session_rating', lambda x: (x >= 4).sum()),
            low_ratings=('session_rating', lambda x: (x <= 2).sum()),
            max_rating=('session_rating', 'max'),
            min_rating=('session_rating', 'min'),
        ).reset_index()

        # 过滤：至少 5 次阅读事件
        stats = stats[stats['total_sessions'] >= 5]
        if stats.empty:
            return pd.DataFrame(columns=['book_id', 'title', 'author', 'genre', 'pages',
                                         'rating_spread', 'polarization_score'])

        # 过滤：至少一个 >=4 且一个 <=2 的评分
        stats = stats[(stats['high_ratings'] >= 1) & (stats['low_ratings'] >= 1)]
        if stats.empty:
            return pd.DataFrame(columns=['book_id', 'title', 'author', 'genre', 'pages',
                                         'rating_spread', 'polarization_score'])

        # 计算 rating_spread
        stats['rating_spread'] = stats['max_rating'] - stats['min_rating']

        # 计算极化得分：极端评分占比，保留 2 位小数
        stats['polarization_score'] = (
            (stats['high_ratings'] + stats['low_ratings']) / stats['total_sessions']
        ).round(2)

        # 过滤：极化得分 >= 0.6
        stats = stats[stats['polarization_score'] >= 0.6]

        # 关联 books 表获取书籍信息
        result = stats.merge(books[['book_id', 'title', 'author', 'genre', 'pages']], on='book_id')

        # 排序：极化得分降序，标题降序
        result = result.sort_values(
            by=['polarization_score', 'title'],
            ascending=[False, False]
        )

        return result[['book_id', 'title', 'author', 'genre', 'pages',
                       'rating_spread', 'polarization_score']]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Pandas, Aggregation, Filtering
#
# 解题思路:
# 使用 pandas 对 reading_sessions 按 book_id 进行聚合统计：
# 1. 统计每本书的总阅读次数、高评分次数(>=4)、低评分次数(<=2)、最高分和最低分
# 2. 过滤条件：总次数>=5，至少有1个高评分和1个低评分，极化得分>=0.6
# 3. 极化得分 = (高评分数 + 低评分数) / 总次数，保留2位小数
# 4. rating_spread = max_rating - min_rating
# 5. 关联 books 表获取书籍详情，按极化得分和标题降序排序
#
# 时间复杂度: O(N log N)，N 为 reading_sessions 行数
# 空间复杂度: O(N)
#
# 关键点:
# - 极端评分定义为 <=2 或 >=4
# - 极化得分是极端评分占总评分的比例
# - 结果需按极化得分降序、标题降序排列
