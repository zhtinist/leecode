"""
LeetCode #1942 - The Number of the Smallest Unoccupied Chair
最小未被占据椅子的编号
https://leetcode.cn/problems/the-number-of-the-smallest-unoccupied-chair/

有 `n` 个朋友在举办一个派对，这些朋友从 `0` 到 `n - 1` 编号。派对里有 无数 张椅子，编号为 `0` 到 `infinity` 。当一个朋友到达派对时，他会占据 编号最小 且未被占据的椅子。
比方说，当一个朋友到达时，如果椅子 `0` ，`1` 和 `5` 被占据了，那么他会占据 `2` 号椅子。
当一个朋友离开派对时，他的椅子会立刻变成未占据状态。如果同一时刻有另一个朋友到达，可以立即占据这张椅子。
给你一个下标从 0 开始的二维整数数组 `times` ，其中 `times[i] = [arrival_i, leaving_i]` 表示第 `i` 个朋友到达和离开的时刻，同时给你一个整数 `targetFriend` 。所有到达时间 互不相同 。
请你返回编号为 `targetFriend` 的朋友占据的 椅子编号 。

示例 1：
输入：times = [[1,4],[2,3],[4,6]], targetFriend = 1 输出：1 解释： - 朋友 0 时刻 1 到达，占据椅子 0 。 - 朋友 1 时刻 2 到达，占据椅子 1 。 - 朋友 1 时刻 3 离开，椅子 1 变成未占据。 - 朋友 0 时刻 4 离开，椅子 0 变成未占据。 - 朋友 2 时刻 4 到达，占据椅子 0 。 朋友 1 占据椅子 1 ，所以返回 1 。
示例 2：
输入：times = [[3,10],[1,5],[2,6]], targetFriend = 0 输出：2 解释： - 朋友 1 时刻 1 到达，占据椅子 0 。 - 朋友 2 时刻 2 到达，占据椅子 1 。 - 朋友 0 时刻 3 到达，占据椅子 2 。 - 朋友 1 时刻 5 离开，椅子 0 变成未占据。 - 朋友 2 时刻 6 离开，椅子 1 变成未占据。 - 朋友 0 时刻 10 离开，椅子 2 变成未占据。 朋友 0 占据椅子 2 ，所以返回 2 。

提示：
`n == times.length`
`2 <= n <= 10^4`
`times[i].length == 2`
`1 <= arrival_i < leaving_i <= 10^5`
`0 <= targetFriend <= n - 1`
每个 `arrival_i` 时刻 互不相同 。
"""

from typing import List, Optional


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        """
        Simulate arrivals and departures using two min-heaps.
        """
        import heapq

        n = len(times)
        # Attach original index to each friend
        arrivals = [(times[i][0], times[i][1], i) for i in range(n)]
        arrivals.sort(key=lambda x: x[0])  # sort by arrival time

        available_chairs = list(range(n))  # min-heap of available chair numbers
        heapq.heapify(available_chairs)

        # min-heap of (leaving_time, chair_number)
        occupied = []

        for arr, lea, idx in arrivals:
            # Free chairs of friends who left before current arrival
            while occupied and occupied[0][0] <= arr:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(available_chairs, chair)

            # Assign smallest available chair
            chair = heapq.heappop(available_chairs)

            if idx == targetFriend:
                return chair

            heapq.heappush(occupied, (lea, chair))

        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Heap (Priority Queue)
#
# 解题思路:
# 模拟派对过程。按到达时间排序所有朋友。
# 用一个小顶堆 available 维护当前可用的最小椅子编号。
# 用另一个小顶堆 occupied 维护 (离开时间, 椅子编号)，按离开时间排序。
# 对于每个到达的朋友：
# 1. 释放所有在到达前已经离开的椅子（从 occupied 弹出放回 available）
# 2. 从 available 弹出最小椅子分配给他
# 3. 如果是 targetFriend，返回该椅子编号
# 4. 否则将该朋友的 (离开时间, 椅子) 放入 occupied
#
# 时间复杂度: O(N log N)，排序 + 堆操作
# 空间复杂度: O(N)，存储堆和排序数组
#
# 关键点:
# - 两个堆的配合：一个管理可用椅子，一个管理占用状态
# - 按到达时间处理事件，确保时间线正确
# - 同一时刻离开和到达可以立即占据椅子（用 <= 判断）
