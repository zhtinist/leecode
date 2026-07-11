"""
LeetCode #787 - Cheapest Flights Within K Stops
中文题名：K 站中转内最便宜的航班
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are `n` cities connected by `m` flights. Each fight starts
from city `u `and arrives at `v` with a price `w`.

Now given all the cities and flights, together with starting city `src` and the
destination `dst`, your task is to find the cheapest price from
`src` to `dst` with up to `k` stops. If there is no such
route, output `-1`.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:

The cheapest price from city `0` to city `2` with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:

The cheapest price from city `0` to city `2` with at most 0 stop costs 500, as marked blue in the picture.

Note:

The number of nodes `n` will be in range `[1, 100]`,
with nodes labeled from `0` to `n`` - 1`.

The size of `flights` will be in range `[0, n * (n - 1) /
2]`.

The format of each flight will be `(src, ``dst``,
price)`.

The price of each flight will be in the range `[1, 10000]`.

`k` is in the range of `[0, n - 1]`.

There will not be any duplicated flights or self cycles.

【中文翻译】
有 n 个城市通过 m 个航班连接。每个航班都从城市 u 出发，到达城市 v，票价为 w。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，
你的任务是找到从 src 到 dst 最多经过 k 站中转的最便宜价格。
如果没有这样的路线，则输出 -1。

示例 1：
输入：
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出：200
解释：
城市航班图如下：

从城市 0 到城市 2 经过最多 1 站中转的最便宜价格为 200。

示例 2：
输入：
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出：500
解释：
城市航班图如下：

从城市 0 到城市 2 经过最多 0 站中转的最便宜价格为 500。

注意：

节点数 n 的范围是 [1, 100]，节点标签从 0 到 n - 1。

航班数目的范围是 [0, n * (n - 1) / 2]。

每个航班的格式是 (src, dst, price)。

每个航班的价格范围是 [1, 10000]。

k 的范围是 [0, n - 1]。

没有重复的航班或自环。
"""

from typing import List, Optional
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        # (cost, node, stops)
        heap = [(0, src, 0)]
        # min_stops[i] = 到达节点 i 时允许的最少中转次数，
        # 用于剪枝：若以更多次数到达同一节点且花费更高，则跳过
        min_stops = [float('inf')] * n

        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k or stops >= min_stops[node]:
                continue
            min_stops[node] = stops
            for neighbor, price in graph[node]:
                heapq.heappush(heap, (cost + price, neighbor, stops + 1))

        return -1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# Dijkstra 算法的变种（带中转次数限制的最短路径）。
# 1. 构建图的邻接表 graph[u] = [(v, price)]。
# 2. 使用优先队列（最小堆），存储 (当前总花费, 当前节点, 已中转次数)。
# 3. 从 src 开始 BFS+Dijkstra，每次弹出花费最小的状态。
# 4. 剪枝条件：
#    - 若 stops > k（超过允许的中转次数），跳过。
#    - 若以 >= 之前的中转次数到达当前节点，跳过（因为花费肯定更高）。
# 5. 到达 dst 时直接返回（堆保证第一次到达是最小花费）。
# 6. 队列为空仍未到达则返回 -1。
# 也可以使用 Bellman-Ford：进行 k+1 轮松弛。
#
# 时间复杂度: O(E * log V)，E 为边数，V 为节点数，每边最多入堆一次
# 空间复杂度: O(V + E)，存储图和堆
#
# 关键点:
# - Dijkstra 带限制条件（最多 k 站中转 = 最多 k+1 条边）
# - 用 min_stops 数组剪枝，避免重复处理
# - 堆保证首次到达目标即最优解
# - 也可以用 Bellman-Ford（DP）O(k * E) 解决
