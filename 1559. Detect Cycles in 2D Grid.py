"""
LeetCode #1559 - Detect Cycles in 2D Grid
中文题名：二维网格图中探测环
https://leetcode.com/problems/detect-cycles-in-2d-grid/


Given a 2D array of characters `grid` of size `m x
n`, you need to find if there exists any cycle consisting of the same
value in `grid`.

A cycle is a path of length 4 or more in the grid that
starts and ends at the same cell. From a given cell, you can move to one of the
cells adjacent to it - in one of the four directions (up, down, left, or right), if
it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example,
the cycle `(1, 1) -> (1, 2) -> (1, 1)` is invalid because
from `(1, 2)` we visited `(1, 1)` which
was the last visited cell.

Return `true` if any cycle of the same value exists
in `grid`, otherwise, return `false`.

Example 1:

Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:

Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:

Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false

Constraints:

`m == grid.length`

`n == grid[i].length`

`1 <= m <= 500`

`1 <= n <= 500`

`grid` consists only of lowercase English letters.

【中文翻译】
给定一个 m x n 的字符网格 grid。返回网格中是否存在由相同字符组成的环。
环是一条路径，起始和结束于同一个格子，长度 >= 4，且路径只能沿水平或垂直方向移动到相邻格子。

示例 1：
输入：grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
输出：true

示例 2：
输入：grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
输出：true

示例 3：
输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
输出：false
"""

from typing import List, Optional


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int, pi: int, pj: int, ch: str) -> bool:
            if visited[i][j]:
                return True
            visited[i][j] = True
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == ch:
                    if ni == pi and nj == pj:
                        continue
                    if dfs(ni, nj, i, j, ch):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# DFS 检测环。对于每个未访问的格子，进行 DFS 遍历相同字符的连通区域。
# 传递父节点坐标 (pi, pj) 以避免立即沿原路返回。
# 如果遇到已访问的相邻格子且不是父节点，则说明检测到了一个环（长度 >= 4 自然满足，
# 因为无向图中除了父节点外回到已访问节点一定形成环）。
#
# 时间复杂度: O(M * N) — 每个格子访问一次
# 空间复杂度: O(M * N) — visited 数组 + 递归栈
#
# 关键点:
# - 无向图 DFS 检测环需要排除父节点
# - 相同字符限制连通性
# - 遇到已访问节点（非父节点）即检测到环












