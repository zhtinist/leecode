"""
LeetCode #1996 - The Number of Weak Characters in the Game
游戏中弱角色的数量
https://leetcode.cn/problems/the-number-of-weak-characters-in-the-game/

你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 `properties` ，其中 `properties[i] = [attack_i, defense_i]` 表示游戏中第 `i` 个角色的属性。
如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，如果认为角色 `i` 弱于 存在的另一个角色 `j` ，那么 `attack_j > attack_i` 且 `defense_j > defense_i` 。
返回 弱角色 的数量。

示例 1：
输入：properties = [[5,5],[6,3],[3,6]] 输出：0 解释：不存在攻击和防御都严格高于其他角色的角色。
示例 2：
输入：properties = [[2,2],[3,3]] 输出：1 解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。
示例 3：
输入：properties = [[1,5],[10,4],[4,3]] 输出：1 解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。

提示：
`2 <= properties.length <= 10^5`
`properties[i].length == 2`
`1 <= attack_i, defense_i <= 10^5`
"""

from typing import List, Optional


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        Sort by attack descending, then by defense ascending.
        Track max_defense seen so far. If current defense < max_defense,
        this character is weak (there exists a character with higher attack
        AND higher defense).
        """
        # Sort: attack descending, defense ascending (for same attack)
        properties.sort(key=lambda x: (-x[0], x[1]))

        ans = 0
        max_defense = 0

        for _, defense in properties:
            if defense < max_defense:
                ans += 1
            else:
                max_defense = defense

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, Array, Sorting, Monotonic Stack
#
# 解题思路:
# 排序技巧：按攻击力降序排列。攻击力相同时按防御力升序排列。
# 这样，遍历时攻击力不会成为问题（已经降序），只需比较防御力。
# 维护当前遇到的最大防御力 max_defense。
# 如果当前角色的防御力 < max_defense，说明之前有角色攻击力 >= 当前角色
# 且防御力 > 当前角色。由于同攻击力按防御升序，同攻击力不会误判。
# 满足弱角色条件，计数 +1。
#
# 时间复杂度: O(N log N)，排序
# 空间复杂度: O(1)，不计排序空间
#
# 关键点:
# - 排序键：(-attack, defense)：攻击降序，防御升序
# - 同攻击力升序防御避免了误判
# - 维护 max_defense 即可判断是否有严格更大的双属性角色
