"""
LeetCode #2400 - Number of Ways to Reach a Position After Exactly k Steps
恰好移动 k 步到达某一位置的方法数目
https://leetcode.cn/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

给你两个 正 整数 `startPos` 和 `endPos` 。最初，你站在 无限 数轴上位置 `startPos` 处。在一步移动中，你可以向左或者向右移动一个位置。
给你一个正整数 `k` ，返回从 `startPos` 出发、恰好 移动 `k` 步并到达 `endPos` 的 不同 方法数目。由于答案可能会很大，返回对 `10^9 + 7` 取余 的结果。
如果所执行移动的顺序不完全相同，则认为两种方法不同。
注意：数轴包含负整数。

示例 1：
输入：startPos = 1, endPos = 2, k = 3 输出：3 解释：存在 3 种从 1 到 2 且恰好移动 3 步的方法： - 1 -> 2 -> 3 -> 2. - 1 -> 2 -> 1 -> 2. - 1 -> 0 -> 1 -> 2. 可以证明不存在其他方法，所以返回 3 。
示例 2：
输入：startPos = 2, endPos = 5, k = 10 输出：0 解释：不存在从 2 到 5 且恰好移动 10 步的方法。

提示：
`1 <= startPos, endPos, k <= 1000`
"""

from typing import List, Optional


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        """
        Combinatorics: let r = number of right moves, l = number of left moves.
        We need: r - l = endPos - startPos  and  r + l = k.
        Solving: r = (k + endPos - startPos) / 2.
        If r is a non-negative integer <= k, answer = C(k, r) % MOD, else 0.
        """
        MOD = 10 ** 9 + 7

        diff = endPos - startPos
        # r = (k + diff) / 2 must be integer and 0 <= r <= k
        if (k + diff) % 2 != 0:
            return 0
        r = (k + diff) // 2
        if r < 0 or r > k:
            return 0

        # Compute C(k, r) % MOD using multiplicative inverse
        # C(k, r) = k! / (r! * (k-r)!)
        # Use the formula: C(k, r) = product_{i=1..r} (k - r + i) / i
        # Optimize: choose the smaller of r and k-r
        r = min(r, k - r)
        numerator = 1
        denominator = 1
        for i in range(r):
            numerator = (numerator * (k - i)) % MOD
            denominator = (denominator * (i + 1)) % MOD

        # Modular inverse via Fermat's little theorem: a^(MOD-2) % MOD
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Dynamic Programming, Combinatorics
#
# 解题思路:
# 1. 设向右走 r 步，向左走 l 步。则有方程组：r - l = endPos - startPos 和 r + l = k。
# 2. 解得 r = (k + endPos - startPos) / 2。r 必须是整数且 0 <= r <= k，否则返回 0。
# 3. 问题转化为：从 k 步中选择 r 步向右走，即组合数 C(k, r)。
# 4. 使用乘法逆元（费马小定理）计算组合数取模：C(k, r) = k! / (r! * (k-r)!) % MOD。
#
# 时间复杂度: O(min(r, k-r)) — 计算组合数需要 O(r) 次乘法
# 空间复杂度: O(1) — 常数空间
#
# 关键点:
# - 将路径问题转化为组合数学问题，避免动态规划的 O(k^2) 空间
# - 需要判断 r 是否为整数（奇偶性检查）
# - 利用费马小定理求模逆元：a^(MOD-2) ≡ a^(-1) (mod MOD)，因为 MOD=1e9+7 是质数
# - 选择 r = min(r, k-r) 减少计算量
