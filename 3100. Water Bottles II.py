"""
LeetCode #3100 - Water Bottles II
换水问题 II
https://leetcode.cn/problems/water-bottles-ii/

给你两个整数 `numBottles` 和 `numExchange` 。
`numBottles` 代表你最初拥有的满水瓶数量。在一次操作中，你可以执行以下操作之一：
喝掉任意数量的满水瓶，使它们变成空水瓶。
用 `numExchange` 个空水瓶交换一个满水瓶。然后，将 `numExchange` 的值增加 1 。
注意，你不能使用相同的 `numExchange` 值交换多批空水瓶。例如，如果 `numBottles == 3` 并且 `numExchange == 1` ，则不能用 `3` 个空水瓶交换成 `3` 个满水瓶。
返回你 最多 可以喝到多少瓶水。

示例 1：
输入：numBottles = 13, numExchange = 6 输出：15 解释：上表显示了满水瓶的数量、空水瓶的数量、numExchange 的值，以及累计喝掉的水瓶数量。
示例 2：
输入：numBottles = 10, numExchange = 3 输出：13 解释：上表显示了满水瓶的数量、空水瓶的数量、numExchange 的值，以及累计喝掉的水瓶数量。

提示：
`1 <= numBottles <= 100 `
`1 <= numExchange <= 100`
"""

from typing import List, Optional


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        drunk = 0

        while full > 0 or empty >= numExchange:
            # 喝掉所有满水瓶
            drunk += full
            empty += full
            full = 0

            # 用空瓶换满瓶
            while empty >= numExchange:
                empty -= numExchange
                full += 1
                numExchange += 1

        return drunk



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Simulation
#
# 解题思路:
# 模拟整个过程：每次将满水瓶全部喝完变为空瓶，然后用空瓶尽量兑换满瓶，
# 每次兑换后numExchange增加1。重复直到既没有满瓶也无法兑换为止。
# 由于numExchange每次+1，空瓶兑换能力逐渐下降，模拟会自然终止。
#
# 时间复杂度: O(sqrt(numBottles + numExchange))
# 空间复杂度: O(1)
#
# 关键点:
# - 每次喝掉所有满瓶是最优策略
# - 兑换后numExchange递增，使得兑换条件越来越严格
# - 模拟直到无法兑换且无满瓶为止
