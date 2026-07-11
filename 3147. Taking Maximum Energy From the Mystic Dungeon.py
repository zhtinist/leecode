"""
LeetCode #3147 - Taking Maximum Energy From the Mystic Dungeon
从魔法师身上吸取的最大能量
https://leetcode.cn/problems/taking-maximum-energy-from-the-mystic-dungeon/

在神秘的地牢中，`n` 个魔法师站成一排。每个魔法师都拥有一个属性，这个属性可以给你提供能量。有些魔法师可能会给你负能量，即从你身上吸取能量。
你被施加了一种诅咒，当你从魔法师 `i` 处吸收能量后，你将被立即传送到魔法师 `(i + k)` 处。这一过程将重复进行，直到你到达一个不存在 `(i + k)` 的魔法师为止。
换句话说，你将选择一个起点，然后以 `k` 为间隔跳跃，直到到达魔法师序列的末端，在过程中吸收所有的能量。
给定一个数组 `energy` 和一个整数`k`，返回你能获得的 最大 能量。

示例 1：

输入： energy = [5,2,-10,-5,1], k = 3
输出： 3
解释：可以从魔法师 1 开始，吸收能量 2 + 1 = 3。
示例 2：

输入： energy = [-2,-3,-1], k = 2
输出： -1
解释：可以从魔法师 2 开始，吸收能量 -1。

提示：
`1 <= energy.length <= 10^5`
`-1000 <= energy[i] <= 1000`
`1 <= k <= energy.length - 1`
"""

from typing import List, Optional


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = float('-inf')
        # dp[i] = 从i开始到尾部的能量和
        dp = energy[:]
        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] += dp[i + k]
            ans = max(ans, dp[i])
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Prefix Sum
#
# 解题思路:
# 从右向左动态规划。dp[i]表示从位置i开始跳到末尾能获得的总能量。
# 转移：dp[i] = energy[i] + (dp[i+k] if i+k < n else 0)。
# 最终答案为max(dp[i])。实际上可以复用energy数组作为dp数组节省空间。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 从后往前计算后缀和
# - 跳跃固定步长k，不同起点之间独立
# - 直接取所有后缀和的最大值
