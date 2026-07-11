"""
LeetCode #3808 - Find Emotionally Consistent Users
寻找情绪一致的用户
https://leetcode.cn/problems/find-emotionally-consistent-users/

表：`reactions`
+--------------+---------+ | Column Name  | Type    | +--------------+---------+ | user_id      | int     | | content_id   | int     | | reaction     | varchar | +--------------+---------+ (user_id, content_id) 是这张表的主键（值互不相同）。 每一行代表用户对某条内容的反应。
根据以下要求编写一个解决方案，以识别 情绪一致的用户：
为每个用户统计他们发送的总反应次数。
仅包含 至少对 `5` 个不同内容项 作出反应的用户。
如果用户 至少 `60%` 的反应属于 同一种类型，则认为其 情绪一致。
返回结果表按 `reaction_ratio` 降序 排序，然后按 `user_id` 升序 排序。
注意：
`reaction_ratio` 应该舍入到 `2` 位小数
结果格式如下所示。

示例：

输入：
reactions 表：
+---------+------------+----------+ | user_id | content_id | reaction | +---------+------------+----------+ | 1       | 101        | like     | | 1       | 102        | like     | | 1       | 103        | like     | | 1       | 104        | wow      | | 1       | 105        | like     | | 2       | 201        | like     | | 2       | 202        | wow      | | 2       | 203        | sad      | | 2       | 204        | like     | | 2       | 205        | wow      | | 3       | 301        | love     | | 3       | 302        | love     | | 3       | 303        | love     | | 3       | 304        | love     | | 3       | 305        | love     | +---------+------------+----------+
输出：
+---------+-------------------+----------------+ | user_id | dominant_reaction | reaction_ratio | +---------+-------------------+----------------+ | 3       | love              | 1.00           | | 1       | like              | 0.80           | +---------+-------------------+----------------+
解释：
用户 1：
总反应数 = 5
'like' 出现了 4 次
reaction_ratio = 4 / 5 = 0.80
满足 60% 一致的要求
用户 2：
总反应数 = 5
出现最多的反应只出现了 2 次
reaction_ratio = 2 / 5 = 0.40
不满足一致的要求
用户 3：
总反应数 = 5
'love' 出现了 5 次
reaction_ratio = 5 / 5 = 1.00
满足一致的要求
结果表按 reaction_ratio 降序排序，然后按 user_id 升序排序。
"""

from typing import List, Optional


class Solution:
    def findEmotionallyConsistentUsers(self, reactions: List[List]) -> List[List]:
        """
        寻找情绪一致的用户。
        输入：reactions 是 [user_id, content_id, reaction] 的列表。
        对于每个用户：
        1. 统计不同 content_id 的数量（至少 5 个）。
        2. 统计每种 reaction 的出现次数，找到出现次数最多的 reaction。
        3. 如果该 reaction 占比 >= 60%，则用户是情绪一致的。
        返回 [user_id, dominant_reaction, reaction_ratio] 按 ratio 降序、user_id 升序排列。
        reaction_ratio 保留两位小数。
        """
        from collections import defaultdict
        from typing import List

        # 按用户分组统计
        user_reactions = defaultdict(list)  # user_id -> list of (content_id, reaction)
        user_content_set = defaultdict(set)  # user_id -> set of content_id
        user_reaction_count = defaultdict(lambda: defaultdict(int))  # user_id -> reaction -> count

        for user_id, content_id, reaction in reactions:
            user_content_set[user_id].add(content_id)
            user_reaction_count[user_id][reaction] += 1

        result = []
        for user_id in user_content_set:
            # 至少对 5 个不同 content 作出反应
            if len(user_content_set[user_id]) < 5:
                continue

            total = sum(user_reaction_count[user_id].values())
            # 找到出现次数最多的 reaction
            dominant = ""
            max_count = 0
            for r, cnt in user_reaction_count[user_id].items():
                if cnt > max_count or (cnt == max_count and r < dominant):
                    # tiebreak: 按字典序？题目没有明确说明 tie 的情况，
                    # 但 percentage 通常取最大的那个即可
                    # 如果有多个 reaction 出现次数相同，取任意一个占比 >= 60% 即可判断
                    pass
                if cnt > max_count:
                    max_count = cnt
                    dominant = r

            # 重新找 dominant（处理 tie 更准确）
            max_count = max(user_reaction_count[user_id].values())
            # 找到第一个出现次数等于 max_count 的 reaction（字典序最小）
            dominant = min(
                (r for r, cnt in user_reaction_count[user_id].items() if cnt == max_count)
            )

            ratio = max_count / total
            if ratio >= 0.6:
                result.append([user_id, dominant, round(ratio, 2)])

        # 排序：ratio 降序，user_id 升序
        result.sort(key=lambda x: (-x[2], x[0]))

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, Counting, Sorting
#
# 解题思路:
# 这是典型的 SQL 统计类问题，要求实现为 Python 函数处理列表数据。
# 1. 遍历 reactions 列表，按 user_id 分组统计：
#    - 使用 set 记录每个用户接触过的不同 content_id
#    - 使用嵌套 dict 统计每个用户每种 reaction 的出现次数
# 2. 过滤条件：用户的不同 content_id 数量 >= 5
# 3. 对于满足条件的用户，计算总反应次数和出现最多的 reaction 占比
# 4. 如果占比 >= 60%（0.6），则该用户是情绪一致的
# 5. 保留两位小数，按 reaction_ratio 降序、user_id 升序排序返回
#
# 时间复杂度: O(R)，其中 R 是 reactions 列表的长度。遍历一次完成所有统计。
# 空间复杂度: O(U + C)，U 是用户数，C 是每个用户的 reaction 种类数。
#
# 关键点:
# - 使用 set 去重统计不同 content_id 数量
# - 使用嵌套 defaultdict 方便分组计数
# - 占比计算时注意浮点数比较
# - 排序规则：先按 ratio 降序，再按 user_id 升序
