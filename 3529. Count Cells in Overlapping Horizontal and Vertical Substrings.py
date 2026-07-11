"""
LeetCode #3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
统计水平子串和垂直子串重叠格子的数目
https://leetcode.cn/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

给你一个由字符组成的 `m x n` 矩阵 `grid` 和一个字符串 `pattern`。
水平子串 是从左到右的一段连续字符序列。如果子串到达了某行的末尾，它将换行并从下一行的第一个字符继续。不会 从最后一行回到第一行。
垂直子串 是从上到下的一段连续字符序列。如果子串到达了某列的底部，它将换列并从下一列的第一个字符继续。不会 从最后一列回到第一列。
请统计矩阵中满足以下条件的单元格数量：
该单元格必须属于 至少 一个等于 `pattern` 的水平子串，且属于 至少 一个等于 `pattern` 的垂直子串。
返回满足条件的单元格数量。

示例 1：

输入： grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","b","a"]], pattern = "abaca"
输出： 1
解释：
`"abaca"` 作为一个水平子串（蓝色）和一个垂直子串（红色）各出现一次，并在一个单元格（紫色）处相交。
示例 2：

输入： grid = [["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]], pattern = "aba"
输出： 4
解释：
上述被标记的单元格都同时属于至少一个 `"aba"` 的水平和垂直子串。
示例 3：

输入： grid = [["a"]], pattern = "a"
输出： 1

提示：
`m == grid.length`
`n == grid[i].length`
`1 <= m, n <= 1000`
`1 <= m * n <= 10^5`
`1 <= pattern.length <= m * n`
`grid` 和 `pattern` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])
        total = m * n
        plen = len(pattern)

        # Build KMP prefix function
        def build_kmp(s):
            pi = [0] * len(s)
            for i in range(1, len(s)):
                j = pi[i - 1]
                while j > 0 and s[i] != s[j]:
                    j = pi[j - 1]
                if s[i] == s[j]:
                    j += 1
                pi[i] = j
            return pi

        # KMP match: return list of start positions in text
        def kmp_match(text, pat, pi):
            res = []
            j = 0
            for i, ch in enumerate(text):
                while j > 0 and ch != pat[j]:
                    j = pi[j - 1]
                if ch == pat[j]:
                    j += 1
                if j == len(pat):
                    res.append(i - j + 1)
                    j = pi[j - 1]
            return res

        pi = build_kmp(pattern)

        # Horizontal: flatten row by row
        horiz = ''.join(''.join(row) for row in grid)
        horiz_matches = kmp_match(horiz, pattern, pi)
        horiz_cells = [False] * total
        for start in horiz_matches:
            for k in range(plen):
                pos = start + k
                r = pos // n
                c = pos % n
                horiz_cells[r * n + c] = True

        # Vertical: flatten column by column
        vert_list = []
        for c in range(n):
            for r in range(m):
                vert_list.append(grid[r][c])
        vert = ''.join(vert_list)
        vert_matches = kmp_match(vert, pattern, pi)
        vert_cells = [False] * total
        for start in vert_matches:
            for k in range(plen):
                pos = start + k
                r = pos % m
                c = pos // m
                vert_cells[r * n + c] = True

        # Count overlap
        ans = 0
        for i in range(total):
            if horiz_cells[i] and vert_cells[i]:
                ans += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String, Matrix, String Matching, Hash Function, Rolling Hash
#
# 解题思路:
# 1. 使用 KMP 算法进行高效字符串匹配
# 2. 水平方向：将 grid 按行展开为一维字符串，匹配 pattern，标记匹配位置所在的单元格
# 3. 垂直方向：将 grid 按列展开为一维字符串，同样匹配并标记
# 4. 统计同时被水平匹配和垂直匹配标记的单元格数量
# 5. 一维位置到二维坐标的映射：
#    - 水平展开：pos → (pos // n, pos % n)
#    - 垂直展开：pos → (pos % m, pos // m)
#
# 时间复杂度: O(m*n + matches * plen)
# 空间复杂度: O(m*n)
#
# 关键点:
# - KMP 在 O(N+M) 时间内完成匹配
# - 水平和垂直使用不同的展开方式
# - 坐标转换需正确对应行列
