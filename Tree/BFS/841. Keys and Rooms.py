"""
LeetCode #841 - Keys and Rooms
中文题名：钥匙和房间
https://leetcode.com/problems/keys-and-rooms/

There are `N` rooms and you start in room `0`.  Each room has a
distinct number in `0, 1, 2, ..., N-1`, and each room may have some keys to
access the next room.

Formally, each room `i` has a list of keys `rooms[i]`, and each
key `rooms[i][j]` is an integer in `[0, 1, ..., N-1]` where `N =
rooms.length`.  A key `rooms[i][j] = v` opens the room with
number `v`.

Initially, all the rooms start locked (except for room `0`).

You can walk back and forth between rooms freely.

Return `true` if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.

Note:

`1 <= rooms.length <= 1000`

`0 <= rooms[i].length <= 1000`

The number of keys in all rooms combined is at most `3000`.

【中文翻译】
有 `N` 个房间，你从房间 `0` 开始。每个房间都有一个不同的编号：`0, 1, 2, ..., N-1`，并且每个房间可能有一些钥匙可以进入下一个房间。

形式上，每个房间 `i` 都有一个钥匙列表 `rooms[i]`，每个钥匙 `rooms[i][j]` 是一个在 `[0, 1, ..., N-1]` 范围内的整数，其中 `N = rooms.length`。钥匙 `rooms[i][j] = v` 可以打开编号为 `v` 的房间。

最初，除 `0` 号房间外，所有房间都是锁着的。

你可以自由地在房间之间来回走动。

当且仅当你可以进入每个房间时，返回 `true`。

示例 1：

输入：[[1],[2],[3],[]]
输出：true
解释：
我们从房间 0 开始，拿到钥匙 1。
然后去房间 1，拿到钥匙 2。
然后去房间 2，拿到钥匙 3。
然后去房间 3。由于我们能够进入每个房间，返回 true。

示例 2：

输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们无法进入编号为 2 的房间。

注意：

`1 <= rooms.length <= 1000`

`0 <= rooms[i].length <= 1000`

所有房间的钥匙总数不超过 `3000`。

"""

from typing import List, Optional


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)

        return all(visited)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这是一个典型的图的遍历问题。
# 将每个房间视为图中的节点，钥匙视为有向边。
# 从房间 0 开始，使用 DFS（栈）或 BFS（队列）遍历所有可达房间。
# 用一个 visited 数组记录已访问的房间。
# 遇到新房间时，将该房间的所有钥匙加入待探索列表。
# 最后检查是否所有房间都被访问过。
#
# 时间复杂度: O(N + K) — N 是房间数，K 是钥匙总数
# 空间复杂度: O(N) — visited 数组和栈/队列的大小
#
# 关键点:
# - 房间和钥匙天然构成有向图
# - 从房间 0 开始 DFS/BFS 即可找到所有可达房间
# - 不需要显式构建图，输入 rooms 本身就是邻接表
# - 使用栈实现 DFS（或 collections.deque 实现 BFS）
