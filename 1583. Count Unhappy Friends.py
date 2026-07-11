"""
LeetCode #1583 - Count Unhappy Friends
中文题名：统计不开心的朋友
https://leetcode.com/problems/count-unhappy-friends/


You are given a list of `preferences` for `n` friends,
where `n` is always even.

For each person `i`, `preferences[i]` contains a
list of friends sorted in the order of
preference. In other words, a friend earlier in the list is more
preferred than a friend later in the list. Friends in each list are denoted
by integers from `0` to `n-1`.

All the friends are divided into pairs. The pairings are given in a list `pairs`, where
`pairs[i] = [xi, yi]` denotes
`xi` is paired with `yi` and `yi`
is paired with `xi`.

However, this pairing may cause some of the friends to be unhappy. A friend
`x` is unhappy if `x` is paired with `y` and
there exists a friend `u` who is paired with `v` but:

`x` prefers `u` over `y`, and

`u` prefers `x` over `v`.

Return the number of unhappy friends.

Example 1:

Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
Output: 2
Explanation:
Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.

Example 2:

Input: n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
Output: 0
Explanation: Both friends 0 and 1 are happy.

Example 3:

Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
Output: 4

Constraints:

`2 <= n <= 500`

`n` is even.

`preferences.length == n`

`preferences[i].length == n - 1`

`0 <= preferences[i][j] <= n - 1`

`preferences[i]` does not contain `i`.

All values in `preferences[i]` are unique.

`pairs.length == n/2`

`pairs[i].length == 2`

`xi != yi`

`0 <= xi, yi <= n - 1`

Each person is contained in exactly one pair.

【中文翻译】
有 n 个人（偶数），每人有一个偏好列表 preferences[i] 表示对其他人（除自己外）的好感度排序。
配对关系由 pairs 给出。如果存在 u 更喜欢 v 而非自己的配对对象 x，且 v 更喜欢 u 而非自己的配对对象 y，
则 u 是 不开心 的。返回不开心的朋友数量。

示例 1：输入：n = 4, preferences = [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], pairs = [[0,1],[2,3]]
输出：2

示例 2：输入：n = 2, preferences = [[1],[0]], pairs = [[0,1]]
输出：0
"""

from typing import List, Optional


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        order = [[0] * n for _ in range(n)]
        for i in range(n):
            for rank, j in enumerate(preferences[i]):
                order[i][j] = rank
        match = [0] * n
        for x, y in pairs:
            match[x] = y
            match[y] = x
        unhappy = 0
        for x in range(n):
            y = match[x]
            for u in preferences[x]:
                if u == y:
                    break
                v = match[u]
                if order[u][x] < order[u][v]:
                    unhappy += 1
                    break
        return unhappy



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 构建 order 矩阵，order[i][j] 表示 j 在 i 偏好列表中的排名（越小越喜欢）。
# build match 数组记录每个人的配对对象。
# 对于每个人 x，遍历其偏好列表中排在配对对象 y 之前的每个人 u：
# 如果 u 对 x 的排名高于 u 对自己配对对象 v 的排名，则 x 不开心。
#
# 时间复杂度: O(N^2) — 最坏情况下每个人遍历其偏好列表
# 空间复杂度: O(N^2) — order 矩阵
#
# 关键点:
# - 预处理排名矩阵便于 O(1) 查询偏好
# - 只需找到任意一个双向更喜欢的人，x 就不开心
# - 只检查排在当前配对对象之前的人












