"""
LeetCode #3765 - Complete Prime Number
完全质数
https://leetcode.cn/problems/complete-prime-number/

给你一个整数 `num`。
如果一个数 `num` 的每一个 前缀 和每一个 后缀 都是 质数，则称该数为 完全质数。
如果 `num` 是完全质数，返回 `true`，否则返回 `false`。
注意：
一个数的 前缀 是由该数的 前 `k` 位数字构成的。
一个数的 后缀 是由该数的 后 `k` 位数字构成的。
质数 是大于 1 且只有两个因子（1 和它本身）的自然数。
个位数只有在它是 质数 时才被视为完全质数。

示例 1：

输入：num = 23
输出：true
解释：
`num = 23` 的前缀是 2 和 23，它们都是质数。
`num = 23` 的后缀是 3 和 23，它们都是质数。
所有的前缀和后缀都是质数，所以 23 是完全质数，答案是 `true`。
示例 2：

输入：num = 39
输出：false
解释：
`num = 39` 的前缀是 3 和 39。3 是质数，但 39 不是质数。
`num = 39` 的后缀是 9 和 39。9 和 39 都不是质数。
至少有一个前缀或后缀不是质数，所以 39 不是完全质数，答案是 `false`。
示例 3：

输入：num = 7
输出：true
解释：
7 是质数，所以它的所有前缀和后缀都是质数，答案是 `true`。

提示：
`1 <= num <= 10^9`
"""

from typing import List, Optional


class Solution:
    def isCompletePrime(self, num: int) -> bool:
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            i = 3
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True

        s = str(num)
        # Check all prefixes
        for i in range(1, len(s) + 1):
            prefix = int(s[:i])
            if not is_prime(prefix):
                return False

        # Check all suffixes
        for i in range(len(s)):
            suffix = int(s[i:])
            if not is_prime(suffix):
                return False

        return True










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Enumeration, Number Theory
#
# 解题思路:
# 直接枚举 num 的所有前缀和后缀，分别判断是否为质数。
# 前缀：s[0:1], s[0:2], ..., s[0:n]
# 后缀：s[0:n], s[1:n], ..., s[n-1:n]
# num <= 10^9 最多 10 位，所以最多检查 20 次质数判断，每次 O(sqrt(num))。
#
# 时间复杂度: O(log(num) * sqrt(num))
# 空间复杂度: O(log(num))
#
# 关键点:
# - 需要同时检查所有前缀和所有后缀
# - 质数判断注意 1 不是质数
