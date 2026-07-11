"""
LeetCode #1921 - Eliminate Maximum Number of Monsters
消灭怪物的最大数量
https://leetcode.cn/problems/eliminate-maximum-number-of-monsters/

你正在玩一款电子游戏，在游戏中你需要保护城市免受怪物侵袭。给定一个 下标从 0 开始 且大小为 `n` 的整数数组 `dist` ，其中 `dist[i]` 是第 `i` 个怪物与城市的 初始距离（单位：千米）。
怪物以 恒定 的速度走向城市。每个怪物的速度都以一个长度为 `n` 的整数数组 `speed` 表示，其中 `speed[i]` 是第 `i` 个怪物的速度（单位：千米/分）。
你有一种武器，一旦充满电，就可以消灭 一个 怪物。但是，武器需要 一分钟 才能充电。武器在游戏开始时是充满电的状态，怪物从 第 0 分钟 时开始移动。
一旦任一怪物到达城市，你就输掉了这场游戏。如果某个怪物 恰好 在某一分钟开始时到达城市（距离表示为0），这也会被视为 输掉 游戏，在你可以使用武器之前，游戏就会结束。
返回在你输掉游戏前可以消灭的怪物的 最大 数量。如果你可以在所有怪物到达城市前将它们全部消灭，返回  `n` 。

示例 1：
输入：dist = [1,3,4], speed = [1,1,1] 输出：3 解释： 第 0 分钟开始时，怪物的距离是 [1,3,4]，你消灭了第一个怪物。 第 1 分钟开始时，怪物的距离是 [X,2,3]，你消灭了第二个怪物。 第 3 分钟开始时，怪物的距离是 [X,X,2]，你消灭了第三个怪物。 所有 3 个怪物都可以被消灭。
示例 2：
输入：dist = [1,1,2,3], speed = [1,1,1,1] 输出：1 解释： 第 0 分钟开始时，怪物的距离是 [1,1,2,3]，你消灭了第一个怪物。 第 1 分钟开始时，怪物的距离是 [X,0,1,2]，所以你输掉了游戏。 你只能消灭 1 个怪物。
示例 3：
输入：dist = [3,2,4], speed = [5,3,2] 输出：1 解释： 第 0 分钟开始时，怪物的距离是 [3,2,4]，你消灭了第一个怪物。 第 1 分钟开始时，怪物的距离是 [X,0,2]，你输掉了游戏。  你只能消灭 1 个怪物。

提示：
`n == dist.length == speed.length`
`1 <= n <= 10^5`
`1 <= dist[i], speed[i] <= 10^5`
"""

from typing import List, Optional


import math

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        # Time needed for each monster to reach the city
        arrival_times = []
        for d, s in zip(dist, speed):
            # ceil(d / s) - the minute when monster arrives
            # We need to eliminate before or at the same minute
            # Actually: monster arrives at time d/s (minutes from start)
            # If monster arrives at exactly minute t, it reaches at the START of minute t
            # We can eliminate at minute 0, 1, 2, ...
            # So we need: elimination_minute < arrival_time
            # arrival_time = ceil(d / s) because monster arrives at start of that minute
            arrival_times.append((d + s - 1) // s)  # ceil division

        arrival_times.sort()

        for i in range(n):
            # At minute i, we can eliminate the (i+1)-th monster
            # Monster i must arrive after minute i
            if arrival_times[i] <= i:
                return i

        return n



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 贪心 + 排序。
# 1. 计算每个怪物到达城市所需的时间：ceil(dist[i] / speed[i])。
#    怪物在第 t 分钟开始时到达（如果恰好在 t=0 时到达也失败）。
# 2. 按到达时间排序，优先消灭最早到达的怪物。
# 3. 在第 i 分钟可以消灭一个怪物（第 0 分钟武器已充能），
#    需要在第 i 只怪物的到达时间之前消灭它。
# 4. 如果某只怪物的到达时间 <= 当前分钟 i，游戏失败。
#
# 时间复杂度: O(n log n) — 排序
# 空间复杂度: O(n) — 存储到达时间
#
# 关键点:
# - 怪物到达时间 = ceil(dist/speed)，使用 (d + s - 1) // s
# - 第 0 分钟就可以消灭一只怪物
# - 怪物正好在 t 分钟开始时到达也算失败
# - 贪心选择最早到达的怪物优先消灭
