"""
LeetCode #3233 - Find the Count of Numbers Which Are Not Special
统计不是特殊数字的数字数量
https://leetcode.cn/problems/find-the-count-of-numbers-which-are-not-special/

给你两个 正整数 `l` 和 `r`。对于任何数字 `x`，`x` 的所有正因数（除了 `x` 本身）被称为 `x` 的 真因数。
如果一个数字恰好仅有两个 真因数，则称该数字为 特殊数字。例如：
数字 4 是 特殊数字，因为它的真因数为 1 和 2。
数字 6 不是 特殊数字，因为它的真因数为 1、2 和 3。
返回区间 `[l, r]` 内 不是 特殊数字 的数字数量。

示例 1：

输入： l = 5, r = 7
输出： 3
解释：
区间 `[5, 7]` 内不存在特殊数字。
示例 2：

输入： l = 4, r = 16
输出： 11
解释：
区间 `[4, 16]` 内的特殊数字为 4 和 9。

提示：
`1 <= l <= r <= 10^9`
"""

from typing import List, Optional


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        import math
        # 特殊数字：恰好有两个真因数 → 该数是一个质数的平方
        # 即 x = p^2，其中 p 是质数
        # 这样的数只有 3 个因数：1, p, p^2（真因数为 1 和 p，恰好 2 个）
        limit = int(math.isqrt(r)) + 1
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.isqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        special = 0
        for p in range(2, limit + 1):
            if is_prime[p]:
                sq = p * p
                if l <= sq <= r:
                    special += 1
        total = r - l + 1
        return total - special










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Number Theory
#
# 解题思路:
# "恰好有两个真因数"：如果一个数 x 有恰好 2 个真因数，加上 1 和自身共 4 个因数？
# 不，真因数不包括自身。设 x 有 n 个因数（含 1 和 x），则真因数有 n-2 个。
# 恰好 2 个真因数 → n = 4 个因数（含 1 和 x）。
# 有恰好 4 个因数的数只能是 p^3（质数的立方，因数为 1,p,p^2,p^3）或 p*q（两个不同质数的积，因数为 1,p,q,pq）。
# 等等，重新读题："恰好仅有两个真因数"→ 真因数 = 所有正因数（除了 x 本身）。
# 所以 x 有 2 个真因数，加上 x 本身总共 3 个正因数。
# 有 3 个因数的数只能是质数的平方 p^2（因子：1, p, p^2）。
# 用埃氏筛找到 sqrt(r) 以内的所有质数，统计平方落在 [l, r] 内的个数。
#
# 时间复杂度: O(sqrt(r) log log sqrt(r))
# 空间复杂度: O(sqrt(r))
#
# 关键点:
# - 恰好 2 个真因数 ↔ 恰好 3 个正因数 ↔ p^2（p 为质数）
# - 埃氏筛预处理质数
