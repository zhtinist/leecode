"""
LeetCode #3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
最少翻转次数使二进制矩阵回文 II
https://leetcode.cn/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

给你一个 `m x n` 的二进制矩阵 `grid` 。
如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。
你可以将 `grid` 中任意格子的值 翻转 ，也就是将格子里的值从 `0` 变成 `1` ，或者从 `1` 变成 `0` 。
请你返回 最少 翻转次数，使得矩阵中 所有 行和列都是 回文的 ，且矩阵中 `1` 的数目可以被 `4` 整除 。

示例 1：

输入：grid = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
解释：

示例 2：

输入：grid = [[0,1],[0,1],[0,0]]
输出：2
解释：

示例 3：

输入：grid = [[1],[1]]
输出：2
解释：

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m * n <= 2 * 10^5`
`0 <= grid[i][j] <= 1`
"""

from typing import List, Optional


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        # 1. 处理四元组（四个对称角）
        for i in range(m // 2):
            for j in range(n // 2):
                ones = (grid[i][j] + grid[i][n-1-j] +
                        grid[m-1-i][j] + grid[m-1-i][n-1-j])
                ans += min(ones, 4 - ones)

        diff = 0          # 不同的中间对数（必须翻一次，可选贡献 0 或 2 个 1）
        equal_ones = 0    # 已经相等的中间对中 1 的个数（每对贡献 2 个 1）

        # 2. 中间行 (m 为奇数)
        if m % 2 == 1:
            mid = m // 2
            for j in range(n // 2):
                if grid[mid][j] != grid[mid][n-1-j]:
                    ans += 1
                    diff += 1
                elif grid[mid][j] == 1:
                    equal_ones += 2

        # 3. 中间列 (n 为奇数)
        if n % 2 == 1:
            mid = n // 2
            for i in range(m // 2):
                if grid[i][mid] != grid[m-1-i][mid]:
                    ans += 1
                    diff += 1
                elif grid[i][mid] == 1:
                    equal_ones += 2

        # 4. 中心格子（行列均为奇数时）
        if m % 2 == 1 and n % 2 == 1:
            if grid[m // 2][n // 2] == 1:
                ans += 1  # 中心必须翻成 0

        # 5. 处理 1 的个数被 4 整除的条件
        # 四元组贡献的 1 已经是 4 的倍数；中间对和中心需要调整
        if equal_ones % 4 == 2:
            if diff > 0:
                pass  # 将一个 diff 对翻成 1（增加 2 个 1），总 1 数变为 %4==0，已在 ans 中
            else:
                ans += 2  # 将一对已有的 1 翻成 0

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, Matrix
#
# 解题思路:
# 需要同时满足所有行和列回文，且 1 的总数能被 4 整除。
# 行回文 + 列回文 → 四个对称位置的格子必须全部相等：(i,j), (i,n-1-j), (m-1-i,j), (m-1-i,n-1-j)
# 1. 处理四元组：cost += min(ones, 4-ones)，贡献的 1 数为 0 或 4，都是 4 的倍数
# 2. 处理中间行/列的对称对：每对如果不相等需要翻 1 次（可自由选 0 或 2 个 1）
# 3. 处理中心格子：必须为 0（否则 1 % 4 ≠ 0）
# 4. 最后调整：如果已配对 1 的数量 % 4 == 2：
#    - 如果有不同对（diff > 0），将一对不同的翻成 1 即可（无额外代价）
#    - 否则需额外翻 2 个 1 变 0
#
# 时间复杂度: O(m * n)
# 空间复杂度: O(1)
#
# 关键点:
# - 四种对称位置的等价性：行回文和列回文叠加后产生四元组约束
# - 不同对（diff）提供了灵活调整 1 的数量模 4 的能力
