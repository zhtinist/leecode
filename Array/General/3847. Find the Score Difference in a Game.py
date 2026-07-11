"""
LeetCode #3847 - Find the Score Difference in a Game
计算比赛分数差
https://leetcode.cn/problems/find-the-score-difference-in-a-game/

给你一个整数数组 `nums`，其中 `nums[i]` 表示在第 `i` 场比赛中获得的分数。
恰好 有两位玩家。初始时，第一位玩家为 主动玩家，第二位玩家为 被动玩家。
按顺序 将下述规则应用于每场比赛 `i`：
如果 `nums[i]` 是奇数，主动玩家和被动玩家互换角色。
在每第 6 场比赛（即比赛索引为 `5, 11, 17, ...` 的比赛中），主动玩家和被动玩家互换角色。
主动玩家参与第 `i` 场比赛，并获得 `nums[i]` 分。
返回 分数差，即第一位玩家的 总分 减去第二位玩家的 总分 。

示例 1：

输入： nums = [1,2,3]
输出： 0
解释：​​​​​​​
第 0 场比赛：分数为奇数，第二位玩家成为主动玩家，获得 `nums[0] = 1` 分。
第 1 场比赛：没有交换角色。第二位玩家获得 `nums[1] = 2` 分。
第 2 场比赛：分数为奇数，第一位玩家成为主动玩家，获得 `nums[2] = 3` 分。
分数差为 `3 - 3 = 0`。
示例 2：

输入： nums = [2,4,2,1,2,1]
输出： 4
解释：
第 0 到第 2 场比赛：第一位玩家获得 `2 + 4 + 2 = 8` 分。
第 3 场比赛：分数为奇数，第二位玩家成为主动玩家，获得 `nums[3] = 1` 分。
第 4 场比赛：第二位玩家获得 `nums[4] = 2` 分。
第 5 场比赛：分数为奇数，玩家互换角色。由于这是第 6 场比赛，玩家再次互换角色。第二位玩家获得 `nums[5] = 1` 分。
分数差为 `8 - 4 = 4`。
示例 3：

输入： nums = [1]
输出： -1
解释：
第 0 场比赛：分数为奇数，第二位玩家成为主动玩家，获得 `nums[0] = 1` 分。
分数差为 `0 - 1 = -1`。

提示：
`1 <= nums.length <= 1000`
`1 <= nums[i] <= 1000`
"""

from typing import List, Optional


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        """
        Simulate the game turn by turn, tracking which player is active.
        Player 1 is active initially (active = 0 means P1, active = 1 means P2).
        On each turn:
          - If nums[i] is odd, swap the active player.
          - If this is every 6th game (1-indexed: (i+1) % 6 == 0), swap again.
          - The active player earns nums[i] points.
        Return P1_total - P2_total.
        """
        p1_score = 0
        p2_score = 0
        active = 0  # 0 for player 1, 1 for player 2

        for i, score in enumerate(nums):
            if score % 2 == 1:
                active = 1 - active
            if (i + 1) % 6 == 0:
                active = 1 - active

            if active == 0:
                p1_score += score
            else:
                p2_score += score

        return p1_score - p2_score










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Simulation
#
# 解题思路:
# 模拟比赛过程，维护当前主动玩家的标识（0 表示玩家1，1 表示玩家2）。
# 遍历每一场比赛 i：
#   1. 如果 nums[i] 是奇数，交换主动玩家（active = 1 - active）。
#   2. 如果这是第6场比赛（即 (i+1) % 6 == 0），再次交换。
#   3. 当前主动玩家获得 nums[i] 分。
# 最后返回 P1 总分 - P2 总分。
#
# 时间复杂度: O(n)，其中 n 是 nums 的长度，只需一次遍历。
# 空间复杂度: O(1)，只使用了常数额外空间。
#
# 关键点:
# - 两个交换条件是独立的，都需要依次应用。
# - 注意使用 1-indexed 来判断每6场比赛：(i+1) % 6 == 0。
# - 奇数检查和每6场检查的顺序不影响结果，因为每次都是翻转状态。
