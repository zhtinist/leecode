"""
LeetCode #3001 - Minimum Moves to Capture The Queen
捕获黑皇后需要的最少移动次数
https://leetcode.cn/problems/minimum-moves-to-capture-the-queen/

现有一个下标从 1 开始的 `8 x 8` 棋盘，上面有 `3` 枚棋子。
给你 `6` 个整数 `a` 、`b` 、`c` 、`d` 、`e` 和 `f` ，其中：
`(a, b)` 表示白色车的位置。
`(c, d)` 表示白色象的位置。
`(e, f)` 表示黑皇后的位置。
假定你只能移动白色棋子，返回捕获黑皇后所需的最少移动次数。
请注意：
车可以向垂直或水平方向移动任意数量的格子，但不能跳过其他棋子。
象可以沿对角线方向移动任意数量的格子，但不能跳过其他棋子。
如果车或象能移向皇后所在的格子，则认为它们可以捕获皇后。
皇后不能移动。

示例 1：
输入：a = 1, b = 1, c = 8, d = 8, e = 2, f = 3 输出：2 解释：将白色车先移动到 (1, 3) ，然后移动到 (2, 3) 来捕获黑皇后，共需移动 2 次。 由于起始时没有任何棋子正在攻击黑皇后，要想捕获黑皇后，移动次数不可能少于 2 次。
示例 2：
输入：a = 5, b = 3, c = 3, d = 4, e = 5, f = 2 输出：1 解释：可以通过以下任一方式移动 1 次捕获黑皇后： - 将白色车移动到 (5, 2) 。 - 将白色象移动到 (5, 2) 。

提示：
`1 <= a, b, c, d, e, f <= 8`
两枚棋子不会同时出现在同一个格子上。
"""

from typing import List, Optional


class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        """
        Check if rook or bishop can capture in 1 move (without being blocked).
        Otherwise answer is always 2.
        """

        def between(x: int, lo: int, hi: int) -> bool:
            return min(lo, hi) < x < max(lo, hi)

        # Rook: same row (a == e) or same column (b == f)
        # Blocked by bishop if bishop is on the same line and between them
        if a == e:  # same row
            if not (c == a and between(d, b, f)):
                return 1
        if b == f:  # same column
            if not (d == b and between(c, a, e)):
                return 1

        # Bishop: same diagonal (|c-e| == |d-f|)
        # Blocked by rook if rook is on the same diagonal and between them
        if abs(c - e) == abs(d - f):
            if not (abs(a - e) == abs(b - f) and between(a, c, e)):
                return 1

        return 2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Enumeration
#
# 解题思路:
# 答案只有可能是 1 或 2。检查是否能在 1 步内捕获：
# - 车与皇后同行/同列且象不在中间阻挡 -> 1 步
# - 象与皇后同对角线且车不在中间阻挡 -> 1 步
# - 其他情况：总能在 2 步内捕获（车走两次，至少有一条路径不被象阻挡）
#
# 时间复杂度: O(1)，常数次坐标比较
# 空间复杂度: O(1)
#
# 关键点:
# - 答案只有 1 或 2：车可以在 2 步内到达棋盘任意位置
# - 阻挡判断：检查第三方棋子是否在攻击路径上且位于两者之间
# - 对角线阻挡只需检查行坐标是否在中间即可（对角线保证列坐标也对应在中间）
