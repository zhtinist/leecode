"""
LeetCode #3376 - Minimum Time to Break Locks I
破解锁的最少时间 I
https://leetcode.cn/problems/minimum-time-to-break-locks-i/

Bob 被困在了一个地窖里，他需要破解 `n` 个锁才能逃出地窖，每一个锁都需要一定的 能量 才能打开。每一个锁需要的能量存放在一个数组 `strength` 里，其中 `strength[i]` 表示打开第 `i` 个锁需要的能量。
Bob 有一把剑，它具备以下的特征：
一开始剑的能量为 0 。
剑的能量增加因子 `x` 一开始的值为 1 。
每分钟，剑的能量都会增加当前的 `x` 值。
打开第 `i` 把锁，剑的能量需要到达 至少 `strength[i]` 。
打开一把锁以后，剑的能量会变回 0 ，`x` 的值会增加一个给定的值 `k` 。
你的任务是打开所有 `n` 把锁并逃出地窖，请你求出需要的 最少 分钟数。
请你返回 Bob 打开所有 `n` 把锁需要的 最少 时间。

示例 1：

输入：strength = [3,4,1], k = 1
输出：4
解释：   	 		 			时间 			能量 			x 			操作 			更新后的 x 		 		 			0 			0 			1 			什么也不做 			1 		 		 			1 			1 			1 			打开第 3 把锁 			2 		 		 			2 			2 			2 			什么也不做 			2 		 		 			3 			4 			2 			打开第 2 把锁 			3 		 		 			4 			3 			3 			打开第 1 把锁 			3
无法用少于 4 分钟打开所有的锁，所以答案为 4 。
示例 2：

输入：strength = [2,5,4], k = 2
输出：5
解释：   	 		 			时间 			能量 			x 			操作 			更新后的 x 		 		 			0 			0 			1 			什么也不做 			1 		 		 			1 			1 			1 			什么也不做 			1 		 		 			2 			2 			1 			打开第 1 把锁 			3 		 		 			3 			3 			3 			什么也不做 			3 		 		 			4 			6 			3 			打开第 2 把锁 			5 		 		 			5 			5 			5 			打开第 3 把锁 			7
无法用少于 5 分钟打开所有的锁，所以答案为 5 。

提示：
`n == strength.length`
`1 <= n <= 8`
`1 <= k <= 10`
`1 <= strength[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        import math
        n = len(strength)
        size = 1 << n
        INF = 10 ** 18
        dp = [INF] * size
        dp[0] = 0

        for mask in range(size):
            if dp[mask] == INF:
                continue
            broken = mask.bit_count()
            x = 1 + k * broken
            for i in range(n):
                if not (mask >> i) & 1:
                    time = math.ceil(strength[i] / x)
                    new_mask = mask | (1 << i)
                    if dp[mask] + time < dp[new_mask]:
                        dp[new_mask] = dp[mask] + time

        return dp[size - 1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Breadth-First Search, Array, Dynamic Programming, Backtracking, Bitmask
#
# 解题思路:
# n<=8，使用状态压缩DP。dp[mask]表示已打开mask集合的锁所需的最少分钟数。
# 打开下一把锁i需要 ceil(strength[i] / x) 分钟，其中 x = 1 + k * popcount(mask)。
# 因为每打开一把锁后能量归零，x增加k。遍历所有状态转移即可。
#
# 时间复杂度: O(2^n * n)，n<=8
# 空间复杂度: O(2^n)
#
# 关键点:
# - 每打开一把锁后能量归零、x增加k，所以打开锁的顺序影响总时间
# - x = 1 + k * 已打开锁的数量
# - 打开第i把锁需要 ceil(s_i / x) 分钟等待能量积累
