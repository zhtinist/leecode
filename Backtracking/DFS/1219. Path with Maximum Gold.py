"""
LeetCode #1219 - Path with Maximum Gold
中文题名：黄金矿工
https://leetcode.com/problems/path-with-maximum-gold/

In a gold mine `grid` of size `m * n`, each cell in this mine
has an integer representing the amount of gold in that cell, `0` if it
is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.

From your position you can walk one step to the left, right, up or down.

You can't visit the same cell more than once.

Never visit a cell with `0` gold.

You can start and stop collecting gold from any position in the
grid that has some gold.

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
[5,8,7],
[0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
[2,0,6],
[3,4,5],
[0,3,0],
[9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Constraints:

`1 <= grid.length, grid[i].length <= 15`

`0 <= grid[i][j] <= 100`

There are at most 25 cells containing gold.

【中文翻译】
在一个大小为 m * n 的金矿网格 grid 中，每个单元格中的整数表示该单元格中的黄金数量，如果该单元格是空的则为 0。

返回你在符合以下条件的情况下能收集到的最大黄金量：

每当你在一个单元格中时，你将收集该单元格中的所有黄金。
从你的位置，你可以向左、右、上或下走一步。
你不能多次访问同一个单元格。
永远不要访问黄金为 0 的单元格。
你可以从网格中任意一个有黄金的单元格开始和停止收集黄金。

示例 1：

输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
收集最多黄金的路径：9 -> 8 -> 7。

示例 2：

输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
输出：28
解释：
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
收集最多黄金的路径：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。

约束条件：

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
最多有 25 个单元格含有黄金。

"""

from typing import List, Optional


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            gold = grid[r][c]
            grid[r][c] = 0  # 标记已访问

            max_next = 0
            for dr, dc in dirs:
                max_next = max(max_next, dfs(r + dr, c + dc))

            grid[r][c] = gold  # 回溯
            return gold + max_next

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    res = max(res, dfs(i, j))
        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用深度优先搜索(DFS) + 回溯(Backtracking)穷举所有可能的采金路径。
# 由于网格最多 15x15=225 个单元格，且最多 25 个有黄金的单元格，
# 搜索空间有限（从每个有黄金的单元格出发，最多探索 4^25 个分支，但实际远小于此因为路径受限制）。
#
# 具体步骤：
# 1. 遍历网格的每个单元格，如果含有黄金（grid[i][j] != 0），则从该点开始 DFS。
# 2. DFS 过程：
#    - 收集当前单元格的黄金 gold = grid[r][c]。
#    - 将 grid[r][c] 标记为 0（已访问，避免重复）。
#    - 向四个方向递归探索，取其中能获得最大黄金的路径。
#    - 回溯：恢复 grid[r][c] = gold。
#    - 返回 gold + max_next（当前黄金 + 后续路径最大黄金）。
# 3. 所有起点中的最大值即为答案。
#
# 时间复杂度: O(k * 4^k) - k 为有黄金的单元格数（最多 25），每个单元格最多有 4 个方向
# 空间复杂度: O(k) - 递归调用栈深度最多 k 层
#
# 关键点:
# - 原地标记访问：将 grid[r][c] 设为 0 表示已访问，回溯时恢复原值，避免额外 visited 数组
# - 题目约束保证了暴力搜索的可行性：最多 25 个黄金格
# - 从每个有黄金的单元格出发都需要尝试（因为可以从任意位置开始和结束）
# - 遇到 0 的单元格立即返回 0（不能访问空单元格）
