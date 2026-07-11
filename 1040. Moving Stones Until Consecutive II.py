"""
LeetCode #1040 - Moving Stones Until Consecutive II
中文题名：移动石子直到连续 II
https://leetcode.com/problems/moving-stones-until-consecutive-ii/

On an infinite number line, the position of the i-th stone is given by `stones[i]`.
Call a stone an endpoint stone if it has the smallest or largest position.

Each turn, you pick up an endpoint stone and move it to an unoccupied position so that it is
no longer an endpoint stone.

In particular, if the stones are at say, `stones = [1,2,5]`, you cannot
move the endpoint stone at position 5, since moving it to any position (such as 0, or 3)
will still keep that stone as an endpoint stone.

The game ends when you cannot make any more moves, ie. the stones are in consecutive
positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?
Return the answer as an length 2 array: `answer = [minimum_moves,
maximum_moves]`

Example 1:

Input: [7,4,9]
Output: [1,2]
Explanation:
We can move 4 -> 8 for one move to finish the game.
Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.

Example 2:

Input: [6,5,4,3,10]
Output: [2,3]
We can move 3 -> 8 then 10 -> 7 to finish the game.
Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
Notice we cannot move 10 -> 2 to finish the game, because that would be an illegal move.

Example 3:

Input: [100,101,104,102,103]
Output: [0,0]

【中文翻译】
在一个无限长的数轴上，第 i 颗石子的位置为 stones[i]。如果一颗石子具有最小或最大的位置，我们称其为端点石子。

每一回合，你拿起一颗端点石子并将其移动到一个未被占据的位置，使得该石子不再是端点石子。

特别地，如果石子在例如 stones = [1,2,5] 的位置上，你不能移动位置 5 的端点石子，因为将其移动到任何位置（如 0 或 3）仍会使该石子成为端点石子。

当无法进行任何移动时游戏结束，即石子处于连续位置。

游戏结束时，你最多和最少可以移动多少次？返回一个长度为 2 的数组：answer = [最少移动次数, 最多移动次数]。

示例 1：

输入：[7,4,9]
输出：[1,2]
解释：
我们可以移动 4 -> 8，一次移动完成游戏。
或者，我们可以移动 9 -> 5, 4 -> 6，两次移动完成游戏。

示例 2：

输入：[6,5,4,3,10]
输出：[2,3]
解释：
我们可以移动 3 -> 8 然后 10 -> 7 完成游戏。
或者，移动 3 -> 7, 4 -> 8, 5 -> 9 完成游戏。
注意我们不能移动 10 -> 2 来完成游戏，因为那是非法移动。

示例 3：

输入：[100,101,104,102,103]
输出：[0,0]
"""

from typing import List, Optional


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)

        # Maximum moves
        # After first move, we fill gaps one by one
        # Choose to keep either leftmost or rightmost endpoint
        max_moves = max(
            stones[-1] - stones[1] - (n - 2),
            stones[-2] - stones[0] - (n - 2)
        )

        # Minimum moves using sliding window
        min_moves = n
        j = 0
        for i in range(n):
            # Window [i, j] where stones[j] - stones[i] + 1 <= n
            while j < n and stones[j] - stones[i] + 1 <= n:
                j += 1
            # Stones in window: from i to j-1
            in_window = j - i
            if in_window == n - 1 and stones[j - 1] - stones[i] + 1 == n - 1:
                # Special case: n-1 consecutive stones, need 2 moves
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - in_window)

        return [min_moves, max_moves]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 先对石子位置排序。
#
# 最大移动次数：
# 第一次移动后，选择保留最左或最右的端点。保留最左端点时，右端点石子每次向内移动一步，
# 需要填补的空格数为 stones[n-1] - stones[1] + 1 - n（即最右到第二左之间的空位数）。
# 同理保留最右端点时，空格数为 stones[n-2] - stones[0] + 1 - n。
# 取两者中的较大值，即 max(stones[-1]-stones[1], stones[-2]-stones[0]) - (n-2)。
#
# 最小移动次数：
# 使用滑动窗口。由于最终石子需要连续且占据n个位置，窗口大小固定为n。
# 对每个起点i，找到一个窗口[stones[i], stones[i]+n-1]内已有的石子数。
# 需要移动的石子数 = n - 已有石子数。
# 特殊情况：如果有n-1个石子已经连续排列，而最后一个石子不在旁边（距离>1），
# 需要2步（因为第一步移动端点石子变为非端点，第二步移动到连续位置）。
#
# 时间复杂度: O(N log N) - 排序开销
# 空间复杂度: O(1) - 只使用常量额外空间
#
# 关键点:
# - 最大移动：第一次移动后端点的选择决定了后续能填多少格
# - 最小移动：滑动窗口找到已有石子最多的区间
# - 特殊处理 n-1 个连续石子加一个远端点的情况
