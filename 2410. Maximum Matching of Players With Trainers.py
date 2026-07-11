"""
LeetCode #2410 - Maximum Matching of Players With Trainers
运动员和训练师的最大匹配数
https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/

给你一个下标从 0 开始的整数数组 `players` ，其中 `players[i]` 表示第 `i` 名运动员的 能力 值，同时给你一个下标从 0 开始的整数数组 `trainers` ，其中 `trainers[j]` 表示第 `j` 名训练师的 训练能力值 。
如果第 `i` 名运动员的能力值 小于等于 第 `j` 名训练师的能力值，那么第 `i` 名运动员可以 匹配 第 `j` 名训练师。除此以外，每名运动员至多可以匹配一位训练师，每位训练师最多可以匹配一位运动员。
请你返回满足上述要求 `players` 和 `trainers` 的 最大 匹配数。

示例 1：
输入：players = [4,7,9], trainers = [8,2,5,8] 输出：2 解释： 得到两个匹配的一种方案是： - players[0] 与 trainers[0] 匹配，因为 4 <= 8 。 - players[1] 与 trainers[3] 匹配，因为 7 <= 8 。 可以证明 2 是可以形成的最大匹配数。
示例 2：
输入：players = [1,1,1], trainers = [10] 输出：1 解释： 训练师可以匹配所有 3 个运动员 每个运动员至多只能匹配一个训练师，所以最大答案是 1 。

提示：
`1 <= players.length, trainers.length <= 10^5`
`1 <= players[i], trainers[j] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p_idx = t_idx = 0
        matches = 0
        while p_idx < len(players) and t_idx < len(trainers):
            if players[p_idx] <= trainers[t_idx]:
                matches += 1
                p_idx += 1
                t_idx += 1
            else:
                t_idx += 1
        return matches



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Two Pointers, Sorting
#
# 解题思路:
# 贪心匹配：将运动员和训练师按能力值排序。
# 双指针遍历：对于每个训练师，若当前运动员能力≤训练师能力，则匹配成功，
# 两个指针同时前进；否则训练师能力不足，跳过该训练师。
# 这种贪心策略可以保证最大匹配数。
#
# 时间复杂度: O(n log n + m log m)，排序主导，n为运动员数，m为训练师数。
# 空间复杂度: O(1)，忽略排序的栈空间，只使用常数额外空间。
#
# 关键点:
# - 排序后贪心匹配是最优策略：优先满足能力低的运动员。
# - 双指针渐进匹配，每个元素最多访问一次。
