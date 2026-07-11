"""
LeetCode #1922 - Count Good Numbers
统计好数字的数目
https://leetcode.cn/problems/count-good-numbers/

我们称一个数字字符串是 好数字 当它满足（下标从 0 开始）偶数 下标处的数字为 偶数 且 奇数 下标处的数字为 质数 （`2`，`3`，`5` 或 `7`）。
比方说，`"2582"` 是好数字，因为偶数下标处的数字（`2` 和 `8`）是偶数且奇数下标处的数字（`5` 和 `2`）为质数。但 `"3245"` 不是 好数字，因为 `3` 在偶数下标处但不是偶数。
给你一个整数 `n` ，请你返回长度为 `n` 且为好数字的数字字符串 总数 。由于答案可能会很大，请你将它对 `10^9 + 7` 取余后返回 。
一个 数字字符串 是每一位都由 `0` 到 `9` 组成的字符串，且可能包含前导 0 。

示例 1：
输入：n = 1 输出：5 解释：长度为 1 的好数字包括 "0"，"2"，"4"，"6"，"8" 。
示例 2：
输入：n = 4 输出：400
示例 3：
输入：n = 50 输出：564908303

提示：
`1 <= n <= 10^15`
"""

from typing import List, Optional


MOD = 10 ** 9 + 7

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Even indices (0, 2, 4, ...): 5 choices (0, 2, 4, 6, 8)
        # Odd indices (1, 3, 5, ...): 4 choices (2, 3, 5, 7)

        even_count = (n + 1) // 2  # number of even indices
        odd_count = n // 2          # number of odd indices

        def fast_pow(base: int, exp: int) -> int:
            result = 1
            while exp > 0:
                if exp & 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp >>= 1
            return result

        return (fast_pow(5, even_count) * fast_pow(4, odd_count)) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Recursion, Math
#
# 解题思路:
# 数学 + 快速幂。
# 1. 偶数下标位置（0, 2, 4, ...）有 5 种选择：0, 2, 4, 6, 8。
# 2. 奇数下标位置（1, 3, 5, ...）有 4 种选择：2, 3, 5, 7。
# 3. 总方案数 = 5^(偶数位置数) * 4^(奇数位置数)。
# 4. 使用快速幂计算大指数，结果对 10^9+7 取模。
# 5. n 最大 10^15，必须用 O(log n) 的快速幂。
#
# 时间复杂度: O(log n) — 快速幂
# 空间复杂度: O(1) — 常数空间
#
# 关键点:
# - 偶数位置数和奇数位置数的计算：(n+1)//2 和 n//2
# - 快速幂处理大指数
# - 每一步都取模防止溢出
# - n 可能为 0（但题目保证 n>=1）
