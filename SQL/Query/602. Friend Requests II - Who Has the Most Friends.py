"""
LeetCode #602 - Friend Requests II: Who Has the Most Friends
中文题名：好友请求 II：谁拥有最多好友
https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

In social network like Facebook or Twitter, people send friend requests and accept others'
requests as well.

Table `request_accepted` holds the data of friend acceptance, while
requester_id and accepter_id both are the id of a person.

| requester_id | accepter_id | accept_date|
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |

Write a query to find the the people who has most friends and the most friends number. For the
sample data above, the result is:

| id | num |
|----|-----|
| 3  | 3   |

Note:

It is guaranteed there is only 1 people having the most friends.

The friend request could only been accepted once, which mean there is no multiple
records with the same requester_id and accepter_id value.

Explanation:

The person with id '3' is a friend of people '1', '2' and '4',
so he has 3 friends in total, which is the most number than any others.

Follow-up:

In the real world, multiple people could have the same most number of friends, can you
find all these people in this case?

【中文翻译】
在像 Facebook 或 Twitter 这样的社交网络中，人们可以发送好友请求并接受他人的好友请求。

表 `request_accepted` 存储了通过好友请求的数据，
其中 requester_id 和 accepter_id 都是用户的 ID。

| requester_id | accepter_id | accept_date|
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |

编写一个 SQL 查询，找出拥有好友数量最多的用户及其好友数量。根据上面的示例数据，结果如下：

| id | num |
|----|-----|
| 3  | 3   |

注意：

保证只有 1 个人拥有最多的好友。

每个好友请求只会被接受一次，也就是说不会有重复的 requester_id 和 accepter_id 记录。

解释：

用户 id 为 '3' 的人与用户 '1'、'2' 和 '4' 是好友，
所以他总共有 3 个好友，比任何人都多。

Follow-up：

在现实生活中，可能有多个人拥有相同的最多好友数量，你能在这个情况下找出所有这些人吗？
"""

from typing import List, Optional


class Solution:
    """
    SQL Solution:

    SELECT id, COUNT(*) AS num
    FROM (
        SELECT requester_id AS id FROM request_accepted
        UNION ALL
        SELECT accepter_id AS id FROM request_accepted
    ) t
    GROUP BY id
    ORDER BY num DESC
    LIMIT 1;

    -- Follow-up: find all people with the same max friends
    WITH friend_count AS (
        SELECT id, COUNT(*) AS num
        FROM (
            SELECT requester_id AS id FROM request_accepted
            UNION ALL
            SELECT accepter_id AS id FROM request_accepted
        ) t
        GROUP BY id
    )
    SELECT id, num
    FROM friend_count
    WHERE num = (SELECT MAX(num) FROM friend_count);
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
# 一个用户的好友包括两种关系：他发送请求给别人，或别人发请求给他。
# 因此我们可以用 UNION ALL 将两种关系合并为一张表，然后 GROUP BY id 统计每个用户的出现次数（即好友数），
# 最后按好友数降序排序并取第一条。
# 对于 Follow-up（可能有多人并列最多好友），先用 CTE 计算每个用户的好友数，
# 然后筛选出好友数等于最大值的所有用户。
#
# 时间复杂度: O(n log n) - n 为 request_accepted 表的行数，主要在于排序
# 空间复杂度: O(n) - 存储中间结果
#
# 关键点:
# - 使用 UNION ALL（而非 UNION）因为可能存在重复记录
# - requester 和 accepter 都是好友关系，都要计入好友数
# - 对于 Follow-up，使用子查询或 CTE 找出最大值
