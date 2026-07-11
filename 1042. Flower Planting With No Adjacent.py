"""
LeetCode #1042 - Flower Planting With No Adjacent
中文题名：不邻接植花
https://leetcode.com/problems/flower-planting-with-no-adjacent/

You have `N` gardens, labelled `1` to `N`.  In each
garden, you want to plant one of 4 types of flowers.

`paths[i] = [x, y]` describes the existence of a bidirectional path from garden
`x` to garden `y`.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens
connected by a path, they have different types of flowers.

Return any such a choice as an array `answer`, where `answer[i]`
is the type of flower planted in the `(i+1)`-th garden.  The flower
types are denoted 1, 2,
3, or 4.  It is guaranteed
an answer exists.

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]

Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]

Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]

Note:

`1 <= N <= 10000`

`0 <= paths.size <= 20000`

No garden has 4 or more paths coming into or leaving it.

It is guaranteed an answer exists.

【中文翻译】
你有 N 个花园，标记为 1 到 N。在每个花园中，你想种植 4 种花中的一种。

paths[i] = [x, y] 描述了花园 x 到花园 y 之间的一条双向路径。

此外，没有花园拥有超过 3 条进出路径。

你的任务是为每个花园选择一种花，使得对于通过路径连接的任何两个花园，它们有不同类型的花。

以数组 answer 的形式返回任意一种选择，其中 answer[i] 是种在第 (i+1) 个花园中的花的类型。花的类型用 1、2、3、4 表示。保证答案存在。

示例 1：

输入：N = 3, paths = [[1,2],[2,3],[3,1]]
输出：[1,2,3]

示例 2：

输入：N = 4, paths = [[1,2],[3,4]]
输出：[1,2,1,2]

示例 3：

输入：N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
输出：[1,2,3,4]

注意：

1 <= N <= 10000
0 <= paths.size <= 20000
没有花园拥有 4 条或更多进出路径。
保证答案存在。
"""

from typing import List, Optional


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = [[] for _ in range(N)]
        for u, v in paths:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        # result[i] = flower type (1-4) for garden i
        res = [0] * N

        for i in range(N):
            # Find colors used by neighbors
            used = set()
            for neighbor in graph[i]:
                if res[neighbor] != 0:
                    used.add(res[neighbor])
            # Pick the first unused color (1-4)
            for color in range(1, 5):
                if color not in used:
                    res[i] = color
                    break

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用贪心图着色算法。由于每个花园最多只有3条路径（即度数最多为3），
# 而我们有4种颜色，因此贪心策略一定能找到可行的着色方案。
# 建立邻接表后，按花园编号顺序处理每个花园：
# 1. 检查所有邻居花园已使用的颜色
# 2. 从1-4中选择第一个未被邻居使用的颜色
# 3. 由于度数最多为3，至少有一个颜色可用
# 这相当于图着色问题的一个特例（每个顶点度数<=3，4种颜色）。
#
# 时间复杂度: O(N + P) - P为路径数量
# 空间复杂度: O(N + P) - 邻接表存储
#
# 关键点:
# - 每个花园最多3个邻居，4种颜色足够贪心着色
# - 不需要回溯或复杂算法，直接按顺序贪心即可
# - 输入花园编号从1开始，需要转换为0索引
