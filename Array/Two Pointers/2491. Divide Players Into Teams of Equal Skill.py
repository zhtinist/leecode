"""
LeetCode #2491 - Divide Players Into Teams of Equal Skill
划分技能点相等的团队
https://leetcode.cn/problems/divide-players-into-teams-of-equal-skill/

给你一个正整数数组 `skill` ，数组长度为 偶数 `n` ，其中 `skill[i]` 表示第 `i` 个玩家的技能点。将所有玩家分成 `n / 2` 个 `2` 人团队，使每一个团队的技能点之和 相等 。
团队的 化学反应 等于团队中玩家的技能点 乘积 。
返回所有团队的 化学反应 之和，如果无法使每个团队的技能点之和相等，则返回 `-1` 。

示例 1：
输入：skill = [3,2,5,1,3,4] 输出：22 解释： 将玩家分成 3 个团队 (1, 5), (2, 4), (3, 3) ，每个团队的技能点之和都是 6 。 所有团队的化学反应之和是 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22 。
示例 2：
输入：skill = [3,4] 输出：12 解释： 两个玩家形成一个团队，技能点之和是 7 。 团队的化学反应是 3 * 4 = 12 。
示例 3：
输入：skill = [1,1,2,3] 输出：-1 解释： 无法将玩家分成每个团队技能点都相等的若干个 2 人团队。

提示：
`2 <= skill.length <= 10^5`
`skill.length` 是偶数
`1 <= skill[i] <= 1000`
"""

from typing import List, Optional


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        排序 + 双指针配对：
        - 将 skill 数组排序
        - 每对由最小值和最大值配对：skill[i] + skill[n-1-i]
        - 所有配对的和必须相等，否则返回 -1
        - 若全部匹配则累加每对乘积
        """
        skill.sort()
        n = len(skill)
        target = skill[0] + skill[n - 1]
        total_chemistry = 0

        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target:
                return -1
            total_chemistry += skill[i] * skill[n - 1 - i]

        return total_chemistry



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Two Pointers, Sorting
#
# 解题思路:
# 为了使每个团队的技能点之和相等，排序后最优策略是让最小值和最大值配对、次小值和
# 次大值配对，依此类推。首先计算目标团队技能和 target = skill[0] + skill[n-1]。
# 然后用双指针遍历，检查每一对的和是否等于 target：若不相等则直接返回 -1；
# 若全部匹配成功，则累加每对技能的乘积作为总化学反应值。
#
# 时间复杂度: O(n log n) — 主要开销来自排序
# 空间复杂度: O(1) — 排序通常是原地排序（O(log n) 递归栈不计入数据空间）
#
# 关键点:
# - 排序后最小配最大是唯一可能的配对方式（若解存在）
# - target 由最小和最大元素之和确定，无需猜测
# - 数组长度为偶数，恰好能配成 n/2 对
# - 技能值范围小（1~1000）也可以用计数排序做到 O(n)
