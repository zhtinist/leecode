"""
LeetCode #994 - Rotting Oranges
中文题名：腐烂的橘子
https://leetcode.com/problems/rotting-oranges/

In a given grid, each cell can have one of three values:

the value `0` representing an empty cell;

the value `1` representing a fresh orange;

the value `2` representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes
rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return `-1` instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

`1 <= grid.length <= 10`

`1 <= grid[0].length <= 10`

`grid[i][j]` is only `0`, `1`, or
`2`.

【中文翻译】
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。

每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

示例 1：

输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4

示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行，第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正方向上。

示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案是 0。

注意：

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] 只为 0、1 或 2。
"""

from typing import List, Optional
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while queue:
            r, c, time = queue.popleft()
            minutes = time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, time + 1))

        return minutes if fresh == 0 else -1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 多源 BFS（广度优先搜索）：
# 1. 遍历网格，收集所有腐烂橘子（值为 2）的位置入队，同时统计新鲜橘子数量。
# 2. 若没有新鲜橘子，直接返回 0。
# 3. BFS 逐层扩散：
#    - 每次从队列弹出腐烂橘子，尝试感染四个方向的相邻新鲜橘子。
#    - 被感染的新鲜橘子变为腐烂，新鲜计数减 1，入队并记录时间 +1。
# 4. BFS 结束后，若 fresh > 0 则说明有橘子永远不会腐烂，返回 -1；
#    否则返回最大分钟数。
# 腐烂过程相当于从所有腐烂橘子同时开始 BFS，记录最大层数。
#
# 时间复杂度: O(m * n)，每个单元格最多入队一次
# 空间复杂度: O(m * n)，队列最坏情况存储所有单元格
#
# 关键点:
# - 多源 BFS：所有腐烂橘子同时作为初始源点
# - BFS 本质是求最短时间（层序遍历）
# - 初始统计新鲜橘子数以便判断是否全部腐烂
# - 方向数组 [(1,0), (-1,0), (0,1), (0,-1)] 处理四方向
