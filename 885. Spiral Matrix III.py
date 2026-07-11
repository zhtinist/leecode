"""
LeetCode #885 - Spiral Matrix III
中文题名：螺旋矩阵 III
https://leetcode.com/problems/spiral-matrix-iii/

On a 2 dimensional grid with `R` rows and `C` columns, we start at
`(r0, c0)` facing east.

Here, the north-west corner of the grid is at the first row and column, and the
south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid.

Whenever we would move outside the boundary of the grid, we continue our walk outside the
grid (but may return to the grid boundary later.)

Eventually, we reach all `R * C` spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were
visited.

Example 1:

Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:

Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

Note:

`1 <= R <= 100`

`1 <= C <= 100`

`0 <= r0 < R`

`0 <= c0 < C`

【中文翻译】

在一个有 `R` 行 `C` 列的二维网格上，我们从 `(r0, c0)` 开始，面朝东方。

网格的西北角在第一行第一列，东南角在最后一行最后一列。

我们以顺时针螺旋形状移动，访问网格中的每个位置。

当移动超出网格边界时，我们继续在网格外行走（但稍后可能会回到网格边界内）。

最终，我们将访问到网格中所有的 `R * C` 个位置。

返回一个坐标列表，表示按访问顺序排列的网格位置。

"""

from typing import List, Optional


class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = []
        r, c = r0, c0
        step = 1  # 当前步长
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 东、南、西、北
        d = 0  # 当前方向索引

        while len(result) < R * C:
            for _ in range(2):  # 每两个方向后步长+1
                for _ in range(step):
                    if 0 <= r < R and 0 <= c < C:
                        result.append([r, c])
                    r += directions[d][0]
                    c += directions[d][1]
                d = (d + 1) % 4  # 转向
            step += 1

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 模拟螺旋行走过程。关键观察：步长模式为 1,1,2,2,3,3,4,4,...
# 每两个方向后步长增加1。方向顺序为 东->南->西->北（顺时针）。
# 从起点出发，每走一步检查当前坐标是否在网格内，如果在则加入结果。
# 当结果数量达到 R*C 时停止。
#
# 时间复杂度: O(max(R, C)^2) — 最坏情况需要走完覆盖所有格子的螺旋
# 空间复杂度: O(R * C) — 结果数组大小
#
# 关键点:
# - 步长每两个方向递增的规律
# - 可以在网格外行走，只需判断坐标是否在边界内
# - 方向切换使用取模循环
