"""
LeetCode #2850 - Minimum Moves to Spread Stones Over Grid
将石头分散到网格图的最少移动次数
https://leetcode.cn/problems/minimum-moves-to-spread-stones-over-grid/

给你一个大小为 `3 * 3` ，下标从 0 开始的二维整数矩阵 `grid` ，分别表示每一个格子里石头的数目。网格图中总共恰好有 `9` 个石头，一个格子里可能会有 多个 石头。
每一次操作中，你可以将一个石头从它当前所在格子移动到一个至少有一条公共边的相邻格子。
请你返回每个格子恰好有一个石头的 最少移动次数 。

示例 1：

输入：grid = [[1,1,0],[1,1,1],[1,2,1]] 输出：3 解释：让每个格子都有一个石头的一个操作序列为： 1 - 将一个石头从格子 (2,1) 移动到 (2,2) 。 2 - 将一个石头从格子 (2,2) 移动到 (1,2) 。 3 - 将一个石头从格子 (1,2) 移动到 (0,2) 。 总共需要 3 次操作让每个格子都有一个石头。 让每个格子都有一个石头的最少操作次数为 3 。
示例 2：

输入：grid = [[1,3,0],[1,0,0],[1,0,3]] 输出：4 解释：让每个格子都有一个石头的一个操作序列为： 1 - 将一个石头从格子 (0,1) 移动到 (0,2) 。 2 - 将一个石头从格子 (0,1) 移动到 (1,1) 。 3 - 将一个石头从格子 (2,2) 移动到 (1,2) 。 4 - 将一个石头从格子 (2,2) 移动到 (2,1) 。 总共需要 4 次操作让每个格子都有一个石头。 让每个格子都有一个石头的最少操作次数为 4 。

提示：
`grid.length == grid[i].length == 3`
`0 <= grid[i][j] <= 9`
`grid` 中元素之和为 `9` 。
"""

from typing import List, Optional


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        sources = []  # cells with extra stones: (r, c, count-1)
        targets = []  # cells with 0 stones: (r, c)
        for r in range(3):
            for c in range(3):
                if grid[r][c] > 1:
                    for _ in range(grid[r][c] - 1):
                        sources.append((r, c))
                elif grid[r][c] == 0:
                    targets.append((r, c))

        m = len(sources)
        ans = float('inf')

        # Try all permutations of assigning sources to targets
        def backtrack(idx, used_mask, cur_cost):
            nonlocal ans
            if cur_cost >= ans:
                return
            if idx == m:
                ans = min(ans, cur_cost)
                return
            sr, sc = sources[idx]
            for ti, (tr, tc) in enumerate(targets):
                if not (used_mask >> ti & 1):
                    dist = abs(sr - tr) + abs(sc - tc)
                    backtrack(idx + 1, used_mask | (1 << ti), cur_cost + dist)

        backtrack(0, 0, 0)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Dynamic Programming, Backtracking, Bitmask, Matrix
#
# 解题思路:
# 将问题转化为二分图匹配：收集有多余石头的格子（source，每个多余石头为一个源点）和没有石头的格子（target）。
# 由于网格固定为3x3且总石头数为9，源点和目标点数量相等且很少（最多4个）。
# 使用回溯枚举所有分配方案（源点到目标点的全排列），计算曼哈顿距离之和的最小值。
#
# 时间复杂度: O(m!) 其中 m 为空缺格子数（最多4个）
# 空间复杂度: O(1)
#
# 关键点:
# - 将多余石头视为源点，空格子视为目标点，转化为最小代价匹配
# - 网格小（3x3），回溯枚举所有排列即可
# - 代价 = 曼哈顿距离 |sr-tr| + |sc-tc|
