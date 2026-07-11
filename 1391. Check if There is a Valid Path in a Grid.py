"""
LeetCode #1391 - Check if There is a Valid Path in a Grid
中文题名：检查网格中是否存在有效路径
https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

Given a m x n `grid`. Each cell of the `grid`
represents a street. The street of `grid[i][j]` can be:

1 which means a street connecting the left cell and the right
cell.

2 which means a street connecting the upper cell and the lower
cell.

3 which means a street connecting the left cell and the lower cell.

4 which means a street connecting the right cell and the lower cell.

5 which means a street connecting the left cell and the upper cell.

6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell `(0,0)`.
A valid path in the grid is a path which starts from the upper left cell `(0,0)`
and ends at the bottom-right cell `(m - 1, n - 1)`. The path
should only follow the streets.

Notice that you are not allowed to change any
street.

Return true if there is a valid path in the grid or false
otherwise.

Example 1:

Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

Example 2:

Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)

Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).

Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true

Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true

Constraints:

`m == grid.length`

`n == grid[i].length`

`1 <= m, n <= 300`

`1 <= grid[i][j] <= 6`

【中文翻译】

给定一个 m x n 的网格 grid。每个单元格 grid[i][j] 代表一条街道。grid[i][j] 的取值：

1：连接左格和右格
2：连接上格和下格
3：连接左格和下格
4：连接右格和下格
5：连接左格和上格
6：连接右格和上格

你将从左上角 (0,0) 出发。有效路径是指从 (0,0) 出发，只能沿着街道走，到达右下角 (m-1, n-1)。

注意：不允许改变任何街道。

如果存在有效路径返回 true，否则返回 false。

示例 1：
输入：grid = [[2,4,3],[6,5,2]]
输出：true
解释：如图所示，可以从 (0,0) 出发访问所有单元格到达 (m-1, n-1)。

示例 2：
输入：grid = [[1,2,1],[1,2,1]]
输出：false
解释：单元格 (0,0) 的街道未与任何其他单元格的街道连接，你将卡在 (0,0) 处。

示例 3：
输入：grid = [[1,1,2]]
输出：false
解释：你将在 (0,1) 处卡住，无法到达 (0,2)。

示例 4：
输入：grid = [[1,1,1,1,1,1,3]]
输出：true

示例 5：
输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
输出：true

约束条件：
m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""

from typing import List, Optional


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # 每种街道类型对应的可行方向
        # 方向: 0=上, 1=右, 2=下, 3=左
        dirs = {
            1: {1, 3},  # 左-右
            2: {0, 2},  # 上-下
            3: {3, 2},  # 左-下
            4: {1, 2},  # 右-下
            5: {3, 0},  # 左-上
            6: {1, 0},  # 右-上
        }

        # 方向偏移量
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 上、右、下、左
        # 相反方向映射
        opposite = {0: 2, 1: 3, 2: 0, 3: 1}

        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        stack = [(0, 0)]
        while stack:
            r, c = stack.pop()
            if r == m - 1 and c == n - 1:
                return True

            for d in dirs[grid[r][c]]:
                dr, dc = moves[d]
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # 相邻格必须能接受来自反方向的连接
                    if opposite[d] in dirs[grid[nr][nc]]:
                        visited[nr][nc] = True
                        stack.append((nr, nc))

        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS（或 BFS）遍历网格。
# 每种街道类型（1-6）定义了它能连接的方向。
# 从 (0,0) 出发，对于当前格子的每个可行方向，检查相邻格子是否也有对应
# 方向的连接（即相反方向是否属于相邻格子的可行方向集合）。
# 如果两个相邻格子的方向能匹配，说明可以走过去。
# 最终检查是否能到达 (m-1, n-1)。
#
# 时间复杂度: O(M * N)  每个单元格最多访问一次
# 空间复杂度: O(M * N)  访问标记数组
#
# 关键点:
# - 每类街道有特定的连接方向，需预先定义方向映射表
# - 两个相邻格子的连接必须匹配（方向互补）
# - 使用 DFS 栈或 BFS 队列均可
# - 移动方向与街道类型的对应关系需要仔细定义










