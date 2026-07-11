"""
LeetCode #3096 - Minimum Levels to Gain More Points
得到更多分数的最少关卡数目
https://leetcode.cn/problems/minimum-levels-to-gain-more-points/

给你一个长度为 `n` 的二进制数组 `possible` 。
Alice 和 Bob 正在玩一个有 `n` 个关卡的游戏，游戏中有一些关卡是 困难 模式，其他的关卡是 简单 模式。如果 `possible[i] == 0` ，那么第 `i` 个关卡是 困难 模式，两个玩家 都不可能 通过。一个玩家通过一个简单模式的关卡可以获得 `1` 分，遇到困难模式的关卡将失去 `1` 分。
游戏的一开始，Alice 将从第 `0` 级开始 按顺序 完成一些关卡，然后 Bob 会完成剩下的所有关卡。
假设两名玩家都采取最优策略，目的是 最大化 自己的得分，Alice 想知道自己 最少 需要完成多少个关卡，才能获得比 Bob 更多的分数。
请你返回 Alice 获得比 Bob 更多的分数所需要完成的 最少 关卡数目，如果 无法 达成，那么返回 `-1` 。
注意，每个玩家都至少需要完成 `1` 个关卡。

示例 1：

输入：possible = [1,0,1,0]
输出：1
解释：
我们来看一下 Alice 可以完成的关卡数目：
如果 Alice 只完成关卡 0 ，Bob 完成剩下的所有关卡，那么 Alice 获得 1 分，Bob 获得 -1 + 1 - 1 = -1 分。
如果 Alice 完成到关卡 1 ，Bob 完成剩下的所有关卡，那么 Alice 获得 1 - 1 = 0 分，Bob 获得 1 - 1 = 0 分。
如果 Alice 完成到关卡 2 ，Bob 完成剩下的所有关卡，那么 Alice 获得 1 - 1 + 1 = 1 分，Bob 获得 -1 分。
Alice 需要完成至少一个关卡获得更多的分数。
示例 2：

输入：possible = [1,1,1,1,1]
输出：3
解释：
我们来看一下 Alice 可以完成的关卡数目：
如果 Alice 只完成关卡 0 ，Bob 完成剩下的所有关卡，那么 Alice 获得 1 分，Bob 获得 4 分。
如果 Alice 完成到关卡 1 ，Bob 完成剩下的所有关卡，那么 Alice 获得 2 分，Bob 获得 3 分。
如果 Alice 完成到关卡 2 ，Bob 完成剩下的所有关卡，那么 Alice 获得 3 分，Bob 获得 2 分。
如果 Alice 完成到关卡 3 ，Bob 完成剩下的所有关卡，那么 Alice 获得 4 分，Bob 获得 1 分。
Alice 需要完成至少三个关卡获得更多的分数。
示例 3：

输入：possible = [0,0]
输出：-1
解释：
两名玩家只能各完成 1 个关卡，Alice 完成关卡 0 得到 -1 分，Bob 完成关卡 1 得到 -1 分。两名玩家得分相同，所以 Alice 无法得到更多分数。

提示：
`2 <= n == possible.length <= 10^5`
`possible[i]` 要么是 `0` 要么是 `1` 。
"""

from typing import List, Optional


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        # 将possible转换为得分：1 -> +1, 0 -> -1
        scores = [1 if p == 1 else -1 for p in possible]
        total = sum(scores)

        alice_score = 0
        # Alice至少完成1关，最多n-1关（Bob至少1关）
        for i in range(n - 1):
            alice_score += scores[i]
            bob_score = total - alice_score
            if alice_score > bob_score:
                return i + 1
        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum
#
# 解题思路:
# 将possible数组转换为得分数组（1得1分，0得-1分），计算总分。
# Alice从0开始依次完成关卡，维护前缀和。对于每个分割点i，Alice得分为前缀和，
# Bob得分为总分减去Alice得分。当Alice得分 > Bob得分时返回关卡数。
# 注意Alice和Bob各自至少完成1关，Alice最多完成n-1关。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 前缀和思想，不需要额外数组
# - Alice至少1关，Bob至少1关，边界条件
# - 一旦满足条件立即返回（最少关卡数）
