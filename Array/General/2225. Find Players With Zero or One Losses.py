"""
LeetCode #2225 - Find Players With Zero or One Losses
找出输掉零场或一场比赛的玩家
https://leetcode.cn/problems/find-players-with-zero-or-one-losses/

给你一个整数数组 `matches` 其中 `matches[i] = [winner_i, loser_i]` 表示在一场比赛中 `winner_i` 击败了 `loser_i` 。
返回一个长度为 2 的列表 `answer` ：
`answer[0]` 是所有 没有 输掉任何比赛的玩家列表。
`answer[1]` 是所有恰好输掉 一场 比赛的玩家列表。
两个列表中的值都应该按 递增 顺序返回。
注意：
只考虑那些参与 至少一场 比赛的玩家。
生成的测试用例保证 不存在 两场比赛结果 相同 。

示例 1：
输入：matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]] 输出：[[1,2,10],[4,5,7,8]] 解释： 玩家 1、2 和 10 都没有输掉任何比赛。 玩家 4、5、7 和 8 每个都输掉一场比赛。 玩家 3、6 和 9 每个都输掉两场比赛。 因此，answer[0] = [1,2,10] 和 answer[1] = [4,5,7,8] 。
示例 2：
输入：matches = [[2,3],[1,3],[5,4],[6,4]] 输出：[[1,2,5,6],[]] 解释： 玩家 1、2、5 和 6 都没有输掉任何比赛。 玩家 3 和 4 每个都输掉两场比赛。 因此，answer[0] = [1,2,5,6] 和 answer[1] = [] 。

提示：
`1 <= matches.length <= 10^5`
`matches[i].length == 2`
`1 <= winner_i, loser_i <= 10^5`
`winner_i != loser_i`
所有 `matches[i]` 互不相同
"""

from typing import List, Optional


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict

        loss_count = defaultdict(int)  # 记录每个玩家的输场数
        players = set()                # 所有参与至少一场的玩家

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_count[loser] += 1

        # 一场未输的玩家：出现在 players 中但 loss_count 为 0
        zero_loss = sorted([p for p in players if loss_count[p] == 0])
        # 恰好输一场的玩家
        one_loss = sorted([p for p in players if loss_count[p] == 1])

        return [zero_loss, one_loss]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Counting, Sorting
#
# 解题思路:
# 使用哈希表统计每位玩家的输场数，同时用集合记录所有参与过比赛的玩家。
# 赢家可能从未出现在 loser 列中，所以 loss_count 默认为 0。
# 遍历所有比赛：将 winner 和 loser 都加入玩家集合，并为 loser 的输场数加 1。
# 最后筛选输场数为 0 和 1 的玩家，分别排序后返回。
#
# 时间复杂度: O(N log N) 其中 N 为玩家数量，排序占主导
# 空间复杂度: O(N) 存储所有玩家和输场计数
#
# 关键点:
# - 使用 defaultdict(int) 避免检查 key 是否存在，默认为 0
# - 赢家可能从未输过（不在 loss_count 中），其输场数即为默认值 0
# - 只考虑参与至少一场比赛的玩家，所以需要 players 集合
