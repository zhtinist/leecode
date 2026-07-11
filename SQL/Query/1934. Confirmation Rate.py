"""
LeetCode #1934 - Confirmation Rate
确认率
https://leetcode.cn/problems/confirmation-rate/

表: `Signups`
+----------------+----------+ | Column Name    | Type     | +----------------+----------+ | user_id        | int      | | time_stamp     | datetime | +----------------+----------+ User_id是该表的主键。 每一行都包含ID为user_id的用户的注册时间信息。

表: `Confirmations`
+----------------+----------+ | Column Name    | Type     | +----------------+----------+ | user_id        | int      | | time_stamp     | datetime | | action         | ENUM     | +----------------+----------+ (user_id, time_stamp)是该表的主键。 user_id是一个引用到注册表的外键。 action是类型为('confirmed'， 'timeout')的ENUM 该表的每一行都表示ID为user_id的用户在time_stamp请求了一条确认消息，该确认消息要么被确认('confirmed')，要么被过期('timeout')。

用户的 确认率 是 `'confirmed'` 消息的数量除以请求的确认消息的总数。没有请求任何确认消息的用户的确认率为 `0` 。确认率四舍五入到 小数点后两位 。
编写一个SQL查询来查找每个用户的 确认率 。

以 任意顺序 返回结果表。

查询结果格式如下所示。

示例1:
输入： Signups 表: +---------+---------------------+ | user_id | time_stamp          | +---------+---------------------+ | 3       | 2020-03-21 10:16:13 | | 7       | 2020-01-04 13:57:59 | | 2       | 2020-07-29 23:09:44 | | 6       | 2020-12-09 10:39:37 | +---------+---------------------+ Confirmations 表: +---------+---------------------+-----------+ | user_id | time_stamp          | action    | +---------+---------------------+-----------+ | 3       | 2021-01-06 03:30:46 | timeout   | | 3       | 2021-07-14 14:00:00 | timeout   | | 7       | 2021-06-12 11:57:29 | confirmed | | 7       | 2021-06-13 12:58:28 | confirmed | | 7       | 2021-06-14 13:59:27 | confirmed | | 2       | 2021-01-22 00:00:00 | confirmed | | 2       | 2021-02-28 23:59:59 | timeout   | +---------+---------------------+-----------+ 输出:  +---------+-------------------+ | user_id | confirmation_rate | +---------+-------------------+ | 6       | 0.00              | | 3       | 0.00              | | 7       | 1.00              | | 2       | 0.50              | +---------+-------------------+ 解释: 用户 6 没有请求任何确认消息。确认率为 0。 用户 3 进行了 2 次请求，都超时了。确认率为 0。 用户 7 提出了 3 个请求，所有请求都得到了确认。确认率为 1。 用户 2 做了 2 个请求，其中一个被确认，另一个超时。确认率为 1 / 2 = 0.5。
"""

from typing import List, Optional


class Solution:
    def confirmationRate(self, signups: List[List], confirmations: List[List]) -> List[List]:
        """
        signups: [[user_id, time_stamp], ...]
        confirmations: [[user_id, time_stamp, action], ...]
        return: [[user_id, confirmation_rate], ...]
        """
        from collections import defaultdict

        user_total = defaultdict(int)
        user_confirmed = defaultdict(int)

        for user_id, _, action in confirmations:
            user_total[user_id] += 1
            if action == "confirmed":
                user_confirmed[user_id] += 1

        result = []
        for user_id, _ in signups:
            total = user_total[user_id]
            confirmed = user_confirmed[user_id]
            if total == 0:
                rate = 0.00
            else:
                rate = round(confirmed / total, 2)
            result.append([user_id, rate])

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 数据库, Hash Table
#
# 解题思路:
# 使用两个字典分别记录每个用户的确认消息总数和确认成功数。
# 遍历 confirmations 表，累计每个用户的总请求数和 confirmed 数量。
# 然后遍历 signups 表，计算每个用户的确认率：confirmed / total。
# 没有请求的用户确认率为 0。结果四舍五入保留两位小数。
#
# 时间复杂度: O(N + M)，其中 N 为 signups 长度，M 为 confirmations 长度
# 空间复杂度: O(N)，存储每个用户的统计数据
#
# 关键点:
# - 使用 defaultdict 避免键不存在的判断
# - 没有确认请求的用户确认率为 0，不是 NULL
# - 结果需要四舍五入到小数点后两位
