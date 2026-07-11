"""
LeetCode #777 - Swap Adjacent in LR String
中文题名：在 LR 字符串中交换相邻字符
https://leetcode.com/problems/swap-adjacent-in-lr-string/

In a string composed of `'L'`, `'R'`, and `'X'`
characters, like `"RXXLRXRXL"`, a move consists of either replacing one
occurrence of `"XL"` with `"LX"`, or replacing one
occurrence of `"RX"` with `"XR"`. Given the
starting string `start` and the ending string `end`, return
`True` if and only if there exists a sequence of moves to transform one string to
the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Note:

`1 <= len(start) = len(end) <= 10000`.

Both start and end will only consist of characters in `{'L', 'R',
'X'}`.

【中文翻译】
在一个由 `'L'`、`'R'` 和 `'X'` 组成的字符串中，如 `"RXXLRXRXL"`，一次移动包括将一处出现的 `"XL"` 替换为 `"LX"`，或将一处出现的 `"RX"` 替换为 `"XR"`。给定起始字符串 `start` 和结束字符串 `end`，当且仅当存在一系列移动将起始字符串转换为结束字符串时，返回 `True`。

示例：

输入：start = "RXXLRXRXL", end = "XRLXXRRLX"
输出：True
解释：我们可以通过以下步骤将 start 转换为 end：
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

注意：

`1 <= len(start) = len(end) <= 10000`。

start 和 end 都只包含 `{'L', 'R', 'X'}` 中的字符。
"""

from typing import List, Optional


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # L can only move left (XL -> LX), so its position in start must be >= in end
        # R can only move right (RX -> XR), so its position in start must be <= in end
        # The relative order of L and R (ignoring X) must be preserved
        if start.replace('X', '') != end.replace('X', ''):
            return False

        n = len(start)
        i = j = 0
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i == n and j == n:
                return True
            if i == n or j == n:
                return False
            if start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                return False  # L cannot move right
            if start[i] == 'R' and i > j:
                return False  # R cannot move left
            i += 1
            j += 1
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 规则分析 + 双指针。
# 分析两种操作：
# - "XL" -> "LX" 表示 L 可以向左移动（跨越 X）
# - "RX" -> "XR" 表示 R 可以向右移动（跨越 X）
# 关键约束：
# 1. L 和 R 不能互相穿过（无 "LR" -> "RL" 操作）。
# 2. 忽略所有 X 后，start 和 end 必须完全相同（L/R 相对顺序不变）。
# 3. start 中的 L 位置必须 >= end 中对应的 L 位置（L 只能左移）。
# 4. start 中的 R 位置必须 <= end 中对应的 R 位置（R 只能右移）。
# 使用双指针跳过 X，同时比较两个字符串中的 L/R 及位置。
#
# 时间复杂度: O(N) - 一次遍历两个字符串
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - L 只能向左移动，R 只能向右移动
# - 去掉 X 后两字符串必须完全相同
# - 双指针跳过 X，逐一比较 L/R 及其相对位置
# - 位置约束：L 只能从右往左移（start 位置 >= end 位置），R 反之
