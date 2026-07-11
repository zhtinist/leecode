"""
LeetCode #2749 - Minimum Operations to Make the Integer Zero
得到整数零需要执行的最少操作数
https://leetcode.cn/problems/minimum-operations-to-make-the-integer-zero/

给你两个整数：`num1` 和 `num2` 。
在一步操作中，你需要从范围 `[0, 60]` 中选出一个整数 `i` ，并从 `num1` 减去 `2^i + num2` 。
请你计算，要想使 `num1` 等于 `0` 需要执行的最少操作数，并以整数形式返回。
如果无法使 `num1` 等于 `0` ，返回 `-1` 。

示例 1：
输入：num1 = 3, num2 = -2 输出：3 解释：可以执行下述步骤使 3 等于 0 ： - 选择 i = 2 ，并从 3 减去 2^2 + (-2) ，num1 = 3 - (4 + (-2)) = 1 。 - 选择 i = 2 ，并从 1 减去 2^2 + (-2) ，num1 = 1 - (4 + (-2)) = -1 。 - 选择 i = 0 ，并从 -1 减去 2^0 + (-2) ，num1 = (-1) - (1 + (-2)) = 0 。 可以证明 3 是需要执行的最少操作数。
示例 2：
输入：num1 = 5, num2 = 7 输出：-1 解释：可以证明，执行操作无法使 5 等于 0 。

提示：
`1 <= num1 <= 10^9`
`-10^9 <= num2 <= 10^9`
"""

from typing import List, Optional


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            target = num1 - k * num2
            if target < 0:
                continue
            bits = target.bit_count()
            if bits <= k <= target:
                return k
        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Brainteaser, Enumeration
#
# 解题思路:
# 假设执行 k 次操作，每次选择 i_j，则减去总和 = sum(2^(i_j)) + k*num2 = target。
# 令 target = num1 - k*num2。target 必须能表示为 k 个 2 的幂次之和。
# target 中 1 的位数 bits 是需要的最少操作数，最多可以有 target 个操作（全部拆成 2^0）。
# 所以需要满足 bits <= k <= target。枚举 k 从 1 到 60 找到最小的满足条件的 k。
#
# 时间复杂度: O(60) = O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - k 次操作减去 k*num2 是固定的，剩余部分需要用 2 的幂次表示
# - target 的 popcount 是最少需要的 2 的幂次数
# - target 自身是最大可能的 2 的幂次数（全拆成 2^0）
# - 条件: bit_count(target) <= k <= target
