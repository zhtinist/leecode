"""
LeetCode #2018 - Check if Word Can Be Placed In Crossword
判断单词是否能放入填字游戏内
https://leetcode.cn/problems/check-if-word-can-be-placed-in-crossword/

给你一个 `m x n` 的矩阵 `board` ，它代表一个填字游戏 当前 的状态。填字游戏格子中包含小写英文字母（已填入的单词），表示 空 格的 `' '` 和表示 障碍 格子的 `'#'` 。
如果满足以下条件，那么我们可以 水平 （从左到右 或者 从右到左）或 竖直 （从上到下 或者 从下到上）填入一个单词：
该单词不占据任何 `'#'` 对应的格子。
每个字母对应的格子要么是 `' '` （空格）要么与 `board` 中已有字母 匹配 。
如果单词是 水平 放置的，那么该单词左边和右边 相邻 格子不能为 `' '` 或小写英文字母。
如果单词是 竖直 放置的，那么该单词上边和下边 相邻 格子不能为 `' '` 或小写英文字母。
给你一个字符串 `word` ，如果 `word` 可以被放入 `board` 中，请你返回 `true` ，否则请返回 `false` 。

示例 1：

输入：board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc" 输出：true 解释：单词 "abc" 可以如上图放置（从上往下）。
示例 2：

输入：board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac" 输出：false 解释：无法放置单词，因为放置该单词后上方或者下方相邻格会有空格。
示例 3：

输入：board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca" 输出：true 解释：单词 "ca" 可以如上图放置（从右到左）。

提示：
`m == board.length`
`n == board[i].length`
`1 <= m * n <= 2 * 10^5`
`board[i][j]` 可能为 `' '` ，`'#'` 或者一个小写英文字母。
`1 <= word.length <= max(m, n)`
`word` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)

        def can_place(seg: List[str], w: str) -> bool:
            if len(seg) != len(w):
                return False
            # Check forward
            ok_forward = all(seg[i] == ' ' or seg[i] == w[i] for i in range(len(w)))
            # Check backward
            ok_backward = all(seg[i] == ' ' or seg[i] == w[-1 - i] for i in range(len(w)))
            return ok_forward or ok_backward

        # Check each row for horizontal placement
        for row in board:
            # Split by '#', get candidate segments
            seg = []
            for ch in row:
                if ch == '#':
                    if can_place(seg, word):
                        return True
                    seg = []
                else:
                    seg.append(ch)
            if can_place(seg, word):
                return True

        # Check each column for vertical placement
        for j in range(n):
            seg = []
            for i in range(m):
                ch = board[i][j]
                if ch == '#':
                    if can_place(seg, word):
                        return True
                    seg = []
                else:
                    seg.append(ch)
            if can_place(seg, word):
                return True

        return False



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Enumeration, Matrix
#
# 解题思路:
# 将board按行和列分别扫描，用'#'作为分隔符提取出连续的空白/字母段。
# 对每个段，检查单词是否可以在该段中放置（正向或反向匹配）。
# 空白格' '可以匹配任意字母，已有字母必须和单词对应位置一致。
#
# 时间复杂度: O(m * n)
# 空间复杂度: O(max(m, n))
#
# 关键点:
# - 用'#'分隔获取候选段
# - 同时检查正向和反向匹配
# - 行列分别处理，覆盖水平和垂直放置
