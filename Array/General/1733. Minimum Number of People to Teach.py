"""
LeetCode #1733 - Minimum Number of People to Teach
中文题名：需要教语言的最少人数
https://leetcode.com/problems/minimum-number-of-people-to-teach/

On a social network consisting of `m` users and some friendships between
users, two users can communicate with each other if they know a common language.

You are given an integer `n`, an array `languages`, and an
array `friendships` where:

There are `n` languages numbered `1` through
`n`,

`languages[i]` is the set of languages the `i​​​​​​th`​​​​
user knows, and

`friendships[i] = [u​​​​​​i​​​, v​​​​​​i]`
denotes a friendship between the users `u​​​​​​​​​​​i`​​​​​
and `vi`.

You can choose one language and teach it to some users so that all
friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if `x` is a friend of
`y` and `y` is a friend of `z`, this doesn't guarantee
that `x` is a friend of `z`.

Example 1:

Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.

Example 2:

Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.

Constraints:

`2 <= n <= 500`

`languages.length == m`

`1 <= m <= 500`

`1 <= languages[i].length <= n`

`1 <= languages[i][j] <= n`

`1 <= u​​​​​​i < v​​​​​​i <=
languages.length`

`1 <= friendships.length <= 500`

All tuples `(u​​​​​i, v​​​​​​i)` are unique

`languages[i]` contains only unique values

【中文翻译】
有 n 种语言（编号1到n）和 m 个用户（编号0到m-1）。languages[i] 是用户 i 掌握的语言列表。
friendships[j] = [u, v] 表示用户 u 和 v 是朋友。如果两个朋友之间没有任何共同语言，则他们之间无法交流。
可以选择教某些用户一种语言，使得所有朋友之间都可以交流。求最少需要教多少用户。

示例 1：
输入: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
输出: 1
解释: 教用户1语言2或教用户2语言1即可。
"""

from typing import List, Optional


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        m = len(languages)
        lang_sets = [set(langs) for langs in languages]

        # 找出所有不能交流的朋友对
        need_teach = set()
        for u, v in friendships:
            u, v = u - 1, v - 1
            if not (lang_sets[u] & lang_sets[v]):
                need_teach.add(u)
                need_teach.add(v)

        if not need_teach:
            return 0

        # 对于每种语言，计算需要教的用户数
        min_teach = len(need_teach)
        for lang in range(1, n + 1):
            count = sum(1 for user in need_teach if lang not in lang_sets[user])
            min_teach = min(min_teach, count)

        return min_teach
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 找出所有不能交流的朋友对（没有共同语言的），将这些用户加入 need_teach 集合
# 2. 只需考虑教这些用户一种语言，使得他们能和各自的朋友交流
# 3. 对每种语言，统计 need_teach 中不会该语言的用户数
# 4. 选择需要教授用户最少的语言
#
# 时间复杂度: O(F + L * U) — F 为朋友对数，L 为语言数，U 为需要教的用户数
# 空间复杂度: O(M + U) — 语言集合 + need_teach 集合
#
# 关键点:
# - 只有不能交流的朋友对才需要考虑教语言
# - 已经能交流的朋友不需要额外操作
# - 只需教一种语言就能解决所有不能交流的问题（所有需要教的用户学同一种语言）
