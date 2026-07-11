"""
LeetCode #1311 - Get Watched Videos by Your Friends
中文题名：获取你好友已观看的视频
https://leetcode.com/problems/get-watched-videos-by-your-friends/

There are `n` people, each person has a unique id between `0`
and `n-1`. Given the arrays `watchedVideos` and
`friends`, where `watchedVideos[i]` and `friends[i]`
contain the list of watched videos and the list of friends respectively for the person
with `id = i`.

Level 1 of videos are all watched videos by your friends, level
2 of videos are all watched videos by the friends of your friends
and so on. In general, the level k of videos are all watched
videos by people with the shortest
path equal to k with you. Given
your `id` and the `level` of videos, return the list of
videos ordered by their frequencies (increasing). For videos with the same frequency
order them alphabetically from least to greatest.

Example 1:

Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
Output: ["B","C"]
Explanation:
You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
Person with id = 1 -> watchedVideos = ["C"]
Person with id = 2 -> watchedVideos = ["B","C"]
The frequencies of watchedVideos by your friends are:
B -> 1
C -> 2

Example 2:

Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
Output: ["D"]
Explanation:
You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).

Constraints:

`n == watchedVideos.length == friends.length`

`2 <= n <= 100`

`1 <= watchedVideos[i].length <= 100`

`1 <= watchedVideos[i][j].length <= 8`

`0 <= friends[i].length < n`

`0 <= friends[i][j] < n`

`0 <= id < n`

`1 <= level < n`

if `friends[i]` contains `j`, then
`friends[j]` contains `i`

【中文翻译】
有 n 个人，每个人有一个唯一的 id，范围在 0 到 n-1。
给定 watchedVideos 和 friends 两个数组，
其中 watchedVideos[i] 和 friends[i] 分别包含 id = i 的人观看过的视频列表和好友列表。

第 1 级视频是你所有好友观看过的视频，第 2 级视频是你好友的好友观看过的视频，以此类推。
一般来说，第 k 级视频是所有与你的最短路径等于 k 的人观看过的视频。
给定你的 id 和视频的 level，返回视频列表，按视频出现的频率升序排序；
对于频率相同的视频，按字母顺序从小到大排序。

示例 1：
输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
输出：["B","C"]
解释：
你的 id = 0（图中的绿色）。你的好友（图中的黄色）：
id = 1 的人 -> watchedVideos = ["C"]
id = 2 的人 -> watchedVideos = ["B","C"]
你好友观看视频的频率：
B -> 1
C -> 2

示例 2：
输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
输出：["D"]
解释：
你的 id = 0（图中的绿色）。你唯一的好友的好友是 id = 3 的人（图中的黄色）。

约束条件：
n == watchedVideos.length == friends.length
2 <= n <= 100
1 <= watchedVideos[i].length <= 100
1 <= watchedVideos[i][j].length <= 8
0 <= friends[i].length < n
0 <= friends[i][j] < n
0 <= id < n
1 <= level < n
如果 friends[i] 包含 j，则 friends[j] 包含 i
"""

from typing import List
from collections import deque, Counter


class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int,
    ) -> List[str]:
        n = len(friends)
        visited = [False] * n
        queue = deque([id])
        visited[id] = True
        current_level = 0

        # BFS to find all people at exactly 'level' distance
        while queue and current_level < level:
            for _ in range(len(queue)):
                person = queue.popleft()
                for friend in friends[person]:
                    if not visited[friend]:
                        visited[friend] = True
                        queue.append(friend)
            current_level += 1

        # Count video frequencies from people at the target level
        freq = Counter()
        for person in queue:
            for video in watchedVideos[person]:
                freq[video] += 1

        # Sort: first by frequency (ascending), then alphabetically
        result = sorted(freq.keys(), key=lambda v: (freq[v], v))
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 使用 BFS 从起始 id 出发，逐层向外扩展，找到距离恰好为 level 的所有人。
#    BFS 天然保证找到的是最短路径，因此第 level 层的人就是距离为 level 的人。
# 2. 收集这些 level 级好友观看的所有视频，使用 Counter 统计每个视频出现的频率。
# 3. 按频率升序排序，频率相同按字母顺序排序。
# 4. 使用排序 key=lambda v: (freq[v], v) 实现多条件排序。
#
# 时间复杂度: O(N + V log V)，N 为人数，V 为 level 级好友观看的不同视频数。
#  BFS 遍历图 O(N + E)，其中 E 为朋友关系边数；
#  统计频率 O(K * M)，K 为 level 级好友数，M 为人均视频数；
#  排序 O(V log V)，其中 V <= K * M。
# 空间复杂度: O(N + V)，visited 数组和队列 O(N)，Counter 和结果 O(V)。
#
# 关键点:
# - BFS 层级遍历正好对应题目中的 level 概念
# - 使用 visited 数组避免重复访问和无向图中的回边
# - 排序使用元组 (频率, 名称) 作为 key 实现多条件排序
# - Counter 简化频率统计
# - 注意 BFS 时 current_level < level 的条件控制










