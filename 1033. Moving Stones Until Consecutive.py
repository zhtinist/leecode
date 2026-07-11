"""
LeetCode #1033 - Moving Stones Until Consecutive
中文题名：移动石子直到连续
https://leetcode.com/problems/moving-stones-until-consecutive/

Three stones are on a number line at positions `a`, `b`, and
`c`.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position
stone), and move it to an unoccupied position between those endpoints.  Formally,
let's say the stones are currently at positions `x, y, z` with `x < y
< z`.  You pick up the stone at either position `x` or position
`z`, and move that stone to an integer position `k`, with `x <
k < z` and `k != y`.

The game ends when you cannot make any more moves, ie. the stones are in consecutive
positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?
Return the answer as an length 2 array: `answer = [minimum_moves, maximum_moves]`

Example 1:

Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.

Example 2:

Input: a = 4, b = 3, c = 2
Output: [0,0]
Explanation: We cannot make any moves.

Example 3:

Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.

【中文翻译】
三颗石子放在数轴上，位置分别为 a、b 和 c。

每一回合，你可以从端点拿起一颗石子（即处于最低或最高位置的石子），并将其移动到端点之间的一个未被占据的位置。形式化地，假设石子当前位于位置 x, y, z，其中 x < y < z。你拿起位于位置 x 或位置 z 的一颗石子，将该石子移动到整数位置 k，其中 x < k < z 且 k != y。

当无法进行任何移动时游戏结束，即石子处于连续位置。

游戏结束时，你最多和最少可以移动多少次？返回一个长度为 2 的数组：answer = [最少移动次数, 最多移动次数]。

示例 1：

输入：a = 1, b = 2, c = 5
输出：[1,2]
解释：将石子从 5 移到 3，或将石子从 5 移到 4 再到 3。

示例 2：

输入：a = 4, b = 3, c = 2
输出：[0,0]
解释：我们无法进行任何移动。

示例 3：

输入：a = 3, b = 5, c = 1
输出：[1,2]
解释：将石子从 1 移到 4；或将石子从 1 移到 2 再到 4。
"""

from typing import List, Optional


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])

        # Maximum moves: move endpoints one step inward at a time
        max_moves = z - x - 2

        # Minimum moves
        if z - x == 2:
            min_moves = 0
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1
        else:
            min_moves = 2

        return [min_moves, max_moves]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 首先将三个位置排序为 x < y < z。
# 最大移动次数：每次只能移动端点石子，且只能移动到另一个端点和中间石子之间的空位。
# 最大移动次数 = z - x - 2（每次移动一步，将端点向中间靠拢，填满所有空格）。
# 最小移动次数：
# - 如果已经连续 (z - x == 2)，需要 0 步
# - 如果 y - x <= 2 或 z - y <= 2，只需要 1 步（将一个端点直接放到另一个端点旁边）
# - 否则需要 2 步
#
# 时间复杂度: O(1) - 常数时间
# 空间复杂度: O(1) - 常数空间
#
# 关键点:
# - 最大移动次数等于所有空格数之和：z - x - 2
# - 最小移动次数只需判断三个位置的间距是否 <= 2
# - 当两个石子相邻或只隔一个空位时，可以一步将另一个石子移到紧邻位置
