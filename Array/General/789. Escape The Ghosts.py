"""
LeetCode #789 - Escape The Ghosts
中文题名：逃脱阻碍者
https://leetcode.com/problems/escape-the-ghosts/

You are playing a simplified Pacman game. You start at the point `(0, 0)`,
and your destination is` (target[0], target[1])`. There are several ghosts on the
map, the i-th ghost starts at` (ghosts[i][0], ghosts[i][1])`.

Each turn, you and all ghosts simultaneously *may* move in one of 4 cardinal directions:
north, east, west, or south, going from the previous point to a new point 1 unit of distance
away.

You escape if and only if you can reach the target before any ghost reaches you (for any
given moves the ghosts may take.)  If you reach any square (including the target) at
the same time as a ghost, it doesn't count as an escape.

Return True if and only if it is possible to escape.

Example 1:
Input:
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
Output: true
Explanation:
You can directly reach the destination (0, 1) at time 1, while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.

Example 2:
Input:
ghosts = [[1, 0]]
target = [2, 0]
Output: false
Explanation:
You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.

Example 3:
Input:
ghosts = [[2, 0]]
target = [1, 0]
Output: false
Explanation:
The ghost can reach the target at the same time as you.

Note:

All points have coordinates with absolute value <= `10000`.

The number of ghosts will not exceed `100`.

【中文翻译】
你正在玩一个简化版的吃豆人游戏。你从点 `(0, 0)` 出发，目的地是 `(target[0], target[1])`。地图上有一些鬼魂，第 i 个鬼魂从 `(ghosts[i][0], ghosts[i][1])` 出发。

每个回合，你和所有鬼魂可以同时沿四个基本方向之一移动：北、东、西或南，从之前的点移动到距离 1 单位的新点。

当且仅当你能够在任何鬼魂抓到你之前到达目标时，你才算逃脱。（如果你和鬼魂同时到达同一个方格（包括目标），不算逃脱。）

当且仅当可能逃脱时返回 True。

示例 1：
输入：
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
输出：true
解释：你可以直接在第 1 时刻到达目的地 (0, 1)，而位于 (1, 0) 或 (0, 3) 的鬼魂无法追上你。

示例 2：
输入：
ghosts = [[1, 0]]
target = [2, 0]
输出：false
解释：你需要到达目的地 (2, 0)，但位于 (1, 0) 的鬼魂在你和目的地之间。

示例 3：
输入：
ghosts = [[2, 0]]
target = [1, 0]
输出：false
解释：鬼魂可以与你同时到达目标。

注意：

所有点的坐标绝对值 <= `10000`。

鬼魂数量不超过 `100`。
"""

from typing import List, Optional


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_dist = abs(target[0]) + abs(target[1])
        for gx, gy in ghosts:
            ghost_dist = abs(gx - target[0]) + abs(gy - target[1])
            if ghost_dist <= my_dist:
                return False
        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学 / 曼哈顿距离。
# 核心问题转化为：玩家到目标的距离是否严格小于每个鬼魂到目标的距离。
# 因为在每一步中，玩家和鬼魂的移动速度和规则相同。
# 如果存在鬼魂的曼哈顿距离 d(ghost, target) <= d(player, target)，
# 那么鬼魂可以先到达目标或在目标处拦截玩家。
# 鬼魂无需追逐玩家，只需直接走向目标等待即可。
# 因此只需计算：
# - 玩家到目标距离：|target[0]| + |target[1]|（从 (0,0) 出发）
# - 每个鬼魂到目标距离：|gx - target[0]| + |gy - target[1]|
# 如果所有鬼魂距离都大于玩家距离，返回 True；否则 False。
#
# 时间复杂度: O(G)，其中 G 是鬼魂数量
# 空间复杂度: O(1)
#
# 关键点:
# - 鬼魂无需追逐玩家，直接去目标点拦截即可
# - 只需比较曼哈顿距离
# - 玩家距离 < 所有鬼魂距离 => 逃脱
# - 鬼魂之间互不影响，每个鬼魂独立判断
