"""
LeetCode #1536 - Minimum Swaps to Arrange a Binary Grid
中文题名：排布二进制网格的最少交换次数
https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

Given an `n x n` binary `grid`, in one step you can
choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal
are zeros.

Return the minimum number of steps needed to make the grid valid, or
-1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell `(1, 1)`
and ends at cell `(n, n)`.

Example 1:

Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3

Example 2:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0

Constraints:

`n == grid.length`

`n == grid[i].length`

`1 <= n <= 200`

`grid[i][j]` is `0` or `1`

【中文翻译】
给定一个 n x n 的二进制网格 grid，每一步可以选择网格中相邻的两行并交换它们。
如果网格主对角线以上的所有单元格都是 0，则称网格是有效的。
返回使网格有效所需的最少步数，如果无法做到则返回 -1。

示例 1：

输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
输出：3

示例 2：

输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
输出：-1
解释：所有行相同，交换无效果。

示例 3：

输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
输出：0
"""

from typing import List, Optional


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # trailing_zeros[i] = number of trailing zeros in row i
        trailing_zeros = []
        for row in grid:
            zeros = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    zeros += 1
                else:
                    break
            trailing_zeros.append(zeros)

        swaps = 0
        for i in range(n):
            # Need row with at least (n - 1 - i) trailing zeros
            required = n - 1 - i
            found = -1
            for j in range(i, n):
                if trailing_zeros[j] >= required:
                    found = j
                    break
            if found == -1:
                return -1
            # Bubble the found row up to position i
            for j in range(found, i, -1):
                trailing_zeros[j], trailing_zeros[j - 1] = trailing_zeros[j - 1], trailing_zeros[j]
                swaps += 1
        return swaps



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 主对角线以上的单元格全为 0，等价于第 i 行末尾至少有 n-1-i 个连续的 0。
# 首先计算每行末尾连续 0 的个数。然后贪心地从第 0 行开始：
# 对于第 i 行，需要至少 n-1-i 个末尾零。从当前行及以下找到第一个满足条件的行，
# 将该行冒泡交换到位置 i，累加交换次数。如果找不到满足条件的行，返回 -1。
#
# 时间复杂度: O(N^2) — 对于每行需要扫描后面的行
# 空间复杂度: O(N) — 存储末尾零个数
#
# 关键点:
# - 转化为每行末尾零个数的问题
# - 贪心匹配：第 i 行需要 n-1-i 个末尾零
# - 冒泡交换：每次只能交换相邻行
