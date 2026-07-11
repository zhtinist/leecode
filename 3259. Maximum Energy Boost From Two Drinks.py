"""
LeetCode #3259 - Maximum Energy Boost From Two Drinks
超级饮料的最大强化能量
https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/

来自未来的体育科学家给你两个整数数组 `energyDrinkA` 和 `energyDrinkB`，数组长度都等于 `n`。这两个数组分别代表 A、B 两种不同能量饮料每小时所能提供的强化能量。
你需要每小时饮用一种能量饮料来 最大化 你的总强化能量。然而，如果从一种能量饮料切换到另一种，你需要等待一小时来梳理身体的能量体系（在那个小时里你将不会获得任何强化能量）。
返回在接下来的 `n` 小时内你能获得的 最大 总强化能量。
注意 你可以选择从饮用任意一种能量饮料开始。

示例 1：

输入：energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]
输出：5
解释：
要想获得 5 点强化能量，需要选择只饮用能量饮料 A（或者只饮用 B）。
示例 2：

输入：energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]
输出：7
解释：
第一个小时饮用能量饮料 A。
切换到能量饮料 B ，在第二个小时无法获得强化能量。
第三个小时饮用能量饮料 B ，并获得强化能量。

提示：
`n == energyDrinkA.length == energyDrinkB.length`
`3 <= n <= 10^5`
`1 <= energyDrinkA[i], energyDrinkB[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        # dpA[i]: 前 i 小时，最后一小时喝 A 的最大能量
        # dpB[i]: 前 i 小时，最后一小时喝 B 的最大能量
        dpA = [0] * n
        dpB = [0] * n
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        for i in range(1, n):
            # 继续喝 A，或者从 B 切换（切换那小时无能量）
            dpA[i] = max(dpA[i-1], dpB[i-2] if i >= 2 else 0) + energyDrinkA[i]
            dpB[i] = max(dpB[i-1], dpA[i-2] if i >= 2 else 0) + energyDrinkB[i]
        return max(dpA[-1], dpB[-1])










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# DP 状态定义：
# dpA[i]: 第 i 小时结束后最后喝的是 A 的最大能量
# dpB[i]: 第 i 小时结束后最后喝的是 B 的最大能量
# 转移：
# - 继续喝同一种：dpA[i] = dpA[i-1] + energyDrinkA[i]
# - 从另一种切换：切换需要等待 1 小时（第 i-1 小时无能量），
#   所以 dpA[i] = dpB[i-2] + energyDrinkA[i]（i >= 2）
# 初始条件：dpA[0] = A[0], dpB[0] = B[0]
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)，可优化到 O(1)
#
# 关键点:
# - 切换饮料需要一个冷却小时（无能量收入）
# - DP 状态中需要考虑切换成本
