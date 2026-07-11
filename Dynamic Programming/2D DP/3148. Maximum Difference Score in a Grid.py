"""
LeetCode #3148 - Maximum Difference Score in a Grid
矩阵中的最大得分
https://leetcode.cn/problems/maximum-difference-score-in-a-grid/

给你一个由 正整数 组成、大小为 `m x n` 的矩阵 `grid`。你可以从矩阵中的任一单元格移动到另一个位于正下方或正右侧的任意单元格（不必相邻）。从值为 `c1` 的单元格移动到值为 `c2` 的单元格的得分为 `c2 - c1` 。
你可以从 任一 单元格开始，并且必须至少移动一次。
返回你能得到的 最大 总得分。

示例 1：

输入：grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]
输出：9
解释：从单元格 `(0, 1)` 开始，并执行以下移动：
- 从单元格 `(0, 1)` 移动到 `(2, 1)`，得分为 `7 - 5 = 2` 。
- 从单元格 `(2, 1)` 移动到 `(2, 2)`，得分为 `14 - 7 = 7` 。
总得分为 `2 + 7 = 9` 。
示例 2：

输入：grid = [[4,3,2],[3,2,1]]
输出：-1
解释：从单元格 `(0, 0)` 开始，执行一次移动：从 `(0, 0)` 到 `(0, 1)` 。得分为 `3 - 4 = -1` 。

提示：
`m == grid.length`
`n == grid[i].length`
`2 <= m, n <= 1000`
`4 <= m * n <= 10^5`
`1 <= grid[i][j] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = float('-inf')
        # min_val[i][j] = grid[0..i][0..j]中的最小值
        min_val = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # 获取左上方向的最小值（必须移动至少一次）
                prev_min = float('inf')
                if i > 0:
                    prev_min = min(prev_min, min_val[i - 1][j])
                if j > 0:
                    prev_min = min(prev_min, min_val[i][j - 1])
                if prev_min != float('inf'):
                    ans = max(ans, grid[i][j] - prev_min)

                # 更新min_val
                cur_min = grid[i][j]
                if i > 0:
                    cur_min = min(cur_min, min_val[i - 1][j])
                if j > 0:
                    cur_min = min(cur_min, min_val[i][j - 1])
                min_val[i][j] = cur_min

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Matrix
#
# 解题思路:
# 关键洞察：多次移动的总得分 = 终点值 - 起点值（中间值相消）。
# 因此问题转化为找最大差值grid[i][j] - grid[i'][j']，其中(i',j')在(i,j)的左上方向（可同行或同列）。
# 用二维前缀最小值DP：min_val[i][j]记录(0,0)到(i,j)子矩阵的最小值。
# 对于每个格子，用左/上的最小值计算差值，更新答案。
#
# 时间复杂度: O(m*n)
# 空间复杂度: O(m*n)
#
# 关键点:
# - 总得分简化为终点值减起点值
# - 只需要左上方向的最小值（右/下移动）
# - 至少移动一次（不能选自己作为起点）
