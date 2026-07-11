"""
LeetCode #743 - Network Delay Time
中文题名：网络延迟时间
https://leetcode.com/problems/network-delay-time/

There are `N` network nodes, labelled `1` to `N`.

Given `times`, a list of travel times as directed edges `times[i] =
(u, v, w)`, where `u` is the source node, `v` is the target
node, and `w` is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node `K`. How long will it take for all nodes
to receive the signal? If it is impossible, return `-1`.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:

`N` will be in the range `[1, 100]`.

`K` will be in the range `[1, N]`.

The length of `times` will be in the range `[1, 6000]`.

All edges `times[i] = (u, v, w)` will have `1 <= u, v <= N`
and `0 <= w <= 100`.

【中文翻译】
有 N 个网络节点，标记为 1 到 N。

给定一个列表 times，表示信号经过有向边的传递时间。times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点，w 是一个信号从源节点传递到目标节点的时间。

现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。

示例 1：

输入：times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
输出：2

注意：

N 的范围在 [1, 100] 之间。

K 的范围在 [1, N] 之间。

times 的长度在 [1, 6000] 之间。

所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 0 <= w <= 100。
"""

from typing import List, Optional


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        dist = {}
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            if node in graph:
                for neighbor, w in graph[node]:
                    if neighbor not in dist:
                        heapq.heappush(heap, (time + w, neighbor))

        if len(dist) != n:
            return -1
        return max(dist.values())










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 标准的 Dijkstra 最短路径算法：
# 1. 构建图的邻接表（使用字典 graph[u] = [(v, w)]）。
# 2. 使用最小堆（优先队列），每次弹出距离最小的节点。
# 3. 若节点已访问过（已在 dist 字典中），跳过。
# 4. 否则记录距离，并松弛其所有邻居。
# 5. 最后检查是否访问了所有 n 个节点：
#    - 若 dist 字典大小 != n，说明有节点不可达，返回 -1。
#    - 否则返回 dist 中的最大值。
#
# 时间复杂度: O(E * log V)，E 为边数，V 为节点数
# 空间复杂度: O(V + E)，存储图和优先队列
#
# 关键点:
# - 标准 Dijkstra 单源最短路径算法
# - 使用堆按距离贪婪扩展，保证首次出队即最短距离
# - 节点编号从 1 到 n，注意与数组 0-indexed 对齐
# - 若 len(dist) < n 说明存在不可达节点
